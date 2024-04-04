#!/bin/bash

# Check if a folder argument is provided
if [ $# -ne 1 ]; then
    echo "Usage: $0 <folder_path>"
    exit 1
fi

# Navigate to the folder containing CUDA source files
cd "$1" || exit

# Compile each CUDA source file into an executable with the same name
for file in *.cu; do
    # Extract filename without extension
    filename=$(basename -- "$file")
    filename="${filename%.*}"

    # Compile the CUDA source file into an executable
    nvcc -o "$filename" "$file"
done