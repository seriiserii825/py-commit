import os
from getModifiedFiles import getModifiedFiles
from getModifiedFilesFromCommit import getModifiedFilesFromCommit


help = """
Usage: $0 OPTIONS

This script opens changed files from git into neovim.

OPTIONS:
   -s      Open currently modified tracked files
   -l      Open changed files from a commit
"""

choice = input("What would you like to do, open modified or form a commit? (s/l): ")
# check for valid choice

if choice == 's':
    modified_files = getModifiedFiles()
    print(f"modified_files: {modified_files}")
    # nvim open files
    os.system(f"nvim {' '.join(modified_files)}")
elif choice == 'l':
    modified_files = getModifiedFilesFromCommit()
    print(f"modified_files: {modified_files}")
    # nvim open files
    os.system(f"nvim {' '.join(modified_files)}")
else:
    print(help)
    exit(1)
