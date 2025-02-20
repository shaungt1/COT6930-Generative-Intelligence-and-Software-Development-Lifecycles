#!/bin/bash

# Define the output file
OUTPUT_FILE="requirements.txt"
TEMP_FILE="temp_requirements.txt"

# Clear the output file if it exists
> "$OUTPUT_FILE"

# Find all directories that do not contain a dot and are not named "GENAIENV"
find . -type d ! -name "GENAIENV" ! -name "*.*" | while read -r dir; do
    # Find requirement files in those directories
    find "$dir" -type f -regex ".*/[^/]*_requirements\.txt\|.*/requirements\.txt\|.*/[^/]*_requirements\.txtx" | while read -r req_file; do
        cat "$req_file" >> "$TEMP_FILE"
    done
done

# Remove duplicates and create the final requirements file
if [[ -f "$TEMP_FILE" ]]; then
    sort -u "$TEMP_FILE" > "$OUTPUT_FILE"
    rm "$TEMP_FILE"
    echo "Merged all found requirement files into $OUTPUT_FILE."
else
    echo "No requirement files found."
fi
