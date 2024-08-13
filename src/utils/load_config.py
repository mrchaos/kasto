"""yaml에서 config를 로드하는 함수를 작성합니다.
"""

import yaml
from typing import TypeVar, Type
from pydantic import BaseModel

_T = TypeVar('_T', bound=BaseModel)

def load_config(file_path: str, config_class: Type[_T]) -> _T:
    with open(file_path) as f:
        config_data = yaml.safe_load(f)
        return config_class(**config_data)
