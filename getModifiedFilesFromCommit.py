import subprocess

from pyfzf.pyfzf import FzfPrompt

fzf = FzfPrompt()


def get_git_commits():
    # Run the Git command to get the commit log
    git_log = subprocess.check_output(
        ["git", "log", "--oneline"], universal_newlines=True
    )

    # Split the result into lines (commits)
    return git_log.strip().split("\n")


def getModifiedFilesFromCommit():
    commits = get_git_commits()
    try:
        selected_commit = fzf.prompt(commits)
    except Exception:
        # fzf exits with non-zero code when cancelled with Esc/Ctrl+C
        return []
    if not selected_commit:
        return []
    commit_hash = selected_commit[0].split(" ")[0]
    # -M reports renamed files under their new path,
    # --root makes the initial commit work too
    files = subprocess.check_output(
        [
            "git",
            "diff-tree",
            "--no-commit-id",
            "--name-only",
            "-r",
            "-M",
            "--root",
            commit_hash,
        ],
        universal_newlines=True,
    )
    return files.splitlines()
