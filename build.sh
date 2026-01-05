#!/usr/bin/bash

set -e 

# Initalize "global" variables
PERM_DIR='lib'
TEMP_DIR='temp-build-script-dir'
REPO='https://github.com/payne1778/Translation-Library-Docs'
COMMIT='main'

# Adds the subtree of the Translation Library Docs repository
git subtree add --prefix="$TEMP_DIR/" "$REPO" "$COMMIT" --squash

# Move files from the temp dir into the permenant dir location.
# If the permenant dir location doesn't exist, create it before adding files
if [ -d $PERM_DIR ]; then
    mv $TEMP_DIR/* "$PERM_DIR/"
else
    mkdir "$PERM_DIR/"
    mv $TEMP_DIR/* "$PERM_DIR/"
fi

rm -rf "$TEMP_DIR"
