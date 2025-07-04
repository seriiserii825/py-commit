import subprocess


def getModifiedFiles():
    # Get the modified files in the current branch
    modified_files = subprocess.check_output(['git', 'diff', '--name-only', 'HEAD'])
    #remove b'' from the output
    modified_files = modified_files.decode('utf-8')
    return modified_files.splitlines()
