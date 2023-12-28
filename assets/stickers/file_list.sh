#!/bin/bash

# Get the name of the current directory
current_directory=$(basename "$PWD")

# Generate a list of filenames and save them to a .txt file named after the directory
find . -type f \( -name "*.jpg" -o -name "*.png" -o -name "*.gif" \) -exec basename {} \; > "${current_directory}.txt"

# The .txt file with the directory name will be in the current directory
