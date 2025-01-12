import os
import subprocess
import logging
from rich.console import Console
from config import theme

console = Console(theme=theme)

# List of commands that should be handled by os.system
shell_commands = ['cd', 'cls', 'clear', 'exit', 'start', 'open', 'echo']

#from main
def execute_cli_command(command):
    try:
        # Handle cd commands
        if command.lower().startswith('cd '):
            # Extract the path after 'cd ' and handle '..' or folder name
            target_path = command[3:].strip()  # Remove 'cd ' prefix

            if target_path == "..":
                # Change to the parent directory
                os.chdir("..")
                console.print(f"Moved up one level to {os.getcwd()}", style="success")
            elif target_path:
                # Change to the specified directory
                try:
                    os.chdir(target_path)
                    console.print(f"Changed directory to {os.getcwd()}", style="success")
                except FileNotFoundError:
                    console.print(f"[bold red]Error:[/bold red] Directory '{target_path}' not found.", style="error")
                    return f"Directory '{target_path}' not found."
            return f"Directory changed to {os.getcwd()}."

        # Check if the command is in the list of shell-specific commands
        if any(command.lower().startswith(shell_command) for shell_command in shell_commands):
            # Prevent 'exit' from terminating the script
            if 'exit' in command.lower():
                console.print("Exit command is ignored to prevent terminating the script.", style="warning")
                return "Exit command is ignored to prevent terminating the script."
            
            # Execute shell commands using os.system
            os.system(command)
            return f"Executed shell command: {command}"

        else:
            # Execute other commands using subprocess
            result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
            return result.stdout

    except subprocess.CalledProcessError as e:
        error_msg = f"Command '{command}' failed with error: {e.stderr.strip()}"
        logging.error(error_msg)
        
        if "permission denied" in e.stderr.lower():
            return f"Permission denied. You might need to run the command with 'sudo'. {error_msg}"
        elif "command not found" in e.stderr.lower():
            return f"Command not found. Please check the command syntax. {error_msg}"
        else:
            return error_msg
    except Exception as e:
        logging.error(f"Unexpected error occurred: {str(e)}")
        return f"An unexpected error occurred: {str(e)}"

#from setup project
def run_shell_command(command):
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
        if result.stdout:
            console.print(result.stdout, style="info")
        if result.stderr:
            console.print(result.stderr, style="error")
    except subprocess.CalledProcessError as e:
        console.print(f"Error executing command '{command}': {e.stderr.strip()}", style="error")