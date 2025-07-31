# Page 4: Refactoring Code with a Single Command

![Refactor Mockup](gemini_cli_refactor_mockup.png)

Refactoring code is an essential part of the software development process. It's how we improve the design of our code, make it more readable, and reduce its complexity. But it can also be a time-consuming and error-prone process.

The Gemini CLI takes the pain out of refactoring with its powerful `refactor` command. This command allows you to perform complex refactoring operations with a single command, and it even provides a preview of the changes before they're applied.

### The `refactor` Command

The `refactor` command takes a file path and a set of refactoring options as arguments. Let's say you want to refactor your `auth.py` file to use the `requests` library instead of the built-in `urllib` library.

With the Gemini CLI, you can do this with a single command:

```bash
$ gemini refactor auth.py --library requests
```

The Gemini CLI will then analyze the file and perform the following changes:

*   **Replace all instances of `urllib` with `requests`.**
*   **Update the code to use the `requests` library's API.**
*   **Add the `requests` library to your project's dependencies.**

### Previewing Changes

Before applying the changes, the Gemini CLI will show you a diff of the proposed changes. This allows you to review the changes and make sure they're what you expect.

If you're happy with the changes, you can apply them with the `--apply` flag:

```bash
$ gemini refactor auth.py --library requests --apply
```

### Other Refactoring Options

The `refactor` command supports a wide range of refactoring options, including:

*   **Renaming variables, functions, and classes.**
*   **Extracting code into new functions and classes.**
*   **Inlining functions and classes.**
*   **Changing the signature of a function.**
*   **And much more.**

We'll explore the full range of refactoring options in a later section. But for now, take some time to experiment with the `refactor` command. It's a powerful tool that can save you a lot of time and effort.

**Next Page: Generating Unit Tests Automatically**
