import yaml

def load_config(config_path="config/config.yaml"):
    """
    Loads a YAML config file and returns it as a dictionary.
    :param config_path: Path to the YAML config file.
    :return: Dictionary with config values.
    """
    with open(config_path, "r") as f:
        return yaml.safe_load(f) 