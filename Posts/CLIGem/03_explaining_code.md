# Page 3: Your First Command - Explaining Code

![Code Flow](gemini_cli_code_flow.png)

Now that you have the Gemini CLI installed and configured, it's time to see it in action. One of the most powerful features of the Gemini CLI is its ability to explain complex code in plain English. This can be incredibly useful when you're working with a new codebase, or when you're trying to understand a particularly tricky piece of logic.

### The `explain` Command

The `explain` command is your new best friend. It takes a file path as an argument and provides a detailed explanation of the code in that file.

Let's say you have a Python file called `auth.py` that contains some complex authentication logic. To get an explanation of this file, you would run the following command:

```bash
$ gemini explain auth.py
```

The Gemini CLI will then analyze the file and provide a detailed explanation of the code, including:

*   **A high-level summary of the file's purpose.**
*   **A breakdown of the functions and classes in the file.**
*   **An explanation of the logic within each function.**
*   **A description of the file's dependencies and how it interacts with other parts of the codebase.**

### Explaining a Specific Function

If you only want to understand a specific function within a file, you can use the `--function` flag.

For example, to get an explanation of the `authenticate_user` function in `auth.py`, you would run the following command:

```bash
$ gemini explain auth.py --function authenticate_user
```

This will provide a detailed explanation of the `authenticate_user` function, without the noise of the rest of the file.

### Going Deeper

The `explain` command is just the beginning. You can also use the Gemini CLI to:

*   **Trace the execution of a function.**
*   **Visualize the relationships between different parts of your codebase.**
*   **Identify potential bugs and security vulnerabilities.**

We'll explore these advanced features in later sections. But for now, take some time to experiment with the `explain` command. Try it on some of your own code, or on a complex open-source project. You'll be amazed at how much time and effort it can save you.

**Next Page: Refactoring Code with a Single Command**
