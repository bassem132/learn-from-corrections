# Examples

## Correction → rule

| What the user said | Rule to save |
| --- | --- |
| "Stop using npm, we use pnpm." | `- Use pnpm for all installs and scripts — the repo uses pnpm-lock.yaml.` |
| "Don't touch the generated files." | `- Never edit files in src/generated/; regenerate them with pnpm codegen.` |
| "Why did you add a new date library? We have dayjs." | `- Use dayjs for dates; don't add new date libraries.` |
| "Tests go next to the file, not in __tests__." | `- Put tests beside the source file as *.test.ts.` |
| "You keep committing without asking." | `- Never commit or push unless the user asks in this session.` |
| "The API returns Arabic text, check RTL." | `- Check every new UI screen in RTL (dir="rtl") before calling it done.` |

## Not worth saving

- "Call this function `getUser` instead." — one-time naming choice.
- "Fix the typo on line 12." — task detail.
- "That's wrong." — no rule yet; ask what the right behaviour is first.

## Bad vs good wording

| Bad | Why | Good |
| --- | --- | --- |
| `- Be careful with the database.` | Can't be checked | `- Run migrations with pnpm db:migrate; never edit schema.sql by hand.` |
| `- Don't use npm!!!` | No alternative, no reason | `- Use pnpm, not npm — the lockfile is pnpm-lock.yaml.` |
| `- Follow best practices for tests.` | Vague | `- Every bug fix gets a failing test first.` |

## Handling a conflict

Existing: `- Use Jest for tests.`
New correction: "We moved to Vitest."

> `AGENTS.md` says **Use Jest for tests**, but you just said the project uses Vitest. Should I replace the line with `- Use Vitest for tests (migrated from Jest); run with pnpm test.`?
