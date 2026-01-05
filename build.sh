#!/usr/bin/bash

set -e 

LIB_DIR="lib"
DOCS_REPO_NAME="Translation-Library-Docs"
DOCS_REPO_URL="https://github.com/payne1778/$DOCS_REPO_NAME"
COMMIT="main"

# 1. Set up virtual environment
python3 -m venv .venv
source .venv/bin/activate

# 2. Install dependencies
pip install pytest

# 3. Put contents of the docs repo into a new folder named with $DOCS_REPO_NAME
git subtree add --prefix="$DOCS_REPO_NAME/" "$DOCS_REPO_URL" "$COMMIT" --squash

# 4. If the $LIB_DIR doesn't exist, create it before adding files to it
if [ ! -d $LIB_DIR ]; then
    mkdir "$LIB_DIR"    
fi

# 5. Move files from the docs repo stored in $DOCS_REPO_NAME into $LIB_DIR
mv "$DOCS_REPO_NAME" "$LIB_DIR"