#!/usr/bin/bash

set -e 

LIB_DIR="lib"
DOCS_REPO_NAME="Translation-Library-Docs"
DOCS_REPO_URL="https://github.com/payne1778/$DOCS_REPO_NAME"
COMMIT="main"

# Puts contents of the docs repo into a new folder named with $DOCS_REPO_NAME
git subtree add --prefix="$DOCS_REPO_NAME/" "$DOCS_REPO_URL" "$COMMIT" --squash

# If the $LIB_DIR doesn't exist, create it before adding files to it
if [ ! -d $LIB_DIR ]; then
    mkdir "$LIB_DIR/"    
fi

# Move files from the docs repo stored in $DOCS_REPO_NAME into $LIB_DIR
mv "$DOCS_REPO_NAME" "$LIB_DIR"