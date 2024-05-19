import logging
import json


def load_json():
    logging.info("load_json")
    return json.loads(open("resources/channel.json").read())


# Enable timestamp and log level in log messages
logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s", level=logging.INFO
)


def main():
    logging.info("start")
    _ = load_json()
    logging.info("end")


if __name__ == "__main__":
    main()
