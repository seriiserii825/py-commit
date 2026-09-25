import argparse
import os
import subprocess
import sys

from getModifiedFiles import getModifiedFiles, getRepoRoot
from getModifiedFilesFromCommit import getModifiedFilesFromCommit

parser = argparse.ArgumentParser(
    description="Open changed files from git into neovim.",
)
group = parser.add_mutually_exclusive_group()
group.add_argument(
    "-s", action="store_true", help="Open currently modified tracked files"
)
group.add_argument("-l", action="store_true", help="Open changed files from a commit")
args = parser.parse_args()

if args.s:
    choice = "s"
elif args.l:
    choice = "l"
else:
    choice = input(
        "What would you like to do, open modified or from a commit? (s/l): "
    ).strip()

try:
    repo_root = getRepoRoot()
    if choice == "s":
        modified_files = getModifiedFiles()
    elif choice == "l":
        modified_files = getModifiedFilesFromCommit()
    else:
        parser.print_help()
        sys.exit(1)
except RuntimeError as err:
    # git failed (e.g. not a git repository)
    print(err, file=sys.stderr)
    sys.exit(1)

# git returns paths relative to the repo root, so make them absolute
# to work from any subdirectory; skip files deleted since then
existing_files = []
for file in modified_files:
    path = os.path.join(repo_root, file)
    if os.path.isfile(path):
        existing_files.append(path)
    else:
        print(f"skipped (not found): {file}")

if not existing_files:
    print("No files to open")
    sys.exit(0)

print(f"modified_files: {existing_files}")
# nvim open files
subprocess.run(["nvim", *existing_files])
