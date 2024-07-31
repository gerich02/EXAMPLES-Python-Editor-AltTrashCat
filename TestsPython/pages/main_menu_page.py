from pages.base_page import BasePage
from alttester import By


class MainMenuPage(BasePage):

    def __init__(self, altdriver):
        BasePage.__init__(self, altdriver)

    def load(self):
        self.altdriver.load_scene('Main')

    @property
    def store_button(self):
        return self.altdriver.wait_for_object(By.NAME, 'StoreButton', timeout=2)
    
    @property
    def leader_board_button(self):
        return self.altdriver.wait_for_object(By.NAME, 'OpenLeaderboard', timeout=2)

    @property
    def settings_button(self):
        return self.altdriver.wait_for_object(By.NAME, 'SettingButton', timeout=2)

    @property
    def mission_button(self):
        return self.altdriver.wait_for_object(By.NAME, 'MissionButton', timeout=2)

    @property
    def run_button(self):   
        return self.altdriver.wait_for_object(By.NAME, 'StartButton', timeout=2)

    @property
    def character_name(self):
        return self.altdriver.wait_for_object(By.NAME, 'CharName', timeout=2)

    @property
    def theme_name(self):
        return self.altdriver.wait_for_object(By.NAME, 'ThemeZone', timeout=2)
    
    @property
    def tutorial_top(self):
        return self.altdriver.wait_for_object(By.PATH, '/UICamera/Loadout/TutorialOverlay/BlockerTop', timeout=2)
    
    @property
    def tutorial_bottom(self):
        return self.altdriver.wait_for_object(By.PATH, '/UICamera/Loadout/TutorialOverlay/BlockerBottom', timeout=2)
    
    @property
    def tutorial_text(self):
        return self.altdriver.wait_for_object(By.PATH, '/UICamera/Loadout/TutorialOverlay/TutorialText/Text', timeout=2)
    
    @property
    def tutorial_image(self):
        return self.altdriver.wait_for_object(By.PATH, '/UICamera/Loadout/TutorialOverlay/TutorialText/Image', timeout=2)

    def is_displayed(self):
        return self.store_button \
            and self.leader_board_button \
            and self.settings_button \
            and self.mission_button \
            and self.run_button \
            and self.character_name \
            and self.theme_name
    
    def is_tutorial_displayed(self):
        return self.tutorial_top \
            and self.tutorial_bottom \
            and self.tutorial_text \
            and self.tutorial_text

    def press_run(self):
        self.run_button.tap()
