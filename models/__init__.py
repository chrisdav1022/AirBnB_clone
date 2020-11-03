#!/usr/bin/python3
"""contenedor inicio"""
"""import base model and file storage"""

from models.engine.file_storage import FileStorage

"""storage to json"""
storage = FileStorage()
storage.reload()
