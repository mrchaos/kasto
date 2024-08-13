from pydantic import BaseModel, Field

class LogConfig(BaseModel):
    version: int
    disable_existing_loggers: bool
    formatters: dict
    handlers: dict
    loggers: dict

class Data(BaseModel):
    data: dict = Field(default_factory=dict)
class Crawling(BaseModel):
    site_url: str
    search_keyword: str
    max_workers: int
    data: Data

