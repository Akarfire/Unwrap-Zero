import os
import sys
import platform

# WINDOWS
def setup_windows(script_path, command_name):
    import winreg
    
    # Absolute script path
    script_path_abs = os.path.abspath(script_path)
    script_dir = os.path.dirname(script_path_abs)
    
    # Create batch file
    batch_directory = os.path.join(script_dir, "Run")
    os.makedirs(batch_directory, exist_ok=True)
    
    batch_file = os.path.join(batch_directory, f'{command_name}.bat')
    with open(batch_file, 'w') as f:
        f.write(f'@echo off\npython "{script_path_abs}" %*\n')
    
    # Add batch_directory to PATH
    key = winreg.OpenKey(
        winreg.HKEY_CURRENT_USER,
        "Environment",
        0,
        winreg.KEY_READ | winreg.KEY_SET_VALUE
    )

    try:
        current_path, _ = winreg.QueryValueEx(key, "PATH")
    except FileNotFoundError:
        current_path = ""

    paths = current_path.lower().split(";")
    if batch_directory.lower() not in paths:
        new_path = current_path + (";" if current_path else "") + batch_directory
        winreg.SetValueEx(key, "PATH", 0, winreg.REG_EXPAND_SZ, new_path)
    winreg.CloseKey(key)
    
    print(f"Installed {command_name} in {batch_directory}")

# LINUX
def setup_linux(script_path, command_name):
    pass


# SCRIPT
def main():    
    script_path = "./UnwrapZero.py"
    command_name = 'unwrapz'
    
    if not os.path.exists(script_path):
        print(f"Error: {script_path} not found")
        sys.exit(1)
    
    if platform.system() == 'Windows':
        setup_windows(script_path, command_name)
    else:
        setup_linux(script_path, command_name)


if __name__ == '__main__':
    main()