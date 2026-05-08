#!/bin/bash
# tier-progress.sh - SessionStart hook
# Show current tier progress on session start

PROJECT_DIR="$(pwd)"
STATE_FILE="$PROJECT_DIR/pipeline_state.json"

if [ -f "$STATE_FILE" ]; then
  COMPLETED=$(jq -r '.tiers_completed | keys[]' "$STATE_FILE" 2>/dev/null | tr '\n' ' ')
  PMF_RAW=$(jq -r '.pmf.raw // "not scored"' "$STATE_FILE" 2>/dev/null)
  PMF_ADJ=$(jq -r '.pmf.adjusted // "not scored"' "$STATE_FILE" 2>/dev/null)
  
  echo "📊 Product Tower Status"
  echo "Completed: $COMPLETED"
  echo "PMF: $PMF_RAW (adjusted: $PMF_ADJ)"
  echo ""
  echo "Next: Run /pt:status for details"
fi
