import cohere

class CohereClient:
    def __init__(self, api_key):
        self.co = cohere.Client(api_key)
    
    def translate_command(self, nlp_command, os_type):
        if os_type.lower() == "windows":
            prompt = f"Translate this natural language to a single windows CLI command: {nlp_command}"
        elif os_type.lower() == "linux":
            prompt = f"Translate this natural language to a single linux CLI command: {nlp_command}"
        elif os_type.lower() == "macos":
            prompt = f"Translate this natural language to a single macOS CLI: {nlp_command}"
        else:
            print(f"Invalid OS type: {os_type}")
            return None

        try:
            response = self.co.generate(
                model="command-r-plus",
                prompt=prompt,
                max_tokens=20,  # Adjust token limit if needed
                temperature=0.2,
            )

            cli_command = response.generations[0].text.strip().replace("```", "").strip()
            cli_command = ' '.join(cli_command.splitlines()).strip()

            return cli_command
        except cohere.CohereAPIError as e:
            print(f"API error: {e}")
            return None
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return None