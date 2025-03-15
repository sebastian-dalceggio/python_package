# Python Package Blueprint

This repository provides a streamlined blueprint for developing new Python packages, emphasizing modern tooling and best practices. It leverages:

* **uv:** For efficient dependency management and Python version control.
* **mypy & ruff:** For robust static typing and code linting, ensuring code quality and consistency.
* **pre-commit:** To automate linting and formatting checks before each commit, maintaining a clean codebase.
* **GitHub Actions:** For continuous integration, automated testing, version updates.

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
    git commit -m "Initial commit of python_package blueprint"
    ```


6.  **Push to the `dev` Branch:**

    ```bash
    git push -u origin dev
    ```

    (This will create the `dev` branch on your remote repository if it doesn't already exist.)

7.  **Create a Pull Request:**

    * Go to your GitHub repository.
    * You should see a prompt to create a pull request from the `dev` branch to `main`.
    * Follow the instructions to create the pull request.

8.  **Approve the Pull Request and Verify Workflows:**

    * In your GitHub repository, navigate to the pull request you created.
    * Review the changes and approve the pull request.
    * Go to the "Actions" tab in your repository.
    * Verify that the GitHub Actions workflows are running successfully. If any fail, investigate and fix the issues.
