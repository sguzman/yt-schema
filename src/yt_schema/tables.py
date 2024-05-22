import atexit
import logging
import peewee as p
from typing import Dict, List

logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s", level=logging.DEBUG
)

db: p.SqliteDatabase = p.SqliteDatabase("yt.db")
db.connect()


def close_db():
    logging.info("close_db")
    db.close()


atexit.register(close_db)


class BaseModel(p.Model):
    class Meta:
        database = db


class FormatSortField(BaseModel):
    field = p.TextField(unique=True)


class HttpHeader(BaseModel):
    key = p.TextField()
    value = p.TextField()


class Format(BaseModel):
    abr = p.DoubleField(null=True)
    acodec = p.TextField(null=True)
    aspect_ratio = p.DoubleField(null=True)
    audio_ext = p.TextField()
    columns = p.IntegerField(null=True)
    ext = p.TextField()
    filesize_approx = p.IntegerField(null=True)
    format = p.TextField()
    format_id = p.TextField(null=True)
    format_note = p.TextField()
    fps = p.DoubleField(null=True)
    height = p.IntegerField(null=True)
    protocol = p.TextField()
    resolution = p.TextField()
    tbr = p.DoubleField(null=True)
    url = p.TextField()
    vbr = p.IntegerField(null=True)
    vcodec = p.TextField()
    video_ext = p.TextField()
    width = p.IntegerField(null=True)


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
    resolution = p.TextField()
    tbr = p.DoubleField()
    vbr = p.DoubleField()
    vcodec = p.TextField()
    width = p.IntegerField()


class VideoThumbnail(BaseModel):
    thumbnail_id = p.TextField(null=True)
    preference = p.IntegerField(null=True)
    url = p.TextField()


class Payload(BaseModel):
    type_of = p.TextField()
    availability = p.BooleanField(null=True)
    channel = p.TextField(unique=True)
    channel_follower_count = p.IntegerField(null=True)
    channel_id = p.TextField(unique=True)
    channel_url = p.TextField()
    description = p.TextField()
    epoch = p.DateTimeField()
    extractor = p.TextField()
    extractor_key = p.TextField()
    payload_id = p.TextField(unique=True)
    modified_date = p.DateTimeField(null=True)
    original_url = p.TextField()
    playlist_count = p.IntegerField(null=True)
    release_year = p.IntegerField(null=True)
    title = p.TextField(unique=True)
    uploader = p.TextField(unique=True)
    uploader_id = p.TextField(unique=True)
    uploader_url = p.TextField()
    view_count = p.IntegerField(null=True)
    webpage_url = p.TextField()
    webpage_url_basename = p.TextField()
    webpage_url_host = p.TextField(null=True)


class Entry(BaseModel):
    last_playlist_index = p.IntegerField(null=True)
    has_drm = p.BooleanField(null=True)
    abr = p.DoubleField(null=True)
    acodec = p.TextField(null=True)
    age_limit = p.IntegerField(null=True)
    aspect_ratio = p.DoubleField(null=True)
    asr = p.IntegerField(null=True)
    audio_channels = p.IntegerField(null=True)
    availability = p.TextField(null=True)
    average_rating = p.DoubleField(null=True)
    channel = p.TextField(null=True)
    channel_follower_count = p.IntegerField(null=True)
    channel_id = p.TextField(null=True)
    channel_url = p.TextField(null=True)
    comment_count = p.IntegerField(null=True)
    description = p.TextField(null=True)
    display_id = p.TextField(null=True)
    duration = p.IntegerField(null=True)
    duration_string = p.TextField(null=True)
    dynamic_range = p.TextField(null=True)
    epoch = p.DateTimeField(null=True)
    ext = p.TextField(null=True)
    extractor = p.TextField(null=True)
    extractor_key = p.TextField(null=True)
    filesize = p.IntegerField(null=True)
    format = p.TextField(null=True)
    format_id = p.TextField(null=True)
    format_note = p.TextField(null=True)
    fps = p.IntegerField(null=True)
    fulltitle = p.TextField(null=True)
    height = p.IntegerField(null=True)
    entry_id = p.TextField(unique=True)
    is_live = p.BooleanField(null=True)
    language = p.TextField(null=True)
    like_count = p.IntegerField(null=True)
    live_status = p.TextField(null=True)
    n_entries = p.IntegerField(null=True)
    original_url = p.TextField(null=True)
    playable_in_embed = p.BooleanField(null=True)
    playlist = p.TextField(null=True)
    playlist_auto_number = p.IntegerField(null=True)
    playlist_count = p.IntegerField(null=True)
    playlist_id = p.TextField(null=True)
    playlist_index = p.IntegerField(null=True)
    playlist_title = p.TextField(null=True)
    playlist_uploader = p.TextField(null=True)
    playlist_uploader_id = p.TextField(null=True)
    protocol = p.TextField(null=True)
    release_timestamp = p.DateTimeField(null=True)
    release_year = p.IntegerField(null=True)
    resolution = p.TextField(null=True)
    stretched_ratio = p.DoubleField(null=True)
    tbr = p.DoubleField(null=True)
    thumbnail = p.TextField(null=True)
    title = p.TextField(null=True)
    uploader_date = p.DateTimeField(null=True)
    uploader_id = p.TextField(null=True)
    uploader_url = p.TextField(null=True)
    vbr = p.DoubleField(null=True)
    vcodec = p.TextField(null=True)
    view_count = p.IntegerField(null=True)
    webpage_url = p.TextField(null=True)
    webpage_url_basename = p.TextField(null=True)
    webpage_url_domain = p.TextField(null=True)
    width = p.IntegerField(null=True)


class SubtitleType(BaseModel):
    video_id = p.ForeignKeyField(Entry)
    language = p.TextField()


class Subtitle(BaseModel):
    video_id = p.ForeignKeyField(Entry)
    subtitle_type = p.ForeignKeyField(SubtitleType)
    ext = p.TextField()
    name = p.TextField()
    url = p.TextField()


class VideoCategory(BaseModel):
    video_id = p.ForeignKeyField(Entry)
    category = p.TextField()


class ChannelCategory(BaseModel):
    channel_id = p.ForeignKeyField(Payload)
    category = p.TextField(unique=True)


class AutomaticCaptions(BaseModel):
    video_id = p.ForeignKeyField(Entry)
    language = p.CharField(max_length=2)


class Caption(BaseModel):
    auto_cap = p.ForeignKeyField(AutomaticCaptions)
    ext = p.TextField()
    protocol = p.TextField(null=True)
    url = p.TextField()


class Chapter(BaseModel):
    video_id = p.ForeignKeyField(Entry)
    start_time = p.DoubleField()
    end_time = p.DoubleField()
    title = p.TextField()


class ChannelThumbnail(BaseModel):
    channel_id = p.ForeignKeyField(Payload)
    thumbnail_id = p.TextField(null=True)
    preference = p.IntegerField(null=True)
    resolution = p.TextField(null=True)
    url = p.TextField()
    width = p.IntegerField(null=True)
    height = p.IntegerField(null=True)


class Fragment(BaseModel):
    video_id = p.ForeignKeyField(Entry)
    duration = p.DoubleField()
    url = p.TextField()


class Heatmap(BaseModel):
    video_id = p.ForeignKeyField(Entry)
    end_time = p.DoubleField()
    start_time = p.DoubleField()
    value = p.DoubleField()


class VideoTag(BaseModel):
    video_id = p.ForeignKeyField(Entry)
    tag = p.TextField()


class ChannelTag(BaseModel):
    channel_id = p.ForeignKeyField(Payload)
    tag = p.TextField(unique=True)


class Version(BaseModel):
    channel_id = p.ForeignKeyField(Payload)
    current_git_head = p.TextField(null=True)
    release_git_head = p.TextField(unique=True)
    repository = p.TextField()
    version = p.TextField()


tables = [
    Version,
    FormatSortField,
    Caption,
    AutomaticCaptions,
    ChannelCategory,
    VideoCategory,
    Chapter,
    Fragment,
    HttpHeader,
    Format,
    ChannelTag,
    VideoTag,
    Heatmap,
    RequestedDownload,
    Subtitle,
    SubtitleType,
    VideoThumbnail,
    Entry,
    ChannelThumbnail,
    Payload,
]


db.drop_tables(tables, safe=True)
db.create_tables(tables)


def version(channel: Payload, data: Dict):
    logging.info("version")
    Version.create(
        channel_id=channel,
        current_git_head=data.get("current_git_head"),
        release_git_head=data.get("release_git_head"),
        repository=data.get("repository"),
        version=data.get("version"),
    )


def fragments(video: Entry, data: List[Dict]):
    # If none
    if data is None:
        return

    logging.info(f"{len(data)} fragments")

    for d in data:
        Fragment.create(
            video_id=video,
            duration=d.get("duration"),
            url=d.get("url"),
        )


def http_headers(video: Entry, data: Dict):
    # If none
    if data is None:
        return

    logging.info(f"{len(data)} http_headers")
    for d in data.keys():
        key = d
        value = data.get(d)
        HttpHeader.create(
            video_id=video,
            key=key,
            value=value,
        )


def formats(video: Entry, data: List[Dict]):
    # If none
    if data is None:
        return

    logging.info(f"{len(data)} formats")
    for d in data:
        Format.create(
            video_id=video,
            abr=d.get("abr"),
            acodec=d.get("acodec"),
            aspect_ratio=d.get("aspect_ratio"),
            audio_ext=d.get("audio_ext"),
            columns=d.get("columns"),
            ext=d.get("ext"),
            filesize_approx=d.get("filesize_approx"),
            format=d.get("format"),
            format_id=d.get("format_id"),
            format_note=d.get("format_note"),
            fps=d.get("fps"),
            height=d.get("height"),
            protocol=d.get("protocol"),
            resolution=d.get("resolution"),
            tbr=d.get("tbr"),
            url=d.get("url"),
            vbr=d.get("vbr"),
            vcodec=d.get("vcodec"),
            video_ext=d.get("video_ext"),
            width=d.get("width"),
        )

        # Fragment
        fragments(video, d.get("fragments"))

        # Http Headers
        http_headers(video, d.get("http_headers"))


def heatmaps(video: Entry, data: List[Dict]):
    # If none
    if data is None:
        return

    logging.info(f"{len(data)} heatmaps")
    for d in data:
        Heatmap.create(
            video_id=video,
            end_time=d.get("end_time"),
            start_time=d.get("start_time"),
            value=d.get("value"),
        )


def requested_download(video: Entry, data: List[Dict]):
    # If none
    if data is None:
        return

    logging.info(f"{len(data)} requested_download")

    for d in data:
        RequestedDownload.create(
            write_download_archive=d.get("write_download_archive"),
            filename=d.get("filename"),
            abr=d.get("abr"),
            acodec=d.get("acodec"),
            aspect_ratio=d.get("aspect_ratio"),
            audio_ext=d.get("audio_ext"),
            columns=d.get("columns"),
            ext=d.get("ext"),
            filesize_approx=d.get("filesize_approx"),
            format=d.get("format"),
            format_id=d.get("format_id"),
            format_note=d.get("format_note"),
            fps=d.get("fps"),
            height=d.get("height"),
            protocol=d.get("protocol"),
            resolution=d.get("resolution"),
            tbr=d.get("tbr"),
            vbr=d.get("vbr"),
            vcodec=d.get("vcodec"),
            width=d.get("width"),
        )

        # Requested Formats
        formats(video, d.get("requested_formats"))


def subtitles(video: Entry, s: SubtitleType, data: List[Dict]):
    # If none
    if data is None:
        return

    logging.info(f"{len(data)} subtitles")

    for sub in data:
        Subtitle.create(
            video_id=video,
            subtitle_type=s,
            ext=sub.get("ext"),
            name=sub.get("name"),
            url=sub.get("url"),
        )


def subtitle_type(video: Entry, data: Dict):
    # If none
    if data is None:
        return []

    logging.info(f"{len(data)} subtitles")
    for sub in data.keys():
        s = SubtitleType.create(
            video_id=video,
            language=sub,
        )

        # Subtitles
        subtitles(video, s, data.get(sub))


def format_sort_field(video: Entry, data: List[str]):
    # If none
    if data is None:
        return

    logging.info(f"{len(data)} format_sort_field")
    for d in data:
        FormatSortField.create(video_id=video, field=d)


def caption(video: Entry, auto_captions: AutomaticCaptions, data: Dict):
    # If none
    if data is None:
        return

    logging.info(f"{len(data)} captions")
    for d in data:
        Caption.create(
            video_id=video,
            auto_cap=auto_captions,
            ext=d.get("ext"),
            protocol=d.get("protocol"),
            url=d.get("url"),
        )


def automatic_captions(video: Entry, data: Dict):
    # If none
    if data is None:
        return

    logging.info(f"{len(data)} automatic_captions")
    for d in data.keys():
        ac = AutomaticCaptions.create(video_id=video, language=d)

        # Captions
        caption(video, ac, data.get(d))


def video_categories(video: Entry, data: List[str]):
    # If none
    if data is None:
        return

    logging.info(f"{len(data)} video categories")
    for d in data:
        VideoCategory.create(video_id=video, category=d)


def chapters(video: Entry, data: List[Dict]):
    # If none
    if data is None:
        return

    logging.info(f"{len(data)} chapters")
    for d in data:
        Chapter.create(
            video_id=video,
            start_time=d.get("start_time"),
            end_time=d.get("end_time"),
            title=d.get("title"),
        )

        # Fragments
        fragments(video, d.get("fragments"))


def entries(data: List[Dict]):
    logging.info(f"{len(data)} entries")

    for d in data:
        logging.info(f"Video: {d.get('title')}")
        e = Entry.create(
            last_playlist_index=d.get("__last_playlist_index"),
            has_drm=d.get("has_drm"),
            abr=d.get("abr"),
            acodec=d.get("acodec"),
            age_limit=d.get("age_limit"),
            aspect_ratio=d.get("aspect_ratio"),
            asr=d.get("asr"),
            audio_channels=d.get("audio_channels"),
            availability=d.get("availability"),
            average_rating=d.get("average_rating"),
            channel=d.get("channel"),
            channel_follower_count=d.get("channel_follower_count"),
            channel_id=d.get("channel_id"),
            channel_url=d.get("channel_url"),
            chapters=d.get("chapters"),
            comment_count=d.get("comment_count"),
            description=d.get("description"),
            display_id=d.get("display_id"),
            duration=d.get("duration"),
            duration_string=d.get("duration_string"),
            dynamic_range=d.get("dynamic_range"),
            epoch=d.get("epoch"),
            ext=d.get("ext"),
            extractor=d.get("extractor"),
            extractor_key=d.get("extractor_key"),
            filesize=d.get("filesize"),
            fps=d.get("fps"),
            fulltitle=d.get("fulltitle"),
            entry_id=d.get("id"),
            is_live=d.get("is_live"),
            language=d.get("language"),
            like_count=d.get("like_count"),
            live_status=d.get("live_status"),
            n_entries=d.get("n_entries"),
            original_url=d.get("original_url"),
            playable_in_embed=d.get("playable_in_embed"),
            playlist=d.get("playlist"),
            playlist_auto_number=d.get("playlist_auto_number"),
            playlist_count=d.get("playlist_count"),
            playlist_id=d.get("playlist_id"),
            playlist_index=d.get("playlist_index"),
            playlist_title=d.get("playlist_title"),
            playlist_uploader=d.get("playlist_uploader"),
            playlist_uploader_id=d.get("playlist_uploader_id"),
            protocol=d.get("protocol"),
            release_timestamp=d.get("release_timestamp"),
            release_year=d.get("release_year"),
            requested_subtitles=d.get("requested_subtitles"),
            resolution=d.get("resolution"),
            stretched_ratio=d.get("stretched_ratio"),
            tbr=d.get("tbr"),
            thumbnail=d.get("thumbnail"),
            title=d.get("title"),
            uploader_date=d.get("uploader_date"),
            uploader_id=d.get("uploader_id"),
            uploader_url=d.get("uploader_url"),
            vbr=d.get("vbr"),
            vcoded=d.get("vcodec"),
            view_count=d.get("view_count"),
            was_live=d.get("was_live"),
            webpage_url=d.get("webpage_url"),
            webpage_url_basename=d.get("webpage_url_basename"),
            webpage_url_domain=d.get("webpage_url_domain"),
            width=d.get("width"),
        )

        # Format
        formats(e, d.get("formats"))

        # Heatmaps
        heatmaps(e, d.get("heatmap"))

        # Requested Downloads
        requested_download(e, d.get("requested_download"))

        # Requested Formats
        formats(e, d.get("requested_formats"))

        # Subtitles
        subtitle_type(e, d.get("subtitles"))

        # Video Thumbnails
        video_thumbnails(e, d.get("thumbnails"))

        # Tags
        video_tags(e, d.get("tags"))

        # Format Sort Field
        format_sort_field(e, d.get("format_sort_field"))

        # Automatic Captions
        automatic_captions(e, d.get("automatic_captions"))

        # Video Categories
        video_categories(e, d.get("categories"))

        # Chapters
        chapters(e, d.get("chapters"))

    logging.debug(entries)
    return entries


def video_tags(p: Entry, data: List[str]):
    # If none
    if data is None:
        return

    logging.info(f"{len(data)} tags")
    for d in data:
        VideoTag.create(video_id=p, tag=d)


def channel_tags(p: Payload, data: List[str]):
    # If none
    if data is None:
        return

    logging.info(f"{len(data)} tags")
    for d in data:
        ChannelTag.create(channel_id=p, tag=d)


def video_thumbnails(v: Entry, data: List[Dict]):
    # If none
    if data is None:
        return

    logging.info(f"{len(data)} video thumbnails")

    for d in data:
        VideoThumbnail.create(
            video_id=v,
            thumbnail_id=d.get("thumbnail_id"),
            preference=d.get("preference"),
            url=d.get("url"),
        )


def channel_thumbnails(channel: Payload, data: List[Dict]):
    # If none
    if data is None:
        return

    logging.info(f"{len(data)} channel thumbnails")
    for d in data:
        ChannelThumbnail.create(
            channel_id=channel,
            thumbnail_id=d.get("thumbnail_id"),
            preference=d.get("preference"),
            resolution=d.get("resolution"),
            url=d.get("url"),
            width=d.get("width"),
            height=d.get("height"),
        )


def payload(data: Dict) -> Payload:
    logging.info("payload")

    p = Payload.create(
        type_of=data.get("_type"),
        availability=data.get("availability"),
        channel=data.get("channel"),
        channel_follower_count=data.get("channel_follower_count"),
        channel_id=data.get("channel_id"),
        channel_url=data.get("channel_url"),
        description=data.get("description"),
        epoch=data.get("epoch"),
        extractor=data.get("extractor"),
        extractor_key=data.get("extractor_key"),
        payload_id=data.get("id"),
        modified_date=data.get("modified_date"),
        original_url=data.get("original_url"),
        playlist_count=data.get("playlist_count"),
        release_year=data.get("release_year"),
        title=data.get("title"),
        uploader=data.get("uploader"),
        uploader_id=data.get("uploader_id"),
        uploader_url=data.get("uploader_url"),
        view_count=data.get("view_count"),
        webpage_url=data.get("webpage_url"),
        webpage_url_basename=data.get("webpage_url_basename"),
        webpage_url_host=data.get("webpage_url_host"),
    )

    # Initialize Channel Thumbnails
    channel_thumbnails(p, data.get("thumbnails"))

    # Initialize entries
    entries(data.get("entries"))

    # Initialize version
    version(p, data.get("_version"))

    # Initialize tags
    channel_tags(p, data.get("tags"))

    logging.debug(p)
    return p


def create(data: Dict):
    logging.info("create")
    payload(data)
