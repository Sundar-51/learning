#!/bin/bash

# Exit if any command fails
set -e

# Create virtual environment
python -m venv myenv

# Activate the virtual environment
source myenv/Scripts/activate

# Confirm activation
echo "✅ Virtual environment 'myenv' activated."
python --version
