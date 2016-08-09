import django.test as unittest

from logs.models import Log

class TestLogRecordingToFile(unittest.TestCase):
    def setUp(self):
        import logging
        self.log = Log(save_file=True)
        self.logger = logging.getLogger('test.'+__name__)

    def test_logging(self):
        with self.log:
            self.logger.info("info")
            self.logger.debug("debug")
        self.assertIn(u"info", self.log.log_data)
        self.assertIn(u"debug", self.log.log_data)
        self.assertIn(u"test.logs.tests", self.log.log_data)

    def test_persistence(self):
        with self.log:
            self.logger.info("info")
            self.logger.debug("debug")
        self.log = Log.objects.get(pk=self.log.pk)
        self.assertIn(u"info", self.log.log_data)
        self.assertIn(u"debug", self.log.log_data)
        self.assertIn(u"test.logs.tests", self.log.log_data)




class TestLogRecordingToDb(unittest.TestCase):
    def setUp(self):
        import logging
        self.log = Log(save_file=False)
        self.logger = logging.getLogger('test.'+__name__)

    def test_logging(self):
        with self.log:
            self.logger.info("info")
            self.logger.debug("debug")
        self.assertIn(u"info", self.log.log_data)
        self.assertIn(u"debug", self.log.log_data)
        self.assertIn(u"test.logs.tests", self.log.log_data)

    def test_persistence(self):
        with self.log:
            self.logger.info("info")
            self.logger.debug("debug")
        self.log = Log.objects.get(pk=self.log.pk)
        self.assertIn(u"info", self.log.log_data)
        self.assertIn(u"debug", self.log.log_data)
        self.assertIn(u"test.logs.tests", self.log.log_data)



