import logging
import os
import json

from yt_schema.tables import create


def load_json(name: str):
    logging.info(f"load_json {name}")
    return json.loads(open(f"resources/{name}").read())


# Enable timestamp and log level in log messages
logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s", level=logging.INFO
)


def main():
    logging.info("start")
    # For each json file in the resources folder, create a table
    for file in os.listdir("resources"):
        if file.endswith("pretty.json"):
            js = load_json(file)
            logging.info(f"Creating table for {file}")
            create(js)
    logging.info("end")


if __name__ == "__main__":
    main()
