import os
import subprocess
from rich.console import Console
from command_exec import execute_command
from config import theme

# Initialize Console with the theme
console = Console(theme=theme)

def check_node_npm():
    try:
        node_check = subprocess.run(["node", "--version"], capture_output=True, text=True)
        npm_check = subprocess.run(["npm", "--version"], capture_output=True, text=True)

        if node_check.returncode != 0 or npm_check.returncode != 0:
            console.print("Node.js or npm is not installed. Please install them from: https://nodejs.org/en/download/", style="error")
            return False
        return True
    except Exception as e:
        console.print(f"Error while checking Node.js/npm: {e}", style="error")
        return False

def check_ruby():
    try:
        ruby_check = subprocess.run(["ruby", "--version"], capture_output=True, text=True)

        if ruby_check.returncode != 0:
            console.print("Ruby is not installed. Please install it from: https://www.ruby-lang.org/en/documentation/installation/", style="error")
            return False
        return True
    except Exception as e:
        console.print(f"Error while checking Ruby: {e}", style="error")
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

def execute_command(command):
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
        if result.stdout:
            console.print(result.stdout, style="info")
        if result.stderr:
            console.print(result.stderr, style="error")
    except subprocess.CalledProcessError as e:
        console.print(f"Error executing command '{command}': {e.stderr.strip()}", style="error")

def get_project_name(project_type):
    project_names = {
        "1": "static-website",
        "2": "react",
        "3": "java",
        "4": "flask",
        "5": "ruby-rails"
    }
    return project_names.get(project_type, "unknown-project")

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
        execute_command("npx create-react-app my-app && cd my-app && npm install && npm start")
        console.print("Setup completed for React app.", style="success")

    elif project_type == "5":  # Ruby on Rails
        if not check_ruby():
            return
        execute_command("rails new my-app && cd my-app")
        execute_command("bundle install")
        execute_command("rails server")
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
