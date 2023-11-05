import os
import configparser
import subprocess

def find_git_repositories(start_path='/'):
    git_repositories = []

    for dirpath, dirnames, filenames in os.walk(start_path):
        if '.git' in dirnames:
            git_repositories.append(os.path.abspath(os.path.join(dirpath)))

    return git_repositories


def is_directory_committed(directory_path):
    # Run "git status" to check the status of the directory
    cmd = ["git", "status", "--porcelain", "--", directory_path]
    result = subprocess.run(cmd, stdout=subprocess.PIPE, text=True)

    print(result)
    # Check the output to determine if the directory is committed or not
    if result.returncode == 0:
        status_output = result.stdout.strip()
        if status_output == "":
            return "The directory is clean and has no uncommitted changes."
        else:
            return "The directory has uncommitted changes."
    else:
        return "Error: Git command failed."



if __name__ == "__main__":
    git_directories = find_git_repositories('/Users/snathani')
    if git_directories:
        print("Git repositories found:")
        for git_directory in git_directories:
            # print(git_directory)
            gitconfig_path = os.path.expanduser(git_directory + "/.git/config")
            config = configparser.ConfigParser()
            config.read(gitconfig_path)

            # print(config.sections())
            # Access and print a specific configuration value

            url = config.get("remote \"origin\"", "url")
            if "surajn222" in url:
                print(git_directory)
                result = is_directory_committed(git_directory)


    else:
        print("No Git repositories found.")


