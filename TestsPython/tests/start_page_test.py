from pages.start_page import StartPage
from pages.main_menu_page import MainMenuPage
from tests.base_test import TestBase
import pytest


class TestStartPage(TestBase):
    def setup(self):
        self.start_page = StartPage(self.altdriver)
        self.start_page.load()
        self.main_menu_page = MainMenuPage(self.altdriver)

    @pytest.mark.run(order=1)
    def test_start_page_loaded_correctly(self):
        assert (self.start_page.is_displayed())

    @pytest.mark.run(order=2)
    def test_start_button_loads_main_menu(self):
        self.start_page.press_start()
        assert (self.main_menu_page.is_displayed())
