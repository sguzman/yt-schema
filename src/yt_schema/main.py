import logging
import json

import peewee as p
import datetime


db = p.SqliteDatabase("yt.db")


def load_json():
    logging.info("load_json")
    return json.loads(open("resources/channel.json").read())


def keys(data):
    logging.info("keys")

    logging.info("keys: %s", data.keys())


class BaseModel(p.Model):
    class Meta:
        database = db


class User(BaseModel):
    username = p.CharField(unique=True)


class Tweet(BaseModel):
    user = p.ForeignKeyField(User, backref="tweets")
    message = p.TextField()
    created_date = p.DateTimeField(default=datetime.datetime.now)
    is_published = p.BooleanField(default=True)


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
