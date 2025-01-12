from rich.console import Console
from config import theme

console = Console(theme=theme)

def view_command_history():
    try:
        # Open the command history log file in read mode
        with open("logs/command_history.log", "r") as file:
            content = file.read()
            
            # If the log is empty, inform the user
            if not content.strip():
                console.print("Command history is empty.", style="yellow")
                return

            # Print out the full command history without any filtering
            console.print("\nCommand History:", style="info")
            console.print("=" * 20)
            console.print(content, style="info")
            console.print("=" * 20)
            
    except FileNotFoundError:
        console.print("No command history found.", style="error")
    except Exception as e:
        console.print(f"An error occurred: {e}", style="error")