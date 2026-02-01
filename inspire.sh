#!/bin/bash

echo "💡 ShipOrKill: Idea Generator"
echo "----------------------------------------"
echo "Stuck? Let's find a problem to solve."
echo "Enter a domain (e.g., 'Healthcare', 'Construction', 'Finance') or hit Enter for random:"
read -p "> " DOMAIN

if [ -z "$DOMAIN" ]; then
  PROMPT="Generate 5 varied startup ideas."
else
  PROMPT="Generate 5 startup ideas specifically for the $DOMAIN industry."
fi

echo ""
echo "🧠 Brainstorming un-obvious ideas for you..."
echo "----------------------------------------"

gemini -c ideator.md "${PROMPT}"