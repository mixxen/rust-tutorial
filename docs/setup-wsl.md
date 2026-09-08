# Set up on Windows with WSL

WSL runs a Linux environment on Windows. The tutorial's primary Windows path is **WSL 2 with Ubuntu**, so you can use the same commands as a Linux learner.

## Install or inspect WSL

For a new installation, open PowerShell as Administrator:

```powershell
wsl --install -d Ubuntu-24.04
```

Follow the prompts, restart if requested, and create your Linux username and password. If WSL is already installed, inspect it instead of reinstalling:

```powershell
wsl --list --verbose
```

Use Microsoft's [installation instructions](https://learn.microsoft.com/en-us/windows/wsl/install) for version requirements, updates, or converting an existing distribution to WSL 2. WSL installation depends on your Windows configuration and has not been interactively tested in this authoring session.

## Continue inside Ubuntu

Open the Ubuntu terminal. The remaining setup commands belong there, **not in PowerShell**. Keep the checkout in the Linux home directory, for example:

```bash
mkdir -p ~/projects
cd ~/projects
```

Now follow [Linux setup](setup-linux.md). Use the Linux installation of Rust in WSL rather than mixing a Windows `cargo.exe` with Linux build tools.

VS Code is optional. Its WSL extension can open the Linux checkout; select the Rust Analyzer extension in that remote environment. A plain editor and terminal are sufficient.

## What about the board?

Lesson 00 does not use the board. Leave USB setup out of the first learning session. Later board access needs an explicit USB attachment path; a device visible in Windows is not automatically available inside WSL. The later hardware setup must follow Microsoft's [USB connection guide](https://learn.microsoft.com/en-us/windows/wsl/connect-usb) and verify the actual NUCLEO-H723ZG connection.

No WSL USB, probe, or board execution results are claimed by this Phase 1 host batch.
