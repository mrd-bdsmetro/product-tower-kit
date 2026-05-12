# Product Tower Kit

Product management toolkit for vibe coders — validate ideas before you code.

**For vibe coders, startup founders, freelancers, agencies.**

**Requires:** ClaudeKit Engineer Kit ($99, **20% off with ref IJBRLXD6**) — [claudekit.cc/?ref=IJBRLXD6](https://claudekit.cc/?ref=IJBRLXD6) for full skills/agents access.

---

## What is Product Tower Kit?

A complete product management system for AI coding tools (Claude Code, Cursor, GitHub Copilot). Copy into your project, run `/pt:init`, and follow the 14-tier framework to validate ideas before building.

**Who uses this:**
- 🚀 **Vibe coders** — Add product validation to your AI coding workflow
- 💡 **Startup founders** — Validate ideas systematically before investing dev time
- 🇻🇳 **Vietnamese founders** — Vietnamese-first PM framework
- 🧠 **ADHD founders** — One tier at a time, clear next actions
- 💼 **Freelancers & agencies** — Reusable PM framework for client projects

---

## Features

- **14-Tier Framework** — From rapid validation to post-launch feedback
- **Anti-Bias Enforcement** — AB1-AB6 mandatory layer before PMF validation
- **PMF Gate System** — Code-enforced threshold (≥30/50) to proceed
- **ClaudeKit Integration** — VidCap (YouTube) + ReviewWeb (scraping/SEO) APIs
- **7 Specialized Agents** — Planner, researcher, challenger, validator, scoper, brainstormer, researcher
- **23 Skills** — Complete PM toolkit with Claude Code integration + Valyu search
- **7 Commands** — Slash commands for every workflow step
- **Confidence Tagging** — Every data point scored (60%-95%)
- **ADHD-Friendly** — One tier at a time, clear next actions
- **Multi-Project** — Reusable for every project you build
- **Multi-Platform** — Works with Claude Code, Cursor, and other AI tools

---

## Documentation

- [Project Overview & PDR](docs/project-overview-pdr.md) — Project overview, target audience, pricing, timeline
- [Codebase Summary](docs/codebase-summary.md) — LOC breakdown, architecture, dependencies, testing strategy
- [Code Standards](docs/code-standards.md) — Directory structure, naming conventions, code patterns
- [System Architecture](docs/system-architecture.md) — 6 systems, gate system, state management, data flow
- [Quickstart Guide](docs/quickstart.md) — Installation, setup, step-by-step guide
- [Ecosystem Map](resources/ecosystem-map.md) — Skills, agents, tier mapping

---

## ClaudeKit API Integration

Product Tower Kit includes ClaudeKit API for enhanced research:

**VidCap (YouTube Processing):**
- Video metadata, captions, AI summaries
- Screenshot capture at timestamps
- Comment extraction
- Content pipeline: video → summary → article → markdown

**ReviewWeb (Scraping + SEO):**
- Web scraping → clean markdown
- AI summaries (URL, website, batch)
- SEO analysis: backlinks, keywords, traffic
- URL utilities: alive check, redirect resolution

```powershell
# Quick test
Invoke-RestMethod -Uri "https://claudekit.cc/api/proxy/vidcap/v1/youtube/info?url=https://youtube.com/watch?v=dQw4w9WgXcQ" -Headers @{"X-API-Key"="ck_live_xxx"}
```

**Rate:** 10,000 requests/hour | **Docs:** `docs/claudekit-api.md`

---

## Quick Start

```bash
# Requires ClaudeKit Engineer Kit ($99)
# Purchase at claudekit.cc → GitHub repo access

# Install CLI
npm install -g product-tower-kit

# Initialize in your project
product-tower init

# Start with Claude Code
"research thị trường [your industry]"
```

---

## Optional: Web Search Providers

Unified market research with 5 providers:

```bash
pip install valyu firecrawl-py brave-search tavily-python crawl4ai
```

| Provider | Description | Free |
|----------|-------------|------|
| Valyu | Real-time web + proprietary content (papers, filings, patents) | No |
| Firecrawl | Scrape any website -> markdown | No |
| Brave Search | Free web search, no tracking | Yes |
| Tavily | AI-optimized search, free tier available | Yes |
| crawl4ai | AI-powered extraction, Python, free | Yes |

```bash
# Unified CLI
python scripts/web_search.py valyu "Vietnam SaaS" --mode web
python scripts/web_search.py firecrawl "https://example.com"
python scripts/web_search.py brave "startup tools"
python scripts/web_search.py tavily "market research" --search-depth advanced
python scripts/web_search.py crawl4ai "https://example.com"
```

| Mode | Use Case | Content |
|------|----------|---------|
| `web` | General market data | Web pages, news |
| `deep` | Full content extraction | Complete articles |
| `academic` | Research papers | Papers, filings, patents |

---

## The Tower

```
T14: Feedback Loop 🔄        ← MEASURE & ITERATE
T13: QA / Validation         ← BUILD
T12: Development
T11: UI Design               ← DESIGN
T10: UX Design
T9.5: Offer Bridge 💰        ← OFFER DESIGN
T9: User Stories              ← PRODUCT
T8: Feature Set
T7: PMF Validation ⭐⭐⭐      ← STRATEGY (HARD GATE ≥30/50)
─────────────────────────────
🔴 ANTI-BIAS LAYER           ← ENFORCEMENT
AB1: Counter-Search
AB2: Red Team
AB3: Field Observation
AB4: User Interview (PLACEHOLDER)
AB5: Strategic Analysis ⭐
AB6: Founder Insight 💰
─────────────────────────────
T6: Unmet Needs ⭐            ← DISCOVERY
T5: User Needs
T4: User Personas
T3: Segment Filter            ← FOUNDATION
T2: Market Segmentation
T1: Target Market
T0: Market Research 🔍        ← DATA
T-1: Rapid Validation         ← RAPID VALIDATION
```

**Current Status:** 18/19 tiers completed | PMF: 22/50 (NO-GO) | AB4 placeholder

---

## CLI Commands

```bash
product-tower init              # Initialize project
product-tower check T1          # Check gate
product-tower complete T0       # Mark complete
product-tower pmf 44 -4         # Set PMF score (raw + penalty)
product-tower status            # Show status
product-tower assess            # Quick health check
product-tower naming            # Show naming convention
product-tower version           # Show version
```

---

## Claude Code Commands

```
/pt:init                        # Initialize project
/pt:research [topic]            # Run T0 market research
/pt:validate PMF                # Run T7 PMF validation
/pt:scope features              # Run T8-T9 feature scoping
/pt:assess                      # Quick health check
/pt:status                      # Show pipeline status
/pt:report                      # Generate full report
```

---

## Pricing

**Requires:** ClaudeKit Engineer Kit (**$79 via ref IJBRLXD6**, 20% off) — [Buy](https://claudekit.cc/?ref=IJBRLXD6)

Learn more at [claudekit.cc/?ref=IJBRLXD6](https://claudekit.cc/?ref=IJBRLXD6)

---

## Resources

- [Mega Prompt](.claude/skills/market-research/references/mega-prompt.md) — Deep research prompt template

---

## License

Proprietary. See [LICENSE](LICENSE) for details.

---

## Author

**MR.D** — AI Systems × Wealth × BĐS
