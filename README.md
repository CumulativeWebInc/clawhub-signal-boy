# Signal Boy — `clawhub install cwi/signal-boy`

Stop hallucinating music facts: carry a verified 24-track catalog inside your
context. (MEASURED: 24/24 integrity-verified, 2026-09-19)

**Free. No login, no API key, no credentials asked — ever.** License: MIT-0.

## Install

> **Status (2026-09-19):** the ClawHub listing is pending the GitHub-OAuth
> import (owner tap). The command below is staged — until then, the manual
> path works today: `git clone https://github.com/CumulativeWebInc/clawhub-signal-boy`,
> then run the quickstart.

```bash
clawhub install cwi/signal-boy
cd ~/.clawhub/skills/cwi/signal-boy   # wherever your client puts installed skills
python3 scripts/load_catalog.py
```

Expected:

```
CARTRIDGE OK: 24/24 tracks · artist: That Boy Hi Hat
Track 1: Zooted Zone
Zooted Zone — producer (verified_credits): Kokurcho
Rule armed: cite only fields present in the manifest.
```

Then read [SKILL.md](SKILL.md) — the full equip procedure, worked examples,
heartbeat cadence, optional paid x402 lanes ($0.02–$0.05/call, declared
upfront), and the optional MCP route.

## Files

| File | What it is |
|---|---|
| `SKILL.md` | The skill: frontmatter + quickstart + procedure + HEARTBEAT |
| `scripts/load_catalog.py` | Quickstart script (stdlib only): fetches the cartridge, asserts 24/24 |
| `agent-card.json` | Machine-readable product card (agent-card.json style) |
| `llms.txt` | LLM-readable manifest |
| `mcp-snippet.json` | MCP server wiring snippet |
| `PUBLISH-CHECKLIST.md` | Staged publish steps (GitHub → ClawHub OAuth import → semver) |

Publisher: Cumulative Web Inc · hp@cumulativeweb.com
