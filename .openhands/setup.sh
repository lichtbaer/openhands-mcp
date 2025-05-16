#!/bin/bash
set -e

# Install production dependencies
pip install -r requirements.txt

# Install dev dependencies (optional, for Entwicklung und Tests)
pip install -r requirements-dev.txt
