import subprocess


def getRepoRoot():
    return subprocess.check_output(
        ["git", "rev-parse", "--show-toplevel"], universal_newlines=True
    ).strip()


def getModifiedFiles():
    # Get the modified tracked files (staged and unstaged) relative to HEAD
    modified_files = subprocess.check_output(
        ["git", "diff", "--name-only", "HEAD"], universal_newlines=True
    )
    return modified_files.splitlines()
