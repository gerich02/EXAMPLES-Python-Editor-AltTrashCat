import os
import sys
from alttester import AltDriver

sys.path.append(os.path.dirname(__file__))


class TestBase():
    plaform = os.getenv('TESTS_PLATFORM')

    def setup_class(cls):
        print("In Base Test")
        cls.altdriver = AltDriver()

    def teardown_class(cls):
        cls.altdriver.stop()
