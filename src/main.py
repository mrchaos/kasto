import asyncio
from src.utils.logger import logger
from src.utils.load_config import load_config
from src.schemas import Crawling
import json

data = {
    "site_url": "https://www.google.com",
    "search_keyword": "python",
    "max_workers": 10,
    "data": {
        "data": {
            "key1": "value1"
        }
    }
}


async def convert_to_crawling(data: dict) -> None:
    try:
        crawling = Crawling(**data)
        logger.info(f"Converted data: {crawling}")
        logger.info(f"Data keys: {crawling.data.data.keys()}")
        logger.info(f"Data val1: {crawling.data.data['key1']}")
    except Exception as e:
        logger.error(f"Error converting data: {e}")

async def logg_test() -> None:
    logger.info("Hello, World!")
    logger.debug("Hello, World!")
    logger.warning("Hello, World!")
    logger.error("Hello, World!")
    logger.critical("Hello, World!")

async def main():
    # await logg_test()
    await convert_to_crawling(data)

if __name__ == "__main__":
    # asyncio.run(main())
    # asyncio.run(ModernKivyApp().run())
    ModernKivyApp().run()