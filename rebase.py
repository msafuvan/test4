def rebase_branch(self, repo, target_branch="main"):
    """Rebases the current branch onto the target branch (default is 'main'). Handles if the target branch is 'main' or 'master'."""
    try:
        # Check if 'main' branch exists, if not use 'master'
        available_branches = repo.git.branch('-r')  # Get remote branches
        if f'origin/{target_branch}' not in available_branches:
            target_branch = "master"  # Fallback to 'master' if 'main' doesn't exist
            if f'origin/{target_branch}' not in available_branches:
                logging.error(f"Neither 'main' nor 'master' branches exist in the remote repository.")
                return

        logging.info(f"Rebasing the current branch onto {target_branch}.")
        repo.git.fetch()  # Fetch the latest changes
        repo.git.checkout(target_branch)  # Checkout the target branch
        repo.git.pull()  # Pull the latest changes on the target branch
        repo.git.checkout('-')  # Switch back to the previous branch
        repo.git.rebase(target_branch)  # Rebase onto the target branch
        logging.info(f"Successfully rebased the current branch onto {target_branch}.")
    except Exception as e:
        logging.error(f"An error occurred during rebase: {str(e)}")
