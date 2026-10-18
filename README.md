# Learn from corrections

Turns your corrections into short, durable rules in AGENTS.md so your AI agent stops repeating the same mistakes.

A portable agent skill (`SKILL.md`) that works in **Claude Code**, **Codex** and **Cursor**.

## Install

### Claude Code (plugin)

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

### Cursor

Copy the folder into your project's `.cursor/skills/`, or paste the body of `SKILL.md` into a rule in `.cursor/rules/learn-from-corrections.mdc`.

## What's inside

```
skills/learn-from-corrections/SKILL.md              the skill
skills/learn-from-corrections/examples.md           good and bad rules
skills/learn-from-corrections/templates/AGENTS.md   starter AGENTS.md
```

See [skills/learn-from-corrections/SKILL.md](skills/learn-from-corrections/SKILL.md) for when it triggers and what it does.

## Author

Bassem Mo’men — [@bassem132](https://github.com/bassem132)

## License

MIT — see [LICENSE](LICENSE).
