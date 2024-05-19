import logging
import json

from yt_schema.tables import create


def load_json():
    logging.info("load_json")
    return json.loads(open("resources/channel.json").read())


# Enable timestamp and log level in log messages
logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s", level=logging.DEBUG
)


def main():
    logging.info("start")
    js = load_json()
    create(js)
    logging.info("end")


if __name__ == "__main__":
    main()
