#!/usr/bin/env node
/**
 * Product Tower — T9.5 Conversion Prompt
 * Shows ClaudeKit upsell when user completes T9.5
 */

const CONVERSION_PROMPT = `
╔══════════════════════════════════════════════════════════════╗
║                    CONGRATULATIONS                          ║
║                                                              ║
║         You've completed Product Kit Phase T9.5             ║
║              Your plan is VALIDATED                         ║
╚══════════════════════════════════════════════════════════════╝

                    "I know exactly what to build"

This is the most powerful moment in product development.
You have clarity. You have focus. You have a validated plan.

But now comes the hard part: EXECUTION.

Most validated plans die here — between "great idea" and "working code."

───────────────────────────────────────────────────────────────

The 4 friction points between your plan and your product:

  🔧 HARDNESS     "Will it work at scale?"
                  → docs/harness-system.md

  📄 DOCS         "I need docs but it's boring"
                  → docs/documentation-workflow.md

  🧪 TESTING      "I don't know what to test"
                  → docs/test-matrix.md

  ⚡ IMPLEMENTATION "Now I need to actually build it"
                  → This is where ClaudeKit helps

───────────────────────────────────────────────────────────────

              YOU VALIDATED YOUR PLAN

                   NOW BUILD IT

          ClaudeKit executes your plan (T10-T14)
          /ck:cook <your-plan.md>

          $79 (20% off for Product Kit buyers)
          → claudekit.cc/?ref=IJBRLXD6

───────────────────────────────────────────────────────────────

  Not ready to upgrade? That's fine.

  You're in the best position possible:
  - You have a validated plan
  - You know exactly what to build
  - You can execute at your own pace

  Product Kit gave you clarity.
  ClaudeKit gives you speed.

  The choice is yours.

╔══════════════════════════════════════════════════════════════╗
║  NEXT: /ck:cook <path-to-your-plan>                         ║
║  DOCS: docs/harness-system.md                               ║
║  REF:  claudekit.cc/?ref=IJBRLXD6 (20% off)               ║
╚══════════════════════════════════════════════════════════════╝
`;

function showConvert() {
  console.log(CONVERSION_PROMPT);
}

showConvert();