import atexit
import logging
import json

import peewee as p

db: p.SqliteDatabase = p.SqliteDatabase("yt.db")
db.connect()


def close_db():
    logging.info("close_db")
    db.close()


atexit.register(close_db)


def load_json():
    logging.info("load_json")
    return json.loads(open("resources/channel.json").read())


def keys(data):
    logging.info("keys")

    logging.info("keys: %s", data.keys())


class BaseModel(p.Model):
    class Meta:
        database = db


class Payload(BaseModel):
    username = p.CharField(unique=True)


db.create_tables([Payload])

# Enable timestamp and log level in log messages
logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s", level=logging.INFO
)


def main():
    logging.info("start")
    json_data = load_json()
    keys(json_data)
    logging.info("end")


if __name__ == "__main__":
    main()
