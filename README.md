# codebase-to-markdown

## Script Usage Guide

This Python script generates a Markdown file (`repo_summary.md`) that lists all files in a Git repository (with an option to include or exclude untracked files), their relative paths, and either their content (for text files) or a reference (for image files). It automatically assigns the appropriate programming language identifier to code blocks based on file extensions.

### Features

- **Automatic File Listing**: Retrieves a list of files from the Git repository (optionally including untracked files).
- **File Exclusion**: Automatically excludes the script itself and the generated `repo_summary.md`.
- **File Type Handling**:
  - **Text Files**: Assigns a programming language based on the file extension and generates a code block.
  - **Image Files**: Embeds an image reference using a relative path.
  - **Non-Text Files**: Skips processing.
- **Header Levels**: Sets Markdown header levels based on the file path depth (e.g., `#` for root files, `##` for files in subdirectories, etc.).

### Prerequisites

- **Git**: The script relies on Git to fetch the file list and must be run within a Git repository.
- **Python**: Written for Python 3.x.

### Installation and Execution

1. **Save the Script**: Save the script code as a `.py` file, e.g., `generate_md.py`.
2. **Run the Script**: Open a terminal in the root directory of your Git repository and execute one of the following commands:

   - **Default Execution (Tracked Files Only)**:
     ```bash
     python generate_md.py
     ```
   - **Include Untracked Files**:
     ```bash
     python generate_md.py --include-untracked
     ```

3. **Check Output**: After running, the script generates a `repo_summary.md` file in the current directory.

### Command-Line Arguments

- `--include-untracked`: Optional flag, defaults to `False`. When set, includes untracked files (not ignored by `.gitignore`) in the summary.
