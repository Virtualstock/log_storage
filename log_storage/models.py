import os, time

from private_storage.storage import private_storage

from django.conf import settings
from django.core.files.base import ContentFile
from django.db import models
from django.utils.encoding import smart_str


class BaseLog(models.Model):
    save_file = models.BooleanField(default=True)
    db_log_data = models.TextField()
    filename = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    prefix = ""
    suffix = ".log"

    class Meta:
        abstract = True

    def _get_desired_filename(self):
        path = getattr(settings, "LOG_DATA_DIR", "logs")
        filename = "{}_{}{}".format(
            self.prefix, time.strftime("%Y%m%d_%H%M%S_%f"), self.suffix
        )
        return os.path.join(path, filename)

    @property
    def log_data(self):
        if self.save_file:
            if self.filename:
                if private_storage.exists(self.filename):
                    file_path = self.filename
                else:
                    # Backwards compatability with 0.7.0
                    path = getattr(settings, "LOG_DATA_DIR", "logs")
                    file_path = os.path.join(path, self.filename)
                with private_storage.open(file_path, "rb") as f:
                    return f.read().decode("utf-8")
            else:
                return u""
        else:
            return self.db_log_data or u""

    _handler = None

    def make_file_handler(self):
        from logging import StreamHandler

        class FileStream(object):
            def __init__(stream):
                stream.contents = ContentFile(b"")
                stream.contents.open("wb")

            def write(stream, data):
                stream.contents.write(smart_str(data).encode(("utf-8")))

        class FileStreamHandler(StreamHandler):
            def close(handler):
                handler.stream.contents.seek(0)
                self.filename = private_storage.save(
                    self._get_desired_filename(), handler.stream.contents
                )
                super(FileStreamHandler, handler).close()

        return FileStreamHandler(FileStream())

    def make_db_handler(self):
        from logging import StreamHandler

        self.db_log_data = self.db_log_data or u""

        class DbStream(object):
            def write(stream, data):
                self.db_log_data += data

            def flush(stream):
                self.save()

            close = flush

        return StreamHandler(DbStream())

    @property
    def formatter(self):
        from logging import Formatter

        return Formatter("%(asctime)s   %(levelname)s   %(name)s   %(message)s")

    def make_handler(self):
        if self.save_file:
            handler = self.make_file_handler()
        else:
            handler = self.make_db_handler()
        handler.formatter = self.formatter
        return handler

    def __enter__(self):
        import logging

        self._handler = self.make_handler()
        logging.root.addHandler(self._handler)

    def __exit__(self, *tpl):
        import logging

        logging.root.removeHandler(self._handler)
        self._handler.close()
        self._handler = None
        self.save()


class Log(BaseLog):
    pass
