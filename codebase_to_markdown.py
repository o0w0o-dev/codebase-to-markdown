import os
import subprocess
import sys
import argparse
from mimetypes import guess_type

# Mapping of file extensions to programming languages
EXTENSION_TO_LANGUAGE = {
    "py": "python",
    "js": "javascript",
    "java": "java",
    "c": "c",
    "cpp": "cpp",
    "cs": "csharp",
    "html": "html",
    "css": "css",
    "xml": "xml",
    "json": "json",
    "md": "markdown",
    "sh": "bash",
    "rb": "ruby",
    "go": "go",
    "php": "php",
    "rs": "rust",
    "ts": "typescript",
    "swift": "swift",
    "kt": "kotlin",
    "scala": "scala",
    "pl": "perl",
    "sql": "sql",
    "r": "r",
    "m": "matlab",
    "f": "fortran",
    "lua": "lua",
    "ps1": "powershell",
    "tex": "latex",
    "yaml": "yaml",
    "toml": "toml",
}


def get_all_files(include_untracked=False):
    """Get all files in the Git repository not ignored by .gitignore"""
    try:
        tracked_files = (
            subprocess.check_output(["git", "ls-files"]).decode().splitlines()
        )
        all_files = tracked_files
        if include_untracked:
            untracked_files = (
                subprocess.check_output(
                    ["git", "ls-files", "--others", "--exclude-standard"]
                )
                .decode()
                .splitlines()
            )
            all_files += untracked_files
        script_name = os.path.basename(sys.argv[0])
        all_files = sorted(set(all_files))
        all_files = [f for f in all_files if f not in ["repo_summary.md", script_name]]
        return all_files
    except subprocess.CalledProcessError:
        print(
            "Error: The current directory is not a Git repository or Git is not installed."
        )
        exit(1)


def get_language_from_extension(file_path):
    """Get the programming language based on the file extension"""
    ext = os.path.splitext(file_path)[1][
        1:
    ].lower()  # Extract the extension and convert to lowercase
    return EXTENSION_TO_LANGUAGE.get(
        ext, ""
    )  # Return an empty string if no mapping exists


def main(include_untracked):
    all_files = get_all_files(include_untracked)
    with open("repo_summary.md", "w", encoding="utf-8") as md_file:
        for file_path in all_files:
            depth = file_path.count("/")
            header = "#" * (depth + 1) + " " + file_path
            md_file.write(header + "\n\n")

            mime_type, _ = guess_type(file_path)
            if mime_type and mime_type.startswith("image/"):
                md_file.write(f"![{file_path}]({file_path})\n\n")
            else:
                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        content = f.read()
                    language = get_language_from_extension(file_path)
                    md_file.write(f"```{language}\n{content}\n```\n\n")
                except UnicodeDecodeError:
                    continue


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generate a Markdown summary of the repository."
    )
    parser.add_argument(
        "--include-untracked", action="store_true", help="Include untracked files."
    )
    args = parser.parse_args()
    main(args.include_untracked)
