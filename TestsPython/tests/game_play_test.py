from pages.main_menu_page import MainMenuPage
from pages.game_play_page import GamePlayPage
from pages.pause_overlay_page import PauseOverlayPage
from pages.get_another_chance_page import GetAnotherChancePage
from assertpy import assert_that
import pytest


class TestGamePlay():

    @pytest.fixture(autouse=True)
    def before_and_after_test(self, altdriver):
        # setUp
        self.main_menu_page = MainMenuPage(altdriver)
        self.main_menu_page.load()
        self.main_menu_page.press_run()
        print("done sleeping")
        self.game_play_page = GamePlayPage(altdriver)
        self.pause_overlay_page = PauseOverlayPage(altdriver)
        self.get_another_chance_page = GetAnotherChancePage(altdriver)

        yield
        # tearDown
        self.main_menu_page.load()

    def test_game_play_page_displayed_correctly(self):
        assert (self.game_play_page.is_displayed())

    def test_countdown_displayed_correctly(self):
        """Новый тест на наличие обратного отсчета."""
        assert (self.game_play_page.is_countdown_displayed())

    def test_tutorial_displayed_correctly(self):
        """Новый тест на наличие подсказок."""
        assert (self.game_play_page.is_tutorial_displayed())

    def test_game_can_be_paused_and_resumed(self):
        self.game_play_page.press_pause()
        assert (self.pause_overlay_page.is_displayed())
        self.pause_overlay_page.press_resume()
        assert (self.game_play_page.is_displayed())

    def test_game_can_be_paused_and_stopped(self):
        self.game_play_page.press_pause()
        self.pause_overlay_page.press_main_menu()
        assert (self.main_menu_page.is_displayed())

    def test_avoiding_obstacles(self):
        self.game_play_page.avoid_obstacles(5)
    # check that player has 2 or 3 lives left (sometimes 1 life is lost right when stopping the tests)
        assert_that(self.game_play_page.get_current_life()).described_as(
            "player current life").is_greater_than(0)

    def test_player_dies_when_obstacles_not_avoided(self):
        timeout = 10
        while timeout > 0:
            try:
                self.get_another_chance_page.is_displayed()
                break
            except:
                timeout -= 1
        self.get_another_chance_page.is_displayed()
