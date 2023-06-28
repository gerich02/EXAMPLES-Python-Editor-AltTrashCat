import os
import sys
from alttester import AltDriver

sys.path.append(os.path.dirname(__file__))


class TestBase():
    plaform = os.getenv('TESTS_PLATFORM')

    @classmethod
    def setup_class(cls):
        print("In Base Test")
        cls.altdriver = AltDriver()

    @classmethod
    def teardown_class(cls):
        cls.altdriver.stop()
