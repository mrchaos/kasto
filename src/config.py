import os
from src.schemas import LogConfig
from src.utils.load_config import load_config


config_logging = load_config("config/logger.yaml", LogConfig)
if config_logging:
    config_logging: LogConfig
    try:
        log_path = config_logging.handlers["file"]["filename"]
        # Create the log  folder if it does not exist
        if not os.path.exists(os.path.dirname(log_path)):
            os.makedirs(os.path.dirname(log_path))
    except Exception as e:
        raise Exception(f"Error loading logger configuration: {e}")