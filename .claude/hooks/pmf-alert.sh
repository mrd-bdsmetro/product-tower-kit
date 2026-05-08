#!/bin/bash
# pmf-alert.sh - PostToolUse hook
# Alert when PMF score is set

INPUT=$(cat)
TOOL_NAME=$(echo "$INPUT" | jq -r '.tool_name // empty')

if [[ "$TOOL_NAME" == "bash" ]]; then
  COMMAND=$(echo "$INPUT" | jq -r '.tool_input.command // empty')
  
  if [[ "$COMMAND" == *"pmf"* ]]; then
    # Extract score from output
    OUTPUT=$(echo "$INPUT" | jq -r '.tool_output.stdout // empty')
    
    if [[ "$OUTPUT" == *"NO-GO"* ]] || [[ "$OUTPUT" == *"BLOCKED"* ]]; then
      echo '{
        "decision": "allow",
        "message": "🔴 PMF ALERT: Score below threshold. Consider:\n1. Pivot segment → T1\n2. Pivot persona → T4\n3. Re-interview users → AB4"
      }'
      exit 0
    fi
  fi
fi

echo '{"decision":"allow"}'
