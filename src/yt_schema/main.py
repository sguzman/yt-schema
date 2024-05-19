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


class Version(BaseModel):
    current_git_head = p.TextField(null=True)
    release_git_head = p.TextField(unique=True)
    repository = p.TextField()
    version = p.TextField()


class Entry(BaseModel):
    abr = p.DoubleField()


class Tags(BaseModel):
    tag = p.TextField(unique=True)


class ChannelThumbnail(BaseModel):
    thumbnail_id = p.TextField(unique=True)
    preference = p.IntegerField(null=True)
    resolution = p.TextField(null=True)
    url = p.TextField()
    width = p.IntegerField(null=True)
    height = p.IntegerField(null=True)


class Payload(BaseModel):
    username = p.CharField(unique=True)
    type_of = p.TextField()
    version = p.ForeignKeyField(Version)
    availability = p.BooleanField(null=True)
    channel = p.TextField(unique=True)
    channel_follower_count = p.IntegerField(null=True)
    channel_id = p.TextField(unique=True)
    channel_url = p.TextField()
    description = p.TextField()
    entries = p.ForeignKeyField(Entry)
    epoch = p.DateTimeField()
    extractor = p.TextField()
    extractor_key = p.TextField()
    payload_id = p.TextField(unique=True)
    modified_date = p.DateTimeField(null=True)
    original_url = p.TextField()
    playlist_count = p.IntegerField(null=True)
    release_year = p.IntegerField(null=True)
    tags = p.ForeignKeyField(Tags)
    thumbnails = p.ForeignKeyField(ChannelThumbnail)
    title = p.TextField(unique=True)
    uploader = p.TextField(unique=True)
    uploader_id = p.TextField(unique=True)
    uploader_url = p.TextField()
    view_count = p.IntegerField(null=True)
    webpage_url = p.TextField()
    webpage_url_basename = p.TextField()
    webpage_url_host = p.TextField()


tables = [Payload, Version, Entry, Tags, ChannelThumbnail]

db.drop_tables(tables, safe=True)
db.create_tables(tables)

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
