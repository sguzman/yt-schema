import atexit
import logging
import peewee as p
from typing import Dict, List

logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s", level=logging.INFO
)

db: p.PostgresqlDatabase = p.PostgresqlDatabase(
    "youtube",  # Required by Peewee.
    user="admin",  # Will be passed directly to psycopg2.
    password="admin",  # Ditto.
    host="localhost",
    port="5555",
)  # Ditto.
db.connect()


def close_db():
    logging.info("close_db")
    db.close()


atexit.register(close_db)


class BaseModel(p.Model):
    class Meta:
        database = db


# Time series Tables for YouTube video and channel data


class VideoStats(BaseModel):
    video_id = p.TextField()
    timestamp = p.DateTimeField(default=p.datetime.datetime.now)
    view_count = p.BigIntegerField()
    comment_count = p.BigIntegerField()


class ChannelStats(BaseModel):
    channel_id = p.TextField()
    timestamp = p.DateTimeField(default=p.datetime.datetime.now)
    subscriber_count = p.BigIntegerField()
    video_count = p.IntegerField()
    view_count = p.BigIntegerField()


tables = [
    VideoStats,
    ChannelStats,
]


db.drop_tables(tables, safe=True)
db.create_tables(tables)


def video(data: List[Dict]):
    logging.info("video stats")

    for entry in data:
        # Continue if any of the required keys are missing
        if "id" not in entry or "view_count" not in entry:
            continue

        # Continue if entries are none
        if entry["id"] is None or entry["view_count"] is None:
            continue

        comment_count = 0
        if "comment_count" in entry:
            comment_count = entry["comment_count"]
        VideoStats.create(
            video_id=entry["id"],
            view_count=entry["view_count"],
            comment_count=comment_count,
        )


# Sum up all view counts for each channel from all entries
def view_sum(data: Dict):
    logging.info("view sum")
    # Ignore null entries
    return sum(
        [
            entry["view_count"]
            for entry in data["entries"]
            if "view_count" in entry and entry["view_count"] is not None
        ]
    )


# Find key from list of dictionaries until the key is found
def find_key(d: Dict, key: str):
    data = d["entries"]
    logging.info("find key")
    for entry in data:
        if key in entry:
            return entry[key]
    return None


def channel(data: Dict):
    logging.info("channel stats")

    ChannelStats.create(
        channel_id=data["channel_id"],
        subscriber_count=find_key(data, "channel_follower_count"),
        video_count=len(data["entries"]),
        view_count=view_sum(data),
    )


def create(data: Dict):
    logging.info("create stats")
    # Log keys in the data dictionary
    channel(data)
    video(data["entries"])
