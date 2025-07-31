# Page 2: Installation and Setup - Let's Get Started

![Gemini CLI Installation Mockup](gemini_cli_install_mockup.png)

Getting started with the Gemini CLI is a straightforward process. In this section, we'll walk you through the steps to install the tool and configure it for your development environment.

### Prerequisites

Before we begin, make sure you have the following installed on your system:

*   **Node.js and npm:** The Gemini CLI is distributed as an npm package, so you'll need to have Node.js and npm installed. You can download them from the official [Node.js website](https://nodejs.org/).

### Installation

Once you have Node.js and npm installed, you can install the Gemini CLI with a single command:

```bash
$ npm install -g @google/gemini-cli
```

This will install the Gemini CLI globally on your system, which means you can run it from any directory.

### Authentication

After the installation is complete, you'll need to authenticate the Gemini CLI with your Google account. This is a one-time process that will allow the tool to access the Gemini API on your behalf.

To authenticate, run the following command:

```bash
$ gemini auth login
```

This will open a new tab in your web browser and prompt you to log in to your Google account. Once you've logged in, you'll be asked to grant the Gemini CLI permission to access your account. After you've granted permission, you can close the browser tab and return to your terminal.

### Configuration

The Gemini CLI is designed to work out of the box, but there are a few configuration options you can customize to tailor the tool to your workflow.

To view the current configuration, run the following command:

```bash
$ gemini config list
```

This will display a list of the available configuration options and their current values. To set a configuration option, you can use the `gemini config set` command.

For example, you can set the default output format to JSON with the following command:

```bash
$ gemini config set output.format json
```

We'll explore the available configuration options in more detail in a later section.

### You're Ready to Go!

That's it! You've successfully installed and configured the Gemini CLI. You're now ready to start using the power of AI in your terminal.

**Next Page: Your First Command - Explaining Code**
