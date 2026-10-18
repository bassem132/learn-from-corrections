# Where rules go

Pick the narrowest file that covers every place the rule applies.

## Scope

| The rule is about… | Put it in |
| --- | --- |
| This repo: commands, layout, libraries, conventions | `AGENTS.md` at the repo root |
| One part of a monorepo (e.g. `apps/web`) | `apps/web/AGENTS.md` (agents read the nearest file) |
| You, in every project: language, tone, git habits | Your user-level file (below) |
| A secret, a path on your machine, a personal token | **Nowhere.** Never write these into rules. |

## File locations per tool

| Tool | Repo file | User-level file |
| --- | --- | --- |
| Codex | `AGENTS.md` (nested files apply to their folder) | `~/.codex/AGENTS.md` |
| Cursor | `AGENTS.md`, or `.cursor/rules/*.mdc` | User Rules in Cursor Settings |
| Claude Code | `CLAUDE.md` (put `@AGENTS.md` in it to share one file) | `~/.claude/CLAUDE.md` |

To serve all three from one source, keep the rules in `AGENTS.md` and make `CLAUDE.md` a single line:

```markdown
@AGENTS.md
```

## Moving a rule

- **Repo → user:** the user repeats the same correction in a second, unrelated project.
- **User → repo:** a personal rule turns out to be a team convention others need too.
- **Root → nested:** the rule only applies to one package and confuses work elsewhere.

When moving, delete the old line in the same edit so the rule never exists twice.

## Sections

Use these headings so rules are easy to find and dedupe:

- **Project**: one or two lines about what the repo is.
- **Commands**: install, dev, test, lint, build, with the exact command.
- **Code style**: naming, patterns, libraries to use or avoid.
- **Testing**: where tests go, how to run one test, what must be tested.
- **Git**: branching, commits, what needs approval.
- **Don'ts**: hard limits (generated files, prod data, secrets).
