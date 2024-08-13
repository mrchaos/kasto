
import logging.config
from src.config import config_logging as config

def _setup_logging():
    logging.config.dictConfig(config)
    return logging.getLogger(__name__)

logger = _setup_logging()