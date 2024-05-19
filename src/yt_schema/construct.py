# This file will contain method constructors to map JSON data to peewee orm classes
from typing import Dict


def payload(data: Dict) -> Dict:
    return {
        "current_git_head": data.get("current_git_head"),
        "release_git_head": data.get("release_git_head"),
        "repository": data.get("repository"),
        "version": data.get("version"),
    }


def create(data: Dict) -> Dict:
    return {
        "file": data.get("file"),
    }
