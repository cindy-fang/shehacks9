# Synapse

Synapse is an interactive terminal assistant that translates natural language commands into system-specific commands, and helps you execute them in your terminal. It's built using Python and the Cohere API for natural language processing.

---

## Project Setup

Before running the application, follow the instructions below to set up the environment and get the application running.

### 1. **Clone or Download the Repo**
   - Clone the repository or fork it to your own GitHub account and download it to your local machine.

### 2. **Set up the Cohere API Key**

   - You'll need a **Cohere API Key** to interact with the application.

   #### a. **Create a .env File**
      - In the root of the project directory, create a file named `.env`.

   #### b. **Add Your API Key**
      - Get your API key from [Cohere's website](https://cohere.ai) (you may need to sign up).
      - Add the API key to the `.env` file like this:

   ```env
   COHERE_API_KEY=your_cohere_api_key_here
  ```


### 3. **Install Dependencies**
   - Open a command prompt or terminal in your project directory.
   - Run the following command to install all required Python dependencies:

     ```bash
     pip install -r requirements.txt
     ```

### 4. **Navigate to the Backend Folder**
   - Change to the `backend` directory where the core application files are located:

     ```bash
     cd backend
     ```

### 5. **Run the Application**
   - Start the application by running:

     ```bash
     python app.py
     ```

### 6. **Have Fun!**
   - Enjoy using Termibuddy! Interact with the terminal, and let Termibuddy translate natural language commands into system commands for you.
