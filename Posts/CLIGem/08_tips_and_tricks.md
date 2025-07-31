# Page 8: Tips and Tricks - Getting the Most Out of the Gemini CLI

![Tips and Tricks Mockup](gemini_cli_tips_and_tricks.png)

Now that you're familiar with the core features of the Gemini CLI, here are a few tips and tricks to help you get the most out of the tool.

### 1. Use Aliases

The Gemini CLI commands can be a bit long to type. You can save yourself some time and effort by creating aliases for your most commonly used commands.

For example, you can create an alias for the `gemini explain` command like this:

```bash
alias ge="gemini explain"
```

Then, you can simply type `ge auth.py` to get an explanation of the `auth.py` file.

### 2. Combine Commands

The Gemini CLI is designed to be composable. You can combine multiple commands to create powerful and flexible workflows.

For example, you can use the `explain` command to get an explanation of a file, and then use the `doc` command to generate documentation for that file:

```bash
$ gemini explain auth.py && gemini doc auth.py
```

### 3. Use the `--dry-run` Flag

The `--dry-run` flag is your friend. It allows you to preview the changes that a command will make without actually applying them. This is a great way to avoid making mistakes and to make sure that a command is going to do what you expect.

### 4. Experiment with Different Models

The Gemini CLI allows you to choose which Gemini model you want to use. Different models have different strengths and weaknesses, so it's worth experimenting with different models to see which one works best for you.

You can use the `gemini models list` command to see a list of the available models, and you can use the `gemini config set model` command to set the default model.

### 5. Join the Community

The Gemini CLI has a growing community of users and developers. If you have a question, or if you want to share a tip or trick of your own, be sure to join the community on the [Gemini CLI GitHub repository](https://github.com/Rpgbyter/Rpgbyter).

**Next Page: The Future of the Gemini CLI**
