from django.db import models


class BaseLog(models.Model):
    save_file = models.BooleanField(default=True)
    db_log_data = models.TextField()
    filename = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    prefix = ''
    suffix = '.log'

    class Meta:
        abstract = True

    def get_filename(self):
        import os, time, random
        from django.conf import settings
        root = getattr(settings, 'PRIVATE_STORAGE_ROOT')
        assert root, "PRIVATE_STORAGE_ROOT setting not set"
        path = getattr(settings, 'LOG_DATA_DIR', 'logs')
        if not self.filename:
            self.filename = '_'.join(filter(bool, [self.prefix,
                    time.strftime('%Y%m%d_%H%M%S'),
                    ''.join([random.choice('0123456789') for i in range(0, 5)]),
                    self.suffix]))
        filename = self.filename
        path = os.path.join(root, path)
        if not os.path.isdir(path):
            os.makedirs(path)
        return os.path.join(root, path, filename)

    @property
    def log_data(self):
        if self.save_file:
            if self.filename:
                with open(self.get_filename(), 'rb') as f:
                    return f.read().decode('utf-8')
            else:
                return u''
        else:
            return self.db_log_data or u''

    _handler = None

    def make_file_handler(self):
        from logging import FileHandler
        return FileHandler(self.get_filename())

    def make_db_handler(self):
        from logging import StreamHandler
        self.db_log_data = self.db_log_data or u''
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
        return Formatter('%(asctime)s   %(levelname)s   %(name)s   %(message)s')

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
        self._handler.flush()
        self._handler = None
        self.save()


class Log(BaseLog):
    pass
