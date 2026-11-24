# Set up on Windows with WSL

Use WSL 2 with Ubuntu to run the tutorial's Linux commands on Windows.

## Install or inspect WSL

For a new installation, run this command in PowerShell as Administrator.

```powershell
wsl --install -d Ubuntu-24.04
```

Follow the prompts, restart if asked, and create your Linux username and password. If you already use WSL, check your installed distributions with this command.

```powershell
wsl --list --verbose
```

For version requirements or help switching an existing distribution to WSL 2, see the installation guide. [Microsoft WSL installation guide](https://learn.microsoft.com/en-us/windows/wsl/install)

## Continue inside Ubuntu

Open the Ubuntu terminal for the rest of setup. To keep the checkout in your Linux home directory, create a folder for it.

```bash
mkdir -p ~/projects
cd ~/projects
```

Follow the Linux guide in that terminal to clone `main` and install the Linux Rust tools. [Linux setup](setup-linux.md)

Any text editor works. If you use VS Code, open the checkout with its WSL extension and install Rust Analyzer in the WSL environment.

## Board access

You can complete Lesson 00 with your terminal and editor. For board work later in the course, attach the board's USB connection to WSL. [Microsoft WSL USB guide](https://learn.microsoft.com/en-us/windows/wsl/connect-usb)
