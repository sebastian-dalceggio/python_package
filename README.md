# Python Package Blueprint

This repository provides a streamlined blueprint for developing new Python packages, emphasizing modern tooling and best practices. It leverages:

* **uv:** For efficient dependency management and Python version control.
* **mypy & ruff:** For robust static typing and code linting, ensuring code quality and consistency.
* **pre-commit:** To automate linting and formatting checks before each commit, maintaining a clean codebase.
* **python-semantic-release:** For automated versioning and release management based on semantic commit messages.
* **GitHub Actions:** For continuous integration, automated testing, version updates, and merging `main` into `dev`.

## Getting Started

Follow these steps to initialize your new Python package:

1.  **Initialize the Project:**

    ```bash
    uv init python_package
    ```

    Replace `python_package` with your desired package name.

2.  **Install pre-commit Hooks:**

    ```bash
    uv run pre-commit install
    ```

    This sets up pre-commit to run automatically before each commit.

3.  **Initialize `main` Branch and Push `README.md`:**

    ```bash
    git checkout -b main
    git add README.md
    git commit -m "Initial commit to main branch: Add README.md"
    git remote add origin <YOUR_GITHUB_REPOSITORY_URL>
    git push -u origin main
    ```

    Replace `<YOUR_GITHUB_REPOSITORY_URL>` with the URL of your GitHub repository.

4.  **Create a `dev` Branch:**

    ```bash
    git checkout -b dev
    ```

5.  **Commit Your Changes:**

    ```bash
    git add .
    git commit -m "feat: Initial commit of python_package blueprint"
    ```

    **Important:** Since you are using `python-semantic-release`, your commit messages should follow the [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) specification. This allows `python-semantic-release` to automatically determine the next version based on your commit history.

    * `feat`: Indicates a new feature (minor version bump).
    * `fix`: Indicates a bug fix (patch version bump).
    * `BREAKING CHANGE`: In the commit message footer, indicates a breaking change (major version bump).

    For the initial commit, `feat: Initial commit of python_package blueprint` is a suitable message.


6.  **Push to the `dev` Branch:**

    ```bash
    git push -u origin dev
    ```

    (This will create the `dev` branch on your remote repository if it doesn't already exist.)

7.  **Create a Pull Request:**

    * Go to your GitHub repository.
    * You should see a prompt to create a pull request from the `dev` branch to `main`.
    * Follow the instructions to create the pull request.

8.  **Add GitHub Token to Secrets:**

    * Your GitHub Actions workflow requires a GitHub token with specific permissions.
    * Go to your repository's "Settings" tab.
    * Click on "Secrets and variables" -> "Actions".
    * Click "New repository secret".
    * Name the secret `PAT_TOKEN` (or whatever name your workflow expects).
    * Paste your personal access token (PAT) into the "Value" field.
    * Click "Add secret".

    **Important:** Generate a PAT with the following permissions for your workflow:

    * **`contents: write`:** This permission is required for `python-semantic-release` to update the version number, create changelogs, and push commits.
    * **`actions: write`:** This permission is required if the semantic release action is also creating a github release.

    **Never** commit your PAT directly to your repository.

9.  **Approve the Pull Request and Verify Workflows:**

    * In your GitHub repository, navigate to the pull request you created.
    * Review the changes and approve the pull request.
    * Go to the "Actions" tab in your repository.
    * Verify that the GitHub Actions workflows are running successfully. If any fail, investigate and fix the issues.
