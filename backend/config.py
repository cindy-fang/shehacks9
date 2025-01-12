import logging
import os
from rich.theme import Theme

# Ensure logs directory exists
if not os.path.exists('logs'):
    os.makedirs('logs')

# Setup logging
logging.basicConfig(
    filename='logs/command_history.log',
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# Optionally add a console handler for logging output to console as well
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
console_handler.setFormatter(formatter)
logging.getLogger().addHandler(console_handler)

# Initialize Console Theme
theme = Theme({
    "info": "cyan",
    "error": "bold red",
    "success": "bold green",
    "prompt": "bold white",
    "background": "on blue",
})
