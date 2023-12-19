#!/bin/bash

# Navigate to the assets directory
cd assets

# Generate a list of filenames and save them to a text file
find . -type f \( -name "*.jpg" -o -name "*.png" -o -name "*.gif" \) -exec basename {} \; > image_list.txt

# Move the text file back to the folio2 directory
mv image_list.txt ../
