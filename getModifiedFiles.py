from py_libs.Command import Command


def getRepoRoot():
    return Command.run_quiet("git rev-parse --show-toplevel")


def getModifiedFiles():
    # Get the modified tracked files (staged and unstaged) relative to HEAD
    return Command.run_quiet("git diff --name-only HEAD").splitlines()
