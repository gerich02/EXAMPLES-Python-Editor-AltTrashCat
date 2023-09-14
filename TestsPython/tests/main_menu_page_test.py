import pytest
from pages.main_menu_page import MainMenuPage


class TestMainMenuPage():
    @pytest.fixture(autouse=True)
    def setup_method(self, altdriver):
        self.main_menu_page = MainMenuPage(altdriver)
        self.main_menu_page.load()

    def test_main_menu_page_loaded_correctly(self):
        assert (self.main_menu_page.is_displayed())
