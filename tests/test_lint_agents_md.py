import os, subprocess, sys, tempfile, unittest

HERE = os.path.dirname(os.path.abspath(__file__))
SCRIPT = os.path.join(HERE, "..", "skills", "learn-from-corrections", "scripts", "lint_agents_md.py")
TEMPLATE = os.path.join(HERE, "..", "skills", "learn-from-corrections", "templates", "AGENTS.md")


def run(text):
    with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False) as fh:
        fh.write(text)
    try:
        out = subprocess.run([sys.executable, SCRIPT, fh.name], capture_output=True, text=True)
        return out.returncode, out.stdout
    finally:
        os.unlink(fh.name)


class LintTests(unittest.TestCase):
    def test_clean_file_passes(self):
        code, out = run("# AGENTS.md\n\n## Commands\n- Test: `pnpm test`\n\n## Don'ts\n"
                        "- Never edit src/generated/ — regenerate with pnpm codegen.\n")
        self.assertEqual(code, 0, out)

    def test_duplicate_detected(self):
        code, out = run("## Style\n- Use pnpm, not npm — lockfile is pnpm-lock.yaml.\n"
                        "- Use pnpm not npm, the lockfile is pnpm-lock.yaml.\n")
        self.assertEqual(code, 1)
        self.assertIn("[duplicate]", out)

    def test_vague_rule_detected(self):
        code, out = run("## Style\n- Follow best practices for tests.\n")
        self.assertIn("[vague]", out)

    def test_strict_rule_without_reason(self):
        code, out = run("## Don'ts\n- Never touch the payments folder\n")
        self.assertIn("[no-reason]", out)

    def test_shouting(self):
        code, out = run("## Git\n- NEVER EVER commit to main!!! — CI deploys it.\n")
        self.assertIn("[shouting]", out)

    def test_size_limit(self):
        code, out = run("## Rules\n" + "".join("- Use tool%d for job%d — it's the standard.\n" % (i, i) for i in range(160)))
        self.assertIn("[size]", out)

    def test_code_fences_ignored(self):
        code, out = run("## Commands\n```\n- never do this\n- never do this\n```\n- Test: `make test`\n")
        self.assertEqual(code, 0, out)

    def test_template_placeholders_flagged(self):
        code, out = subprocess.run([sys.executable, SCRIPT, TEMPLATE], capture_output=True, text=True).returncode, ""
        self.assertEqual(code, 1)

    def test_missing_file(self):
        out = subprocess.run([sys.executable, SCRIPT, "/nonexistent/AGENTS.md"], capture_output=True, text=True)
        self.assertEqual(out.returncode, 2)


if __name__ == "__main__":
    unittest.main()
