from box.exceptions import  BoxValueError
from box.exceptions import  BoxValueError
from box import ConfigBox
import yaml
from pathlib import Path
from ensure import ensure_annotations
from src.llm_connect.logging.logger import logger

@ensure_annotations
def read_yaml(path_to_yaml) -> ConfigBox:
    """
    reads yaml file and returns
    Args:
       Valueerror: IF YAML file is empty
       e: empty file

    Raises:
    ConfigBox.ConfigBox:
    """
    try:
        with open(path_to_yaml, "r") as f:
            config = yaml.safe_load(f)
            return ConfigBox(config)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        logger.error(e)