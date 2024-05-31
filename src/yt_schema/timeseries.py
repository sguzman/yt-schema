import atexit
import logging
import datetime
import peewee as p
from typing import Dict, List, Tuple, Union

logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s", level=logging.DEBUG
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
    timestamp = p.DateTimeField(default=p.datetime.datetime.now)

    video_id = p.TextField()
    view_count = p.BigIntegerField()
    comment_count = p.BigIntegerField(null=True)


class ChannelStats(BaseModel):
    timestamp = p.DateTimeField(default=p.datetime.datetime.now)
    channel_id = p.TextField()

    subscriber_count = p.BigIntegerField()
    video_count = p.IntegerField()
    view_count = p.BigIntegerField()


# Class for heatmap data
class HeatmapStats(BaseModel):
    timestamp = p.DateTimeField(default=p.datetime.datetime.now)
    video_id = p.TextField()
    start_time = p.DoubleField()
    end_time = p.DoubleField()
    value = p.DoubleField()


tables = [VideoStats, ChannelStats, HeatmapStats]


db.drop_tables(tables, safe=True)
db.create_tables(tables)


def heatmap(data: List[Dict]):
    # Log number of heatmaps
    logging.debug(f"{len(data)} heatmaps stats")

    # Get video id
    video_id = data[0].get("display_id")
    hs: List[Tuple[datetime.datetime, str, float, float, float]] = []

    for d in data:
        if "heatmap" in d and d.get("heatmap") is not None:
            for h in d.get("heatmap"):
                hs.append(
                    (
                        datetime.datetime.now(),
                        video_id,
                        h.get("start_time"),
                        h.get("end_time"),
                        h.get("value"),
                    )
                )

    HeatmapStats.insert_many(hs).execute()


def video(data: List[Dict]):
    # Log number of videos
    logging.debug(f"{len(data)} video stats")

    VideoStats.insert_many(
        [
            (
                datetime.datetime.now(),
                d.get("display_id"),
                d.get("view_count"),
                d.get("comment_count"),
            )
            for d in data
        ]
    ).execute()


# find all entries objects
# If current object has an "entries" key, call this function again with the value of "entries"
# Entry objects SHOULD NOT have an "entries" key
def find_all_entries(data: Dict, total=[]) -> List[Dict]:
    all_entries = []

    if "entries" in data:
        for entry in data["entries"]:
            if "entries" in entry:
                all_entries.extend(entry["entries"])
            else:
                all_entries.append(entry)

    return all_entries


def channel(data: Dict[str, Union[str, int, List[Dict[str, Union[str, int]]]]]) -> None:
    """
    Record channel statistics.

    Args:
        data (Dict[str, Union[str, int, List[Dict[str, Union[str, int]]]]]):
            Dictionary containing channel statistics.

    Returns:
        None
    """
    logging.debug(f"channel stats: {data['channel']}")

    all_entries: List[Dict[str, Union[str, int]]] = find_all_entries(data)
    logging.debug(f"Num of entries: {len(all_entries)}")

    # Sum up all view counts for each channel from all entries
    entries: List[int] = [entry["view_count"] for entry in all_entries]

    view_sum: int = sum(entries)

    logging.debug(f"Sum of views for channel: {view_sum}")

    ChannelStats.create(
        timestamp=datetime.datetime.now(),
        channel_id=data["channel_id"],
        subscriber_count=all_entries[0].get("channel_follower_count"),
        video_count=len(all_entries),
        view_count=view_sum,
    )

    video(all_entries)

    # Get heatmap data
    heatmap(all_entries)


def create(data: Dict):
    # Log keys in the data dictionary
    channel(data)
