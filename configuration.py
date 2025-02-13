import configparser
import json
from flask import Flask, jsonify

# Configuration file path
CONFIG_FILE = "config.ini"
JSON_FILE = "config_data.json"

def parse_config(file_path):
    """Reads and parses the configuration file."""
    config = configparser.ConfigParser()
    try:
        config.read(file_path)
        if not config.sections():
            raise ValueError("Configuration file is empty or invalid")
        
        config_data = {section: dict(config.items(section)) for section in config.sections()}
        return config_data
    except Exception as e:
        print(f"Error reading config file: {e}")
        return None

def save_to_json(data):
    """Saves extracted data as a JSON file."""
    with open(JSON_FILE, "w") as json_file:
        json.dump(data, json_file, indent=4)

def load_from_json():
    """Loads data from the JSON file."""
    try:
        with open(JSON_FILE, "r") as json_file:
            return json.load(json_file)
    except FileNotFoundError:
        return {}

# Initialize Flask app
app = Flask(__name__)

@app.route("/config", methods=["GET"])
def get_config():
    """API endpoint to get the latest configuration."""
    return jsonify(load_from_json())

if __name__ == "__main__":
    config_data = parse_config(CONFIG_FILE)
    if config_data:
        save_to_json(config_data)
        print("Configuration successfully parsed and saved as JSON.")
    app.run(debug=True)
# In the code snippet above, we have a configuration file config.ini that contains some configuration data. We read and parse this configuration file using the parse_config function, which returns a dictionary of configuration data. We then save this data as a JSON file using the save_to_json function. The load_from_json function loads the data from the JSON file.