#!/usr/bin/bash

set -e 

LIB_DIR="lib"
REPO_NAME="Translation-Library-Docs"
REPO_URL="https://github.com/payne1778/$REPO_NAME"
COMMIT="main"

# Adds the subtree of the Translation Library Docs repository. 
# Puts contents of the docs repo into a new folder named with $REPO_NAME
git subtree add --prefix="$REPO_NAME/" "$REPO_URL" "$COMMIT" --squash

# Move files from the temp dir into the `lib` directory location.
# If the `lib` dir location doesn't exist, create it before adding files to it
if [ -d $LIB_DIR ]; then
    mv "$REPO_NAME/" "$LIB_DIR/"
else
    mkdir "$LIB_DIR/"
    mv $REPO_NAME/* "$LIB_DIR/"
fi