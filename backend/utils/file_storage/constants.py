from enum import Enum


class FileStorageKeys:
    PERMANENT_REMOTE_STORAGE = "PERMANENT_REMOTE_STORAGE"
    TEMPORARY_REMOTE_STORAGE = "TEMPORARY_REMOTE_STORAGE"


class FileStorageType(Enum):
    PERMANENT = "permanent"
    TEMPORARY = "temporary"


class FileStorageConstants:
    PROMPT_STUDIO_FILE_PATH = "PROMPT_STUDIO_FILE_PATH"
    REMOTE_PROMPT_STUDIO_FILE_PATH = "REMOTE_PROMPT_STUDIO_FILE_PATH"
