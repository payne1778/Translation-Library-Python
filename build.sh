#!/usr/bin/bash

set -e 

RESOURCES_DIR="resources"
DOCS_REPO_NAME="Translation-Library-Docs"
DOCS_REPO_URL="https://github.com/payne1778/$DOCS_REPO_NAME"
COMMIT="main"

# 1. Set up virtual environment
python3 -m venv .venv
source .venv/bin/activate

# TODO: move dependencies installation to future pyproject.toml
# 2. Install dependencies
pip install pytest > /dev/null
pip install tomlkit > /dev/null
pip install glom > /dev/null
pip install pydantic > /dev/null

# 3. If $RESOURCES_DIR doesn't exist, create it before adding files 
if [ ! -d $RESOURCES_DIR ]; then
    mkdir "$RESOURCES_DIR"    
fi

# 4. Put contents of the docs repo into a new folder named with $DOCS_REPO_NAME
git subtree add --prefix="$RESOURCES_DIR/" "$DOCS_REPO_URL" "$COMMIT" --squash