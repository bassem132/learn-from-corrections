---
name: learn-from-corrections
description: Turn the user's corrections into short, durable rules in AGENTS.md or CLAUDE.md so the same mistake never happens twice. Use when the user corrects a reusable convention ("no, use X in this repo", "we do Y here", "don't do that again", "remember this", "from now on…"), when you make the same mistake twice in a session, or when asked to clean up or audit an AGENTS.md/CLAUDE.md. Do not use for one-off task details, personal preferences that belong in the assistant's own memory, or a bare "always"/"never" inside an ordinary instruction.
author: Bassem Moumen
license: MIT
---

# Learn from corrections

A correction the user has to repeat is one you failed to learn. This skill turns one-off corrections into short, durable project rules, so the next session already knows them.

## When to use

- The user corrects your output, approach, naming, style or tool choice.
- The user says "from now on", "remember", "don't do that again", or states a convention that clearly applies to the whole repo.
- You notice you made the same mistake twice.
- The user asks you to tidy, audit or shrink their rules file.

Don't use it for one-time details ("rename this to `x`"), a bare "always"/"never" in a normal instruction, or anything secret or specific to one machine.

**Don't interrupt the work.** Ask at most once per turn. If several corrections pile up, finish the task first and offer them together as one short list. If the same rule has already been added or declined this session, don't ask again.

**Rules file vs. assistant memory.** Repo conventions that every contributor and every tool should follow go in `AGENTS.md` / `CLAUDE.md` (versioned, shared). Personal preferences about how the user likes to work with the assistant belong in the assistant's own memory, if it has one. Put a rule in one place, not both.

## Procedure

1. **Extract the rule.** Rewrite the correction as one imperative line that includes the reason:
   `- Use pnpm, not npm — the lockfile is pnpm-lock.yaml.`
   It should be specific enough to act on and general enough to apply next time. If the correction was only "that's wrong", ask what the right behaviour is before writing anything.
2. **Pick the file and scope.** Use the narrowest file that covers every place the rule applies: repo root, a nested package, or the user-level file. See [reference/where-rules-go.md](reference/where-rules-go.md) for the file each tool reads. If no file exists, offer to create `AGENTS.md` from [templates/AGENTS.md](templates/AGENTS.md).
3. **Check the existing file.** Read it and look for:
   - **A duplicate.** The rule is already there, maybe in other words. Don't add it again. If you broke an existing rule, say so and make its wording clearer instead.
   - **A conflict.** An existing rule says the opposite. Show both and ask which one wins, then replace the other.
   - **The right section.** File it under Commands, Code style, Testing, Git or Don'ts.
4. **Ask before saving.** Show the exact line and where it goes:
   > Add to `AGENTS.md` under **Testing**: `- Run tests with pnpm test -- --run; watch mode hangs CI.` OK?
   Save only after the user says yes. If they reword it, use their wording.
5. **Lint after saving.** Run the bundled linter, which flags duplicates, vague rules, missing reasons, leftover placeholders and a file that is too large:
   ```bash
   python3 <skill-dir>/scripts/lint_agents_md.py AGENTS.md
   ```
   Fix what it reports, or tell the user why a warning doesn't apply.
6. **Keep the file small.** Every line costs context in every future session. Once the file passes ~150 lines, propose merging overlapping rules or moving detail into a linked doc.
7. **Apply the rule now.** Redo the corrected work so it follows the new rule.

## Rule quality checklist

- One line, imperative, starts with a verb.
- Says *why* when the reason isn't obvious. Agents follow rules that have reasons more reliably.
- Names real commands, paths and tools from this repo.
- Can be checked. If you can't tell whether a rule was followed, rewrite it.
- Calm wording. Capitals and "!!!" don't improve compliance; a reason does.

## Files in this skill

- [examples.md](examples.md): corrections turned into rules, good vs bad wording, handling a conflict.
- [reference/where-rules-go.md](reference/where-rules-go.md): which file each tool reads, and when to move a rule.
- [templates/AGENTS.md](templates/AGENTS.md): a starter rules file.
- [scripts/lint_agents_md.py](scripts/lint_agents_md.py): the rules-file linter (Python 3.8+, no dependencies).
