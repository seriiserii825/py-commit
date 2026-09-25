from py_libs.Command import Command
from py_libs.Select import Select


def get_git_commits():
    # Get the commit log, one commit per line
    return Command.run_quiet("git log --oneline").splitlines()


def getModifiedFilesFromCommit():
    selected_commit = Select.select_fzf_one(get_git_commits())
    # None when fzf is cancelled with Esc/Ctrl+C
    if not selected_commit:
        return []
    commit_hash = selected_commit.split(" ")[0]
    # -M reports renamed files under their new path,
    # --root makes the initial commit work too
    cmd = Command.build(
        "git diff-tree --no-commit-id --name-only -r -M --root", commit_hash
    )
    return Command.run_quiet(cmd).splitlines()
