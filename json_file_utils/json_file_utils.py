"""
Functions for working with JSON files
"""

from pathlib import Path
import json
import logging
import os
import tempfile

logger = logging.getLogger(__name__)


def read_json_file(file_path: str | Path, *, encoding: str = "utf-8") -> dict | list | str | int | float | bool | None:
    """
    Reads and parses a JSON file.

    Args:
        file_path: Path to the JSON file.
        encoding: Encoding used to read the file.

    Returns:
        The parsed JSON data.
    """
    file_path = Path(file_path)
    if not file_path.exists():
        raise FileNotFoundError(file_path)
    data = json.loads(file_path.read_text(encoding=encoding))
    logger.debug("Successfully read data from %s", file_path)
    return data


def write_json_file(file_path: str | Path, data: dict | list | str | int | float | bool | None, *, encoding: str = "utf-8", indent: int | str | None = 4, ensure_ascii: bool = True) -> None:
    """
    Writes data to a JSON file atomically.

    Args:
        file_path: Path to the JSON file.
        data: Data to write to the file.
        encoding: Encoding used to write the file.
        indent: Indentation level or string used to format the JSON.
        ensure_ascii: If True, escape non-ASCII characters.
    """
    file_path = Path(file_path)
    temp_file_path: Path | None = None

    try:
        if not file_path.parent.exists():
            file_path.parent.mkdir(parents=True, exist_ok=True)
            logger.debug("Created %s", file_path.parent)

        with tempfile.NamedTemporaryFile(mode='w', dir=str(file_path.parent), encoding=encoding, suffix=".tmp", delete=False) as tf:
            temp_file_path = Path(tf.name)
            json.dump(data, tf, indent=indent, ensure_ascii=ensure_ascii)
            tf.flush()
            os.fsync(tf.fileno())

        temp_file_path.replace(file_path)
        logger.debug("Successfully saved to %s", file_path)

    finally:
        if temp_file_path is not None:
            try:
                temp_file_path.unlink(missing_ok=True)
            except OSError:
                logger.exception("Failed to clean up temporary file %s", temp_file_path)


def load_config(file_path: str | Path, *, encoding: str = "utf-8") -> dict | list | str | int | float | bool | None:
    """
    Alias for read_json_file, specifically for configuration files.
    """
    return read_json_file(file_path, encoding=encoding)


def save_config(file_path: str | Path, config_data: dict | list | str | int | float | bool | None, *, encoding: str = "utf-8", indent: int | str | None = 4, ensure_ascii: bool = True) -> None:
    """
    Alias for write_json_file, specifically for configuration files.
    """
    write_json_file(file_path, config_data, encoding=encoding, indent=indent, ensure_ascii=ensure_ascii)


def load_cache(file_path: str | Path, *, encoding: str = "utf-8") -> dict | list | str | int | float | bool | None:
    """
    Alias for read_json_file, specifically for cache files.
    """
    return read_json_file(file_path, encoding=encoding)


def save_cache(file_path: str | Path, cache_data: dict | list | str | int | float | bool | None, *, encoding: str = "utf-8", indent: int | str | None = 4, ensure_ascii: bool = True) -> None:
    """
    Alias for write_json_file, specifically for cache files.
    """
    write_json_file(file_path, cache_data, encoding=encoding, indent=indent, ensure_ascii=ensure_ascii)
