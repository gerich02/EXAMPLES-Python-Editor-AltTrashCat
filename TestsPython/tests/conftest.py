import os
import sys
import pytest
from alttester import AltDriver
sys.path.append(os.path.dirname(__file__))

platform = None


@pytest.fixture(scope="session")
def altdriver():
    altdriver = AltDriver()

    print("altdriver started")

    yield altdriver

    altdriver.stop()
