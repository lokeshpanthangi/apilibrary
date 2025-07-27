# Installation Guide for API Library v1.1.0

## Quick Installation

### Option 1: Install from Wheel (Recommended)

1. Download the wheel file: `apilib-1.1.0-py3-none-any.whl`
2. Install using pip:
   ```bash
   pip install apilib-1.1.0-py3-none-any.whl
   ```

### Option 2: Install from Source

1. Clone or download the repository
2. Navigate to the project directory
3. Install using pip:
   ```bash
   pip install .
   ```

## Post-Installation Setup

### Windows Users

After installation, you need to add the Python Scripts directory to your PATH:

#### Automatic Setup (Recommended)
Run this PowerShell command as Administrator:
```powershell
$scriptsPath = (python -m site --user-base) + "\Python" + (python -c "import sys; print(sys.version_info.major, sys.version_info.minor, sep='')") + "\Scripts"
[Environment]::SetEnvironmentVariable('PATH', [Environment]::GetEnvironmentVariable('PATH', 'User') + ';' + $scriptsPath, 'User')
```

#### Manual Setup
1. Find your Python Scripts directory:
   ```bash
   python -m site --user-base
   ```
   Then append `\Python313\Scripts` (adjust version number as needed)

2. Add this path to your system PATH:
   - Open System Properties → Environment Variables
   - Edit User PATH variable
   - Add the Scripts directory path

3. Restart your terminal

### Linux/macOS Users

The commands should be automatically available after installation. If not:

1. Find your local bin directory:
   ```bash
   python -m site --user-base
   ```
   Then append `/bin`

2. Add to your shell profile (`.bashrc`, `.zshrc`, etc.):
   ```bash
   export PATH="$PATH:$(python -m site --user-base)/bin"
   ```

3. Reload your shell or run:
   ```bash
   source ~/.bashrc  # or ~/.zshrc
   ```

## Verification

Test that the installation worked:

```bash
# Test help messages
storekey
fetchkey

# Test functionality
storekey testprovider "test-key-123"
fetchkey testprovider
```

You should see:
- Usage instructions for both commands
- Successful storage and retrieval of the test key

## Troubleshooting

### Commands Not Found

If you get "command not found" errors:

1. Verify installation:
   ```bash
   pip list | grep apilib
   ```

2. Check if scripts are installed:
   ```bash
   python -c "import apilib; print('Installation successful')"
   ```

3. Manually find script location:
   ```bash
   find $(python -m site --user-base) -name "storekey*" 2>/dev/null
   ```

4. Add the found directory to your PATH

### Permission Issues

If you encounter permission errors:

- Use `pip install --user` for user-only installation
- On Windows, run PowerShell as Administrator for PATH modifications
- On Linux/macOS, avoid using `sudo` with pip

## Features

Once installed, you can:

- **Store API keys**: `storekey provider "your-api-key"`
- **Retrieve API keys**: `fetchkey provider`
- **Use any provider name**: Not limited to predefined providers
- **Secure storage**: All keys are encrypted locally
- **Cross-platform**: Works on Windows, Linux, and macOS

## Support

If you encounter issues:

1. Check that Python 3.6+ is installed
2. Ensure pip is up to date: `pip install --upgrade pip`
3. Try reinstalling: `pip uninstall apilib && pip install apilib-1.1.0-py3-none-any.whl`