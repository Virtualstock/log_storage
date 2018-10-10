import logging


import django.test as unittest

from log_storage.models import Log


class TestLogRecordingToFile(unittest.TestCase):
    def setUp(self):
        self.log = Log(save_file=True)
        self.logger = logging.getLogger('test.'+__name__)
        self.logger.setLevel(logging.DEBUG)

    def test_logging(self):
        with self.log:
            self.logger.info("info")
            self.logger.debug("debug")
        self.assertIn(u"info", self.log.log_data)
        self.assertIn(u"debug", self.log.log_data)
        self.assertIn(u"test.log_storage.tests", self.log.log_data)

    def test_persistence(self):
        with self.log:
            self.logger.info("info")
            self.logger.debug("debug")
        self.log = Log.objects.get(pk=self.log.pk)
        self.assertIn(u"info", self.log.log_data)
        self.assertIn(u"debug", self.log.log_data)
        self.assertIn(u"test.log_storage.tests", self.log.log_data)

    def test_log_data(self):
        """Test that calling log.log_data before logging anything won't throw error."""
        self.assertEqual('', self.log.log_data)


class TestLogRecordingToDb(unittest.TestCase):
    def setUp(self):
        self.log = Log(save_file=False)
        self.logger = logging.getLogger('test.'+__name__)
        self.logger.setLevel(logging.DEBUG)

    def test_logging(self):
        with self.log:
            self.logger.info("info")
            self.logger.debug("debug")
        self.assertIn(u"info", self.log.log_data)
        self.assertIn(u"debug", self.log.log_data)
        self.assertIn(u"test.log_storage.tests", self.log.log_data)

    def test_persistence(self):
        with self.log:
            self.logger.info("info")
            self.logger.debug("debug")
        self.log = Log.objects.get(pk=self.log.pk)
        self.assertIn(u"info", self.log.log_data)
        self.assertIn(u"debug", self.log.log_data)
        self.assertIn(u"test.log_storage.tests", self.log.log_data)

    def test_log_data(self):
        """Test that calling log.log_data before logging anything won't throw error."""
        self.assertEqual('', self.log.log_data)
