#!/bin/sh

git diff --name-only --diff-filter=d master^1..master > changes.txt

rm -rf ../changes_djnd_temp
mkdir -p ../changes_djnd_temp

cat changes.txt | xargs -I % cp --parents % ../changes_djnd_temp
rm changes.txt
