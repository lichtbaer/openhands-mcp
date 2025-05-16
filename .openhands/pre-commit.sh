#!/bin/bash

# Ruff: Linting und Style-Checks
ruff .
RUFF_STATUS=$?

# Bandit: Security-Checks
bandit -r app microagents
BANDIT_STATUS=$?

if [ $RUFF_STATUS -ne 0 ] || [ $BANDIT_STATUS -ne 0 ]; then
  echo "\nPre-commit: Fehler gefunden! Commit abgebrochen."
  exit 1
fi

echo "Pre-commit: Alle Checks bestanden. Commit kann durchgeführt werden."
exit 0
