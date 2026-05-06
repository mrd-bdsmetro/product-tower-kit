#!/bin/bash
# gate-check.sh — PreToolUse hook
# Auto gate enforcement before writing to data/t*.md

INPUT=$(cat)
FILE=$(echo "$INPUT" | jq -r '.tool_input.file_path // empty')

if [[ "$FILE" == *"/data/t"*".md" ]]; then
  # Extract tier from filename
  TIER=$(basename "$FILE" | grep -oP 't\d+' | head -1)
  
  # Check pipeline state
  STATE_FILE="$(dirname "$FILE")/../pipeline_state.json"
  
  if [ -f "$STATE_FILE" ]; then
    COMPLETED=$(jq -r '.tiers_completed | keys[]' "$STATE_FILE" 2>/dev/null)
    
    # Simple gate check
    case "$TIER" in
      t1)
        if ! echo "$COMPLETED" | grep -q "T0"; then
          echo '{"decision":"block","reason":"🛑 GATE BLOCK: T0 must be complete before T1"}'
          exit 0
        fi
        ;;
      t7)
        # Check anti-bias
        AB_STATUS=$(jq -r '.anti_bias | to_entries[] | select(.value.status=="completed") | .key' "$STATE_FILE" 2>/dev/null)
        AB_COUNT=$(echo "$AB_STATUS" | grep -c "AB")
        if [ "$AB_COUNT" -lt 4 ]; then
          echo '{"decision":"block","reason":"🛑 GATE BLOCK: AB1-AB4 must be complete before T7 PMF"}'
          exit 0
        fi
        ;;
    esac
  fi
fi

echo '{"decision":"allow"}'
