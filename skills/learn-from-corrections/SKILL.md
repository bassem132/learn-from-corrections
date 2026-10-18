---
name: learn-from-corrections
description: Turn the user's corrections into durable rules in AGENTS.md (or CLAUDE.md). Use when the user corrects you, says "no, do it this way", "don't do X again", "remember that", "always/never ...", or when the same mistake has happened twice in a session.
author: Bassem Mo'men
license: MIT
---

# Learn from corrections

A correction the user has to repeat is a correction you failed to learn. This skill turns one-off corrections into short, durable project rules so the next session starts already knowing them.

## When to use

- The user corrects your output, approach, naming, style or tooling choice.
- The user says "always", "never", "from now on", "remember", "stop doing".
- You notice you made the same mistake twice.

Do **not** use it for one-time task details ("rename this variable to `x`") that won't matter in future sessions.

## Where rules live

1. `AGENTS.md` at the repo root — read by Codex, Cursor, Claude Code (via import) and most other agents. Prefer this.
2. `CLAUDE.md` — if the project only has this file, use it. If both exist and `CLAUDE.md` contains `@AGENTS.md`, write to `AGENTS.md`.
3. If neither exists, offer to create `AGENTS.md` from [templates/AGENTS.md](templates/AGENTS.md).

Personal preferences that apply to every project (tone, language, editor) go to the user-level file instead (`~/.claude/CLAUDE.md`, `~/.codex/AGENTS.md`), never the repo.

## Procedure

1. **Extract the rule.** Rewrite the correction as one imperative line with the reason:
   `- Use pnpm, not npm — the lockfile is pnpm-lock.yaml.`
   Make it specific enough to act on and general enough to apply next time.
2. **Read the existing file** and check for:
   - **Duplicate** — the rule already exists (maybe worded differently). Don't add it; if you broke an existing rule, say so and strengthen its wording instead.
   - **Conflict** — an existing rule says the opposite. Show both and ask which wins; replace the loser.
   - **Wrong section** — put it under the matching heading (Commands, Code style, Testing, Git, Don'ts).
3. **Ask before saving.** Show the exact line and the file it goes into:
   > Add to `AGENTS.md` under **Testing**: `- Run tests with `pnpm test -- --run`; watch mode hangs CI.` OK?
   Save only on a yes. If the user rewords it, use their wording.
4. **Keep the file small.** If it passes ~150 lines, propose merging overlapping rules or moving detail into a linked doc. Every line costs context in every future session.
5. **Apply it now.** Redo the corrected work following the new rule.

## Rule quality checklist

- One line, imperative, starts with a verb.
- Includes *why* when the reason isn't obvious — agents follow rules with reasons more reliably.
- Names real commands, paths and tools from this repo.
- No vague rules ("write clean code", "be careful"). If you can't check whether it was followed, rewrite it.

See [examples.md](examples.md) for good and bad rules.
