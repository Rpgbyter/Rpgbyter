# Page 6: Writing Documentation and Commit Messages

![Documentation Mockup](gemini_cli_documentation.png)

Writing good documentation and clear commit messages is essential for maintaining a healthy codebase. But it's also a task that many developers find tedious and time-consuming.

The Gemini CLI can help you to write high-quality documentation and commit messages with its `doc` and `commit` commands.

### The `doc` Command

The `doc` command takes a file path as an argument and generates a detailed documentation file for the code in that file.

Let's say you want to generate documentation for your `auth.py` file. You would run the following command:

```bash
$ gemini doc auth.py
```

The Gemini CLI will then analyze the file and generate a new markdown file with the following information:

*   **A high-level summary of the file's purpose.**
*   **A detailed description of each function and class in the file.**
*   **A list of the parameters and return values for each function.**
*   **Code examples that show how to use the functions and classes in the file.**

### The `commit` Command

The `commit` command helps you to write clear and concise commit messages that follow the conventional commit format.

When you're ready to commit your changes, you can run the following command:

```bash
$ gemini commit
```

The Gemini CLI will then analyze your staged changes and suggest a commit message for you. You can then edit the suggested message and commit your changes.

### A Better Way to Document and Commit

The `doc` and `commit` commands are powerful tools that can help you to write better documentation and commit messages with less effort. They're a great way to improve the quality of your codebase and make it easier for other developers to understand your work.

**Next Page: Advanced Features**
