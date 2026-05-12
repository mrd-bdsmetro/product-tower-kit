# Changelog

## [1.4.0] - 2026-05-06

### Added (from claudekit-marketing)
- **launch-strategy skill** — ORB Framework, 5-phase launch, Product Hunt strategy
- **marketing-ideas skill** — 140+ proven marketing ideas (Content, PLG, Social, Email, Partnerships, PR)
- **marketing-psychology skill** — 70+ mental models (persuasion, pricing, UX, growth)
- **competitor-alternatives skill** — Comparison page templates for SEO and sales
- **free-tool-strategy skill** — Engineering-as-marketing for lead generation
- **onboarding-cro skill** — User onboarding and activation optimization

### Skills count: 17 → 23

## [1.3.0] - 2026-05-06

### Added
- **Valyu Search Integration** — Enhanced market research with real-time web + proprietary content
- `scripts/valyu_search.py` — Python CLI for Valyu API (web, deep, academic modes)
- Updated `market-research` skill with Valyu mode (v1.2.0)
- README updated with Valyu setup instructions

### Valyu Modes
- `web` — General market data (fast)
- `deep` — Full content extraction (medium)
- `academic` — Research papers, filings, patents (slow)

## [1.2.0] - 2026-05-06

### Added (from claudekit-engineer)
- **brainstorm skill** — Product brainstorming with trade-off analysis and anti-rationalization
- **research skill** — Market research methodology with confidence scoring
- **problem-solving skill** — Systematic approaches for PMF pivot and stuck situations
- **retro skill** — Sprint retrospectives for T14 feedback loop
- **sequential-thinking skill** — Structured problem-solving for complex product decisions
- **brainstormer agent** — CTO-level advisor for product decisions
- **researcher agent** (enhanced) — Technical analyst with saturation check

### Patterns adopted from claudekit
- Anti-Rationalization table (from brainstorm)
- Quick Dispatch table (from problem-solving)
- Confidence scoring system (from research)
- Saturation check (from research)
- 5 Whys, 80/20 Rule, Inversion Exercise (from problem-solving)

## [1.1.0] - 2026-05-06

### Changed
- **Broader market positioning** — Now targeting vibe coders, startup founders, freelancers, agencies (not just Vietnamese solo founders)
- **Updated target audience** — 8M+ potential users (was 50K)
- **Updated market size** — $645K-1.3M revenue potential (was $495)
- **Updated PMF guidance** — Better handling for new products (0 users)
- **Updated README** — Broader market positioning
- **Updated docs** — project-overview-pdr.md with market size analysis
- **Updated skills** — product-tower, market-research, pmf-validator
- **Updated ecosystem-map** — Added target audiences
- **Updated product-plan template** — Added target audience field

### Added
- **Multi-platform support** — Works with Claude Code, Cursor, and other AI tools
- **Reusable framework** — Use for every project you build
- **Market size analysis** — Detailed TAM/SAM/SOM for all segments

## [1.0.0] - 2026-05-06

### Added
- Initial release
- 14-tier Product Tower framework
- 12 SKILL.md files for Claude Code
- 5 agent definitions
- 7 slash commands
- 3 automation hooks
- Python CLI (gate_checker.py)
- Gate enforcement system
- Anti-Bias layer (AB1-AB6)
- PMF scoring with penalty system
- Confidence tagging system
- Templates and documentation
- Mega Prompt for Deep Research
