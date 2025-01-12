import os
import subprocess
from rich.console import Console
from config import theme
from command_exec import run_shell_command
import cohere
from cohere_client import CohereClient
from dotenv import load_dotenv
import re

# Load environment variables from .env file
load_dotenv()

# Initialize Cohere API client
cohere_api_key = os.getenv('COHERE_API_KEY')
co = cohere.Client(cohere_api_key)

# Initialize Console with the theme
console = Console(theme=theme)

def check_node_npm():
    try:
        # Check if Node.js is installed
        node_check = subprocess.run(["node", "--version"], capture_output=True, text=True)
        if node_check.returncode != 0:
            console.print("Node.js is not installed. Please install it from: https://nodejs.org/en/download/", style="error")
            return False

        # Check if npm is installed
        npm_check = subprocess.run(["npm", "--version"], capture_output=True, text=True)
        if npm_check.returncode != 0:
            console.print("npm is not installed. Please install it from: https://nodejs.org/en/download/", style="error")
            return False

        # Both Node.js and npm are installed
        return True

    except FileNotFoundError:
        console.print("Node.js or npm is not installed or not in PATH. Please install them from: https://nodejs.org/en/download/", style="error")
        return False

    except Exception as e:
        console.print(f"Unexpected error while checking Node.js/npm: {e}", style="error")
        return False

def check_ruby():
    try:
        # Check if Ruby is installed
        ruby_check = subprocess.run(["ruby", "--version"], capture_output=True, text=True)
        if ruby_check.returncode != 0:
            console.print("Ruby is not installed. Please install it from: https://www.ruby-lang.org/en/documentation/installation/", style="error")
            return False

        # Check if Rails is installed
        rails_check = subprocess.run(["rails", "--version"], capture_output=True, text=True)
        if rails_check.returncode != 0:
            console.print("Rails is not installed. Please install it using: gem install rails", style="error")
            return False

        # Both Ruby and Rails are installed
        return True

    except FileNotFoundError:
        console.print("Ruby or Rails is not installed or not in PATH. Please install them as per instructions on: https://www.ruby-lang.org/en/documentation/installation/ and https://rubyonrails.org/", style="error")
        return False

    except Exception as e:
        console.print(f"Unexpected error while checking Ruby/Rails: {e}", style="error")
        return False

def check_java():
    try:
        java_check = subprocess.run(["java", "-version"], capture_output=True, text=True)

        if java_check.returncode != 0:
            console.print("Java is not installed. Please install it from: https://www.oracle.com/java/technologies/javase-jdk11-downloads.html", style="error")
            return False
        return True
    except Exception as e:
        console.print(f"Error while checking Java: {e}", style="error")
        return False

def check_flask():
    try:
        flask_check = subprocess.run(["python", "-m", "flask", "--version"], capture_output=True, text=True)

        if flask_check.returncode != 0:
            console.print("Flask is not installed. Please install Flask using 'pip install flask'.", style="error")
            return False
        return True
    except Exception as e:
        console.print(f"Error while checking Flask: {e}", style="error")
        return False

def get_project_name(project_type):
    project_names = {
        "1": "static-website",
        "2": "react",
        "3": "java",
        "4": "flask",
        "5": "ruby-rails"
    }
    return project_names.get(project_type, "unknown-project")

def generate_code_for_file(file_path, user_input):
    """
    This function interacts with the Cohere API to generate or modify code 
    in a specific file based on the user's input.
    """
    try:
        # Read the content of the current file
        with open(file_path, 'r') as file:
            file_content = file.read()

        # Prepare the prompt for Cohere
        prompt = f"""
        Below is the code content of a file in my project:

        {file_content}

        I want to add or modify to the file:

        {user_input}

        Please generate the appropriate code to fulfill the request.
        """

        # Call the Cohere API to generate or modify the code
        response = co.generate(
            model="command-r-plus",  # You can choose the model based on your needs
            prompt=prompt,
            max_tokens=200,  # Adjust as necessary
            temperature=0.7,  # Adjust for creativity or precision
        )

        # Get the generated code from the API response
        console.log(response)
        generated_code = response.generations[0].text.strip()
        console.log(generated_code)
        # Find the position of the starting and ending code blocks
        #start_code = "```html"
        #end_code = "```"

        #regex 
        match = re.search(r"```([a-zA-Z]+)\n(.*?)```", generated_code, re.DOTALL)
        if match:
            # Extract the code content between the markers (the second group captures the content)
            generated_code = match.group(2).strip()

        # Find the starting and ending indices
        #start_index = generated_code.find(start_code) + len(start_code)
        #end_index = generated_code.find(end_code, start_index)

        #if start_index != -1 and end_index != -1:
            # Extract only the HTML content between the code block markers
            #generated_code = generated_code[start_index:end_index].strip()

        # Append the generated code to the file
        #with open(file_path, 'a') as file:
            #file.write("\n" + generated_code)

        with open(file_path, 'w') as file:  # Use 'w' to overwrite the file
            file.write(generated_code)

        console.print(f"Code generated and added to {file_path}:\n{generated_code}", style="info")

    except Exception as e:
        console.print(f"Error generating code: {e}", style="error")
        return None

def setup_project():
    console.print("What project would you like to set up:", style="bold")
    console.print("1. Static Website")
    console.print("2. React")
    console.print("3. Java")
    console.print("4. Flask")
    console.print("5. Ruby on Rails")
    project_type = input("Please enter the number for your choice: ").strip()

    project_dir = input("Enter the directory path where you'd like to create the project: ").strip()
    project_dir = project_dir.replace('\u202a', '')  # Remove any unwanted characters

    project_folder = os.path.join(project_dir, f"{get_project_name(project_type)}-project")

    if not os.path.exists(project_folder):
        os.makedirs(project_folder, exist_ok=True)
        console.print(f"Created new directory {project_folder}", style="success")
    else:
        console.print(f"Directory {project_folder} already exists, navigating into it.", style="info")

    os.chdir(project_folder)
    console.print(f"Changed directory to {os.getcwd()}", style="success")

    if project_type == "2":  # React
        if not check_node_npm():
            return
        run_shell_command("npx create-react-app my-app && cd my-app && npm install && npm start")
        console.print("Setup completed for React app.", style="success")

    elif project_type == "5":  # Ruby on Rails
        if not check_ruby():
            return
        run_shell_command("rails new my-app && cd my-app")
        run_shell_command("bundle install")
        run_shell_command("rails server")
        console.print("Setup completed for Ruby on Rails app.", style="success")

    elif project_type == "3":  # Java
        if not check_java():
            return
        os.makedirs("src", exist_ok=True)
        with open("src/Main.java", "w") as f:
            f.write("""public class Main {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
}
            """)
        console.print("Setup completed for Java project.", style="success")

    elif project_type == "4":  # Flask
        if not check_flask():
            return
        os.makedirs("app", exist_ok=True)
        with open("app/app.py", "w") as f:
            f.write("""from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World!" 

if __name__ == "__main__":
    app.run(debug=True)
            """)
        console.print("Setup completed for Flask app.", style="success")

    elif project_type == "1":  # Static Website
        os.makedirs("assets", exist_ok=True)
        with open("index.html", "w") as f:
            f.write("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Static Website</title>
</head>
<body>
    <h1>Welcome to my Static Website!</h1>
</body>
</html>
            """)
        with open("assets/styles.css", "w") as f:
            f.write("""body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
    text-align: center;
}
            """)
        console.print("Setup completed for Static Website.", style="success")

    else:
        console.print("Invalid choice. Please choose a valid project type.", style="error")
        return

    # Ask if the user wants to modify any file
    modify_files = input("Do you want to modify any file? (yes/no): ").strip().lower()
    if modify_files == 'yes':
        while True:
            file_to_work_on = input("Enter the file path you want to modify: ").strip()
            if os.path.exists(file_to_work_on):
                user_input = input("What do you want to add or modify in this file? ").strip()
                generate_code_for_file(file_to_work_on, user_input)
            else:
                console.print(f"File {file_to_work_on} does not exist in the project directory.", style="error")

            continue_modifying = input("Do you want to modify another file? (yes/no): ").strip().lower()
            if continue_modifying != "yes":
                break
    else:
        console.print("No file modification selected. Exiting...", style="info")
