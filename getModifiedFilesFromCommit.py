import subprocess

from git import Repo
from pyfzf.pyfzf import FzfPrompt

fzf = FzfPrompt()


def get_git_commits():
    # Run the Git command to get the commit log
    git_log = subprocess.check_output(
        ["git", "log", "--oneline"], universal_newlines=True
    )

    # Split the result into lines (commits)
    commits = git_log.strip().split("\n")

    return commits


def getModifiedFilesFromCommit():
    # all commits to array
    commits = get_git_commits()
    selected_commit = fzf.prompt(commits)
    commit_hash = selected_commit[0].split(" ")[0]
    # Get the repository path
    repositoryPath = subprocess.check_output(
        ["git", "rev-parse", "--show-toplevel"], universal_newlines=True
    ).strip()
    # # Create the repository object
    repo = Repo(repositoryPath)
    # # Get the commit object
    commit = repo.commit(commit_hash)
    # # Get the modified files
    modifiedFiles = commit.stats.files
    # # Print the modified files
    files = []
    for file in modifiedFiles:
        files.append(file)
    return files
