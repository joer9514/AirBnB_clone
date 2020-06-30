#!/usr/bin/python3
""" unique instance of FileStorage """

from models.engine.file_storage import File_storage

storage = File_storage()
storage.reload()
