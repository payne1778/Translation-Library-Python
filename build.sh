LOCATION='lib/'
PREFIX='--prefix=$LOCATION/'
REPO='https://github.com/payne1778/Translation-Library-Docs'
COMMIT='main'

# Adds the subtree of the Translation Library Docs repository
git subtree add $PREFIX "$REPO" "$COMMIT" --squash

# Removes the Translation Library Docs Repository's LICENSE and README.md
# These files are either redundant or not needed in the prefix location
rm lib/LICENSE
rm lib/README.md
