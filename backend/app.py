from prompt_toolkit import PromptSession
from prompt_toolkit.styles import Style
from command_history import view_command_history
from command_exec import execute_cli_command
from cohere_client import CohereClient
from config import theme
from rich.console import Console
import logging
from dotenv import load_dotenv
import os
from setup_project import setup_project  
import platform #detect os! 

# Load environment variables from .env file
load_dotenv()

# Initialize Cohere API client
cohere_api_key = os.getenv('COHERE_API_KEY')
cohere_client = CohereClient(cohere_api_key)

# Initialize Console with the theme
console = Console(theme=theme)

# Define prompt_toolkit style
style = Style.from_dict({
    'prompt': 'bold #FF9D00',
    'input': '#0000ff',  
})

def get_os_type():
    """Automatically detect the OS type."""
    system = platform.system().lower()
    if system == "windows":
        return "windows"
    elif system == "linux":
        return "linux"
    elif system == "darwin":  # macOS is identified as 'Darwin' on most systems
        return "macos"
    else:
        return None

def main():
    session = PromptSession()
    os_type = get_os_type()

    if not os_type:
        console.print("Could not determine the operating system automatically.", style="error")
        return  # Exit if the OS cannot be determined

    console.print(f"Detected OS: {os_type.capitalize()}", style="info")  # Show detected OS

    while True:
        try:
            action = session.prompt("What would you like to do? (ask/view/setup/exit): ", style=style).strip().lower()
            if action == "view":
                view_command_history()
                continue
            elif action == "exit":
                console.print("\nExiting...", style="info")
                break
            elif action == "ask":
                nlp_command = session.prompt("$ask ", style=style)
                logging.info(f"NLP command: {nlp_command}")
                cli_command = cohere_client.translate_command(nlp_command, os_type)
                
                if cli_command is None:
                    console.print("Sorry, I couldn't generate a command for that OS.", style="error")
                    continue

                edited_command = session.prompt(f'Edit and confirm command (default: "{cli_command}"): ', default=cli_command, style=style)

                if 'rm -rf' in edited_command or 'dd if=' in edited_command or 'mkfs' in edited_command:
                    console.print("[bold red]Warning: This command can cause serious damage![/bold red]")
                    final_confirmation = session.prompt(f'Are you sure you want to run "{edited_command}"? This action cannot be undone! [y/N] ', style=style)
                    if final_confirmation.lower() != 'y':
                        console.print("Command execution aborted.", style="bold red")
                        continue

                confirmation = session.prompt(f'Execute "{edited_command}"? [y/N] ', style=style)
                if confirmation.lower() == 'y':
                    output = execute_cli_command(edited_command)
                    console.print(output, style="success" if output else "error")
                    logging.info(f"CLI command: {edited_command}")

            elif action == "setup":
                setup_project()  
                continue
            else:
                console.print("Invalid action. Please enter 'ask', 'view', 'setup', or 'exit'.", style="error")

        except KeyboardInterrupt:
            console.print("\nExiting...", style="info")
            break
        except Exception as e:
            logging.error(f"Error: {e}")
            console.print(f"Error: {e}", style="error")

if __name__ == "__main__":
    main()
