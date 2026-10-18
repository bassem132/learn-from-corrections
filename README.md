# Learn from corrections

Every time you correct your AI agent, that lesson is lost when the session ends. This skill turns each correction into a one-line rule in `AGENTS.md`, checked against the rules already there, so the next session already knows it.

A portable agent skill (`SKILL.md` plus scripts and references) for **Claude Code**, **Codex** and **Cursor**. The scripts have no dependencies (Python 3.8+ / bash 3.2+).

## What's inside

| File | What it does |
| --- | --- |
| `skills/learn-from-corrections/SKILL.md` | When it triggers and the step-by-step procedure |
| `skills/learn-from-corrections/examples.md` | Corrections turned into rules, good vs bad wording, handling conflicts |
| `skills/learn-from-corrections/reference/where-rules-go.md` | Which file Claude Code, Codex and Cursor read; repo vs user vs nested rules |
| `skills/learn-from-corrections/templates/AGENTS.md` | Starter rules file |
| `skills/learn-from-corrections/scripts/lint_agents_md.py` | Linter: duplicates, vague rules, missing reasons, placeholders, size |
| `adapters/cursor/learn-from-corrections.mdc` | Ready-made Cursor rule |
| `adapters/codex/AGENTS.snippet.md` | Short version to paste into any `AGENTS.md` |
| `evals/evals.json` | Test prompts: should it trigger, and what should the agent do |
| `tests/` | Unit tests for the scripts |

## Install

### Claude Code (plugin, recommended)

```
/plugin marketplace add bassem132/learn-from-corrections
/plugin install learn-from-corrections@learn-from-corrections
```

### Claude Code (manual)

```bash
git clone https://github.com/bassem132/learn-from-corrections.git
cp -r learn-from-corrections/skills/learn-from-corrections ~/.claude/skills/
```

### Codex

```bash
cp -r learn-from-corrections/skills/learn-from-corrections ~/.codex/skills/
```

Or paste `adapters/codex/AGENTS.snippet.md` into your `AGENTS.md`.

### Cursor

```bash
mkdir -p .cursor/rules .cursor/skills
cp learn-from-corrections/adapters/cursor/learn-from-corrections.mdc .cursor/rules/
cp -r learn-from-corrections/skills/learn-from-corrections .cursor/skills/      # so the agent can run the scripts
```

## Try the script

```bash
python3 skills/learn-from-corrections/scripts/lint_agents_md.py path/to/AGENTS.md
```

## Develop

```bash
python3 -m unittest discover -s tests -v
claude plugin validate .
```

To check that the skill changes behaviour, run the prompts in `evals/evals.json` in a fresh session with the skill installed. Every `expect` item should hold, and prompts with `should_trigger: false` must not load the skill.

## Author

Bassem Mo’men · [@bassem132](https://github.com/bassem132)

## License

MIT, see [LICENSE](LICENSE).
