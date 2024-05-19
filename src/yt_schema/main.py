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


class FilesToMove(BaseModel):
    file = p.TextField(null=True)


class FormatSortField(BaseModel):
    field = p.TextField(unique=True)


class Caption(BaseModel):
    ext = p.TextField()
    protocol = p.TextField()
    url = p.TextField()


class AutomaticCaptions(BaseModel):
    language = p.CharField(max_length=2)
    caption = p.ForeignKeyField(Caption)


class Category(BaseModel):
    category = p.TextField(unique=True)


class Chapter(BaseModel):
    start_time = p.DoubleField()
    end_time = p.DoubleField()
    title = p.TextField()


class Fragment(BaseModel):
    duration = p.DoubleField()
    url = p.TextField()


class HttpHeader(BaseModel):
    key = p.TextField()
    value = p.TextField()


class Format(BaseModel):
    abr = p.DoubleField()
    acodec = p.TextField()
    aspect_ratio = p.DoubleField()
    audio_ext = p.TextField()
    columns = p.IntegerField()
    ext = p.TextField()
    filesize_approx = p.IntegerField(null=True)
    format = p.TextField()
    format_id = p.TextField(unique=True)
    format_note = p.TextField()
    fps = p.DoubleField()
    fragments = p.ForeignKeyField(Fragment)
    height = p.IntegerField()
    http_headers = p.ForeignKeyField(HttpHeader)
    protocol = p.TextField()
    resolution = p.TextField()
    tbr = p.DoubleField(null=True)
    url = p.TextField()
    vbr = p.IntegerField()
    vcodec = p.TextField()
    video_ext = p.TextField()
    width = p.IntegerField()


class Tag(BaseModel):
    tag = p.TextField(unique=True)


class Heatmap(BaseModel):
    end_time = p.DoubleField()
    start_time = p.DoubleField()
    value = p.DoubleField()


class RequestedDownload(BaseModel):
    write_download_archive = p.BooleanField()
    filename = p.TextField()
    abr = p.DoubleField()
    acodec = p.TextField()
    aspect_ratio = p.DoubleField()
    audio_ext = p.TextField()
    columns = p.IntegerField()
    ext = p.TextField()
    filesize_approx = p.IntegerField(null=True)
    format = p.TextField()
    format_id = p.TextField(unique=True)
    format_note = p.TextField()
    fps = p.DoubleField()
    height = p.IntegerField()
    protocol = p.TextField()
    requested_format = p.ForeignKeyField(Format)
    resolution = p.TextField()
    tbr = p.DoubleField()
    vbr = p.DoubleField()
    vcodec = p.TextField()
    width = p.IntegerField()


class Subtitle(BaseModel):
    ext = p.TextField()
    name = p.TextField()
    url = p.TextField()


class SubtitleType(BaseModel):
    language = p.TextField()
    subtitles = p.ForeignKeyField(Subtitle)


class VideoThumbnail(BaseModel):
    thumbnail_id = p.TextField(unique=True)
    preference = p.IntegerField(null=True)


class Entry(BaseModel):
    last_playlist_index = p.IntegerField()
    format_sort_field = p.ForeignKeyField(FormatSortField)
    has_drm = p.BooleanField(null=True)
    abr = p.DoubleField()
    acodec = p.TextField()
    age_limit = p.IntegerField(null=True)
    aspect_ratio = p.DoubleField()
    asr = p.IntegerField()
    audio_channels = p.IntegerField()
    automatic_captions = p.ForeignKeyField(AutomaticCaptions)
    availability = p.TextField()
    average_rating = p.DoubleField(null=True)
    categories = p.ForeignKeyField(Category)
    channel = p.TextField()
    channel_follower_count = p.IntegerField()
    channel_id = p.TextField()
    channel_url = p.TextField()
    chapters = p.ForeignKeyField(Chapter)
    comment_count = p.IntegerField()
    description = p.TextField()
    display_id = p.TextField()
    duration = p.IntegerField()
    duration_string = p.TextField()
    dynamic_range = p.TextField()
    epoch = p.DateTimeField()
    ext = p.TextField()
    extractor = p.TextField()
    extractor_key = p.TextField()
    filesize = p.IntegerField()
    format = p.TextField()
    format_id = p.TextField()
    format_note = p.TextField()
    formats = p.ForeignKeyField(Format)
    fps = p.IntegerField()
    fulltitle = p.TextField(unique=True)
    heatmap = p.ForeignKeyField(Heatmap)
    height = p.IntegerField()
    entry_id = p.TextField(unique=True)
    is_live = p.BooleanField()
    language = p.TextField(null=True)
    like_count = p.IntegerField()
    live_status = p.TextField()
    n_entries = p.IntegerField()
    original_url = p.TextField()
    playable_in_embed = p.BooleanField()
    playlist = p.TextField()
    playlist_auto_number = p.IntegerField()
    playlist_count = p.IntegerField()
    playlist_id = p.TextField()
    playlist_index = p.IntegerField()
    playlist_title = p.TextField()
    playlist_uploader = p.TextField()
    playlist_uploader_id = p.TextField()
    protocol = p.TextField()
    release_timestamp = p.DateTimeField(null=True)
    release_year = p.IntegerField(null=True)
    requested_download = p.ForeignKeyField(RequestedDownload)
    requested_formats = p.ForeignKeyField(Format)
    resolution = p.TextField()
    stretched_ratio = p.DoubleField(null=True)
    subtitles = p.ForeignKeyField(SubtitleType)
    tags = p.ForeignKeyField(Tag)
    tbr = p.DoubleField()
    thumbnail = p.TextField()
    thumbnails = p.ForeignKeyField(VideoThumbnail)
    title = p.TextField()
    uploader_date = p.DateTimeField()
    uploader_id = p.TextField()
    uploader_url = p.TextField()
    vbr = p.DoubleField()
    vcodec = p.TextField()
    view_count = p.IntegerField()
    webpage_url = p.TextField()
    webpage_url_basename = p.TextField()
    webpage_url_domain = p.TextField()
    width = p.IntegerField()


class ChannelThumbnail(BaseModel):
    thumbnail_id = p.TextField(unique=True)
    preference = p.IntegerField(null=True)
    resolution = p.TextField(null=True)
    url = p.TextField()
    width = p.IntegerField(null=True)
    height = p.IntegerField(null=True)


class Payload(BaseModel):
    files_to_move = p.ForeignKeyField(FilesToMove)
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
    tags = p.ForeignKeyField(Tag)
    thumbnails = p.ForeignKeyField(ChannelThumbnail)
    title = p.TextField(unique=True)
    uploader = p.TextField(unique=True)
    uploader_id = p.TextField(unique=True)
    uploader_url = p.TextField()
    view_count = p.IntegerField(null=True)
    webpage_url = p.TextField()
    webpage_url_basename = p.TextField()
    webpage_url_host = p.TextField()


tables = [Payload, Version, Entry, Tag, ChannelThumbnail]

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
