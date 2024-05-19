import atexit
import logging
import peewee as p
from typing import Dict, List

logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s", level=logging.INFO
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


tables = [
    Version,
    FilesToMove,
    FormatSortField,
    Caption,
    AutomaticCaptions,
    Category,
    Chapter,
    Fragment,
    HttpHeader,
    Format,
    Tag,
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


def version(data: Dict) -> Version:
    logging.info("version")
    return Version(
        current_git_head=data.get("current_git_head"),
        release_git_head=data.get("release_git_head"),
        repository=data.get("repository"),
        version=data.get("version"),
    )


def fragments(data: List[Dict]) -> List[Fragment]:
    logging.info(f"{len(data)} fragments")
    fragments = []
    for d in data:
        f = Fragment(
            duration=d.get("duration"),
            url=d.get("url"),
        )
        fragments.append(f)

    return fragments


def http_headers(data: List[Dict]) -> List[HttpHeader]:
    logging.info(f"{len(data)} http_headers")
    http_headers = []
    for d in data:
        h = HttpHeader(
            key=d.get("key"),
            value=d.get("value"),
        )
        http_headers.append(h)

    return http_headers


def formats(data: List[Dict]) -> List[Format]:
    logging.info(f"{len(data)} formats")
    formats = []
    for d in data:
        f = Format(
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
            fragments=fragments(d.get("fragments")),
            height=d.get("height"),
            http_headers=http_headers(d.get("http_headers")),
            protocol=d.get("protocol"),
            resolution=d.get("resolution"),
            tbr=d.get("tbr"),
            url=d.get("url"),
            vbr=d.get("vbr"),
            vcodec=d.get("vcodec"),
            video_ext=d.get("video_ext"),
            width=d.get("width"),
        )
        formats.append(f)

    return formats


def heatmaps(data: List[Dict]) -> List[Heatmap]:
    logging.info(f"{len(data)} heatmaps")
    heatmaps = []
    for d in data:
        h = Heatmap(
            end_time=d.get("end_time"),
            start_time=d.get("start_time"),
            value=d.get("value"),
        )
        heatmaps.append(h)

    return heatmaps


def requested_download(data: List[Dict]) -> List[RequestedDownload]:
    # If none
    if data is None:
        logging.info("requested_download is none")
        return None

    logging.info(f"{len(data)} requested_download")
    requested_downloads = []
    for d in data:
        rd = RequestedDownload(
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
            requested_format=format(d.get("requested_format")),
            resolution=d.get("resolution"),
            tbr=d.get("tbr"),
            vbr=d.get("vbr"),
            vcodec=d.get("vcodec"),
            width=d.get("width"),
        )
        requested_downloads.append(rd)

    return requested_downloads


def subtitle(data: List[Dict]) -> List[Subtitle]:
    logging.info(f"{len(data)} subtitles")
    subtitles = []
    for sub in data:
        print(sub)
        s = Subtitle(
            ext=sub.get("ext"),
            name=sub.get("name"),
            url=sub.get("url"),
        )
        subtitles.append(s)

    return subtitles


def subtitle_type(data: Dict) -> List[SubtitleType]:
    logging.info(f"{len(data)} subtitles")
    subtitles = []
    for sub in data.keys():
        s = SubtitleType(
            language=sub,
            subtitles=subtitle(data.get(sub)),
        )
        subtitles.append(s)

    return subtitles


def entries(data: List[Dict]) -> List[Entry]:
    logging.info(f"{len(data)} entries")
    entries = []
    for d in data:
        e = Entry(
            last_playlist_index=d.get("__last_playlist_index"),
            format_sort_field=d.get("format_sort_field"),
            has_drm=d.get("has_drm"),
            abr=d.get("abr"),
            acodec=d.get("acodec"),
            age_limit=d.get("age_limit"),
            aspect_ratio=d.get("aspect_ratio"),
            asr=d.get("asr"),
            audio_channels=d.get("audio_channels"),
            automatic_captions=d.get("automatic_captions"),
            availability=d.get("availability"),
            average_rating=d.get("average_rating"),
            categories=d.get("categories"),
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
            format=format(d.get("formats")),
            fps=d.get("fps"),
            fulltitle=d.get("fulltitle"),
            heatmap=heatmaps(d.get("heatmap")),
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
            requested_download=requested_download(d.get("requested_download")),
            requested_formats=format(d.get("requested_formats")),
            requested_subtitles=d.get("requested_subtitles"),
            resolution=d.get("resolution"),
            stretched_ratio=d.get("stretched_ratio"),
            subtitles=subtitle_type(d.get("subtitles")),
            tags=tags(d.get("tags")),
            tbr=d.get("tbr"),
            thumbnail=d.get("thumbnail"),
            thumbnails=video_thumbnails(d.get("thumbnails")),
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

        entries.append(e)
    return entries


def tags(data: List[str]) -> List[Tag]:
    logging.info(f"{len(data)} tags")
    tags = []
    for d in data:
        t = Tag(tag=d)
        tags.append(t)

    return tags


def video_thumbnails(data: List[Dict]) -> List[VideoThumbnail]:
    logging.info(f"{len(data)} thumbnails")
    thumbnails = []
    for d in data:
        t = VideoThumbnail(
            thumbnail_id=d.get("thumbnail_id"),
            preference=d.get("preference"),
            resolution=d.get("resolution"),
        )
        thumbnails.append(t)

    return thumbnails


def channel_thumbnails(data: List[Dict]) -> List[ChannelThumbnail]:
    logging.info(f"{len(data)} thumbnails")
    thumbnails = []
    for d in data:
        t = ChannelThumbnail(
            thumbnail_id=d.get("thumbnail_id"),
            preference=d.get("preference"),
            resolution=d.get("resolution"),
            url=d.get("url"),
            width=d.get("width"),
            height=d.get("height"),
        )
        thumbnails.append(t)

    return thumbnails


def payload(data: Dict) -> Payload:
    logging.info("payload")
    return Payload(
        files_to_move=data.get("__files_to_move"),
        type_of=data.get("_type"),
        version=version(data.get("_version")),
        availability=data.get("availability"),
        channel=data.get("channel"),
        channel_follower_count=data.get("channel_follower_count"),
        channel_id=data.get("channel_id"),
        channel_url=data.get("channel_url"),
        description=data.get("description"),
        entries=entries(data.get("entries")),
        epoch=data.get("epoch"),
        extractor=data.get("extractor"),
        extractor_key=data.get("extractor_key"),
        payload_id=data.get("id"),
        modified_date=data.get("modified_date"),
        original_url=data.get("original_url"),
        playlist_count=data.get("playlist_count"),
        release_year=data.get("release_year"),
        tags=tags(data.get("tags")),
        thumbnails=channel_thumbnails(data.get("thumbnails")),
        title=data.get("title"),
        uploader=data.get("uploader"),
        uploader_id=data.get("uploader_id"),
        uploader_url=data.get("uploader_url"),
        view_count=data.get("view_count"),
        webpage_url=data.get("webpage_url"),
        webpage_url_basename=data.get("webpage_url_basename"),
        webpage_url_host=data.get("webpage_url_host"),
    )


def create(data: Dict):
    logging.info("create")
    p = payload(data)
    p.save()
