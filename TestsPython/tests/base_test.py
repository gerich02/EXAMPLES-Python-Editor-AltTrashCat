import os
import sys
from alttester import AltDriver
import unittest

sys.path.append(os.path.dirname(__file__))


class TestBase(unittest.TestCase):
    plaform = os.getenv('TESTS_PLATFORM')
    
    @classmethod
    def setUpClass(cls):
        print("In Base Test")
        cls.altdriver = AltDriver()

    @classmethod    
    def tearDownClass(cls):
        cls.altdriver.stop()
