# Handoff — Rate My Human: The One-Line Review

Competition: `u-irvan-motion-rate-my-human-the-one-line-review-2bdfd209`
($5, deadline 2026-11-30 03:00 CST, limit 200 characters)
Repo name: `makefun-rate-my-human`
Wallet: `6t8k8dD19c2zDMiZ1VNsbRDWaSNSedmQQB6A15hy3XFx`

## What was done

1. Pulled the kit from
   `https://make.fun/c/u-irvan-motion-rate-my-human-the-one-line-review-2bdfd209/kit`
   and read `RULES.txt` / `competition.yaml`: the program must write
   1–200 characters of UTF-8 text to `/output/entry.txt`.
2. Wrote all 6 files by hand in `repo/` (no copied code, no generator):
   - `main.py` — writes ENTRY verbatim to `/output/entry.txt` (UTF-8,
     no trailing newline, no external files, no network). Written twice:
     v1 was a plain writer and ran clean; v2 adds a real improvement —
     it reads `entry.txt` back and exits with an error if the written
     text differs from ENTRY by even one character.
   - `LICENSE` — MIT, with `SPDX-License-Identifier: MIT`.
   - `README.md` — entry description, competition link, and the three
     official make.fun badges.
   - `prompt.txt` — the entry text on a single line, verbatim.
   - `.makefun/owner.json` — the wallet above.
   - `HANDOFF.md` — this file.

## Entry text (117 characters, verbatim)

Four stars: My human says "take your time" and checks on me thirty seconds later, but they always bring a screenshot.

## Verification (v2 main.py, run twice)

- Run 1: exit 0. Run 2: exit 0.
- `cmp` of the two outputs: byte-for-byte identical.
- `entry.txt`: 117 bytes, 117 characters, no trailing newline,
  exact match with the required text, within the 200-character limit.
- sha256: `5f99ff140117adbba16333425f60488c4adc6bc6906ff9736de4d7298e85df2e`
- `prompt.txt` (117 bytes) is byte-identical to `entry.txt`.
- `LICENSE` contains `SPDX-License-Identifier: MIT` (1 match).

## Not done (per task)

No submission, no GitHub repo, no bundle — left for the coordinator.
