import logging
import os
import json

from typing import Dict
from yt_schema import tables, timeseries


def load_json(name: str) -> Dict[str, object]:
    """
    Load a JSON file from the "resources" directory.

    This function takes a filename as input and reads the corresponding JSON file
    located in the "resources" directory. It returns the contents of the JSON file
    as a Python dictionary. If the specified JSON file does not exist in the
    "resources" directory, it raises a FileNotFoundError.

    Args:
        name (str): The name of the JSON file to load.

    Returns:
        Dict[str, object]: The contents of the JSON file as a Python Dictionary.

    Raises:
        FileNotFoundError: If the specified JSON file does not exist in the "resources" directory.
    """

    # Construct the path to the JSON file by joining the "resources" directory
    # with the provided filename.
    json_file: str = os.path.join("resources", name)

    # Open the JSON file and read its contents. The 'with' statement ensures that
    # the file is properly closed after reading.
    with open(json_file, "r") as f:
        # Load the JSON data from the file and store it in a variable. The json.load()
        # function reads the file and returns a Python dictionary.
        json_data: Dict[str, object] = json.load(f)

    # Return the loaded JSON data.
    return json_data


# Enable timestamp and log level in log messages
logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s", level=logging.INFO
)


def main():
    logging.info("start")
    # For each json file in the resources folder, create a table
    # Make a sorted list of the files in the resources folder
    files = sorted(filter(lambda s: s.endswith("pretty.json"), os.listdir("resources")))
    for file in files:
        js = load_json(file)
        logging.info(f"Creating table for {file}")
        timeseries.create(js)
        tables.create(js)

    logging.info("end")


if __name__ == "__main__":
    main()
