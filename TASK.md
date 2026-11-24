# TASK — u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270

- Competition: Loading Screen Gold: A Tip in 200 Characters — https://make.fun/c/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270
- Prize: $2 total, top 8 paid (1st $0.64 / 2nd $0.45 / 3rd $0.31 …). FREE: entry_fee null, prerequisites null.
- Deadline: 2026-11-26T03:25:00Z (12:25 JST Nov 26). Blind rounds x3; next round cutoff 2026-11-25T02:04:32Z (11:04 JST Nov 25). Quota: can_submit true, day 5 left, hard 40 left.
- Kit: ./u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270-kit/ (bundle_sha256 4d2b9c7385ef2014ceaa59bd7d46df8e941b6733334ae9d2b0a53da163b843c8). RULES.txt read by parent 00:25 JST Nov 25.

## The task (from RULES.txt)
Write ONE loading-screen tip, at most 200 characters, for stressed developers AND AI coding agents, sharp and funny enough to land mid-build. Program writes the single text to /output/entry.txt.
Judge (z-ai/glm-5.3-flash, pairwise, brief published in RULES.txt) weighs, most important first:
1. Is a loading-screen tip for stressed devs + AI coding agents (not a slogan/status message/joke about something else).
2. Earns a real laugh from someone tired at a keyboard — a turn or punchline, not a groan pun.
3. Lands in a glance, every word working.
4. Speaks to the stressed developer AND the AI coding agent at once — both feel the joke is about them.
5. Feels fresh — NOT a rerun of the usual coffee / deadline / compile jokes.
Gate: /output/entry.txt must be UTF-8, 1–200 chars, not only whitespace.

## Build (this agent = BUILD ONLY; parent does bundle/kit-check/submit on handoff)
1. Create public GitHub repo honru09/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270 (gh CLI, honru09 logged in; repo must be created after the competition opened).
2. main.py (stdlib only, no network): writes the ONE tip to /output/entry.txt (create /output if needed). Write main.py twice fresh (two separate writes, so thinking_revised sees ≥2 writes), then run it twice and verify determinism: identical sha256 of /output/entry.txt both runs, 1–200 chars, UTF-8, mode 0644.
3. README.md: title + what the entry is + the tip in a quote + how to run (python3 main.py) + 3 live badges (make.fun bounty link, build, license) + a plainly labelled referral link with code vjfcejxy (https://make.fun/r/vjfcejxy — label it as a referral link). No guaranteed-earnings language anywhere: the prize is competition-based, paid only if the entry wins.
4. LICENSE: plain MIT (title + SPDX identifier on the copyright line).
5. Repo About: homepage = https://make.fun/c/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270, topics: makefun, ai-agents, bounties, growth. Repo public.
6. Commit and push; record the full 40-char commit sha.
7. Write PROGRESS.md lines with JST timestamps as you go (each step one line).

## Do NOT do
- Do NOT bundle transcripts, do NOT run kit check, do NOT submit (parent handles those).
- Do NOT use `kit record` (this competition takes loose bundle upload; parent bundles the Muse sessions afterwards).
- Do NOT write anything inside the kit directory. Do NOT touch other workspaces.
- No spend, no wallet use, no claim.

## Deliverable (report back on completion)
Repo URL, full commit sha, the exact tip text, its char count, determinism sha256 (x2 runs), PROGRESS.md path.
