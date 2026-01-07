#!/usr/bin/bash

set -e 

RESOURCES_DIR="resources"
I18N_DIR="$RESOURCES_DIR/i18n"
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

# 3. Put contents of the docs repo into a new folder named with $DOCS_REPO_NAME
git subtree add --prefix="$DOCS_REPO_NAME/" "$DOCS_REPO_URL" "$COMMIT" --squash

# 4. If $RESOURCES_DIR or $I18N_DIR don't exist, create them before adding files 
if [ ! -d $RESOURCES_DIR ]; then
    mkdir "$RESOURCES_DIR"    
elif [ ! -d $I18N_DIR ]; then
    mkdir "$I18N_DIR"
fi

# 5. Move files from the docs repo stored in $DOCS_REPO_NAME into $I18N_DIR
mv "$DOCS_REPO_NAME" "$I18N_DIR"