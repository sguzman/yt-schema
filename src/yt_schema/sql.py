import atexit
import logging
import peewee as p

from yt_schema.tables import tables

logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s", level=logging.INFO
)

db: p.SqliteDatabase = p.SqliteDatabase("yt.db")
db.connect()


def close_db():
    logging.info("close_db")
    db.close()


atexit.register(close_db)

db.drop_tables(tables, safe=True)
db.create_tables(tables)
