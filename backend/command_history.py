from rich.console import Console
from config import theme
import re
from collections import Counter
import cohere
from cohere_client import CohereClient
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Initialize Cohere API client
cohere_api_key = os.getenv('COHERE_API_KEY')
co = cohere.Client(cohere_api_key)

# Initialize Console with the theme
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

            # Print out the full command history
            console.print("\nCommand History:", style="info")
            console.print("=" * 20)
            console.print(content, style="info")
            console.print("=" * 20)

            # Extract CLI commands from the log (assuming they are prefixed with a special tag)
            commands = re.findall(r"CLI command: (.+)", content)
            
            if not commands:
                console.print("No CLI commands found in history.", style="yellow")
                return

            # Count the frequency of each command
            command_counter = Counter(commands)
            top_commands = command_counter.most_common(10)

            console.print("\nTop 10 Most Used CLI Commands:", style="info")
            console.print("=" * 20)
            for command, count in top_commands:
                # Use Cohere API to generate NLP translation for each command
                prompt = f"Translate this CLI command to a natural language description: {command}"
                response = co.generate(
                    model="command-r-plus",
                    prompt=prompt,
                    max_tokens=20,
                    temperature=0.5,
                )
                nlp_translation = response.generations[0].text.strip()

                console.print(f"{count}x - {command}")
                console.print(f"NLP Translation: {nlp_translation}", style="green")
                console.print("-" * 20)
            
    except FileNotFoundError:
        console.print("No command history found.", style="error")
    except Exception as e:
        console.print(f"An error occurred: {e}", style="error")