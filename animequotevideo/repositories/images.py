from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from animequotevideo.models.quote import Quote

class Images:
    def __init__(self) -> None:
        self.driver = Chrome()
        self.url = "https://www.google.com/imghp"
        self.script = "return [... document.querySelectorAll(\"img[alt]\")].filter(img => img.alt)[2].src"

    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.driver.close()

    def search(self, term: str) -> None:
        self.driver.get(self.url)

        ActionChains(self.driver)\
            .send_keys(term)\
            .send_keys(Keys.ENTER)\
            .perform()

    def getCharacter(self, quote: Quote):
        self.search(f"{ quote.character } { quote.anime }")

        src = self.driver.execute_script(self.script)

        quote.characterImage = src

    def getAnimeWallpaper(self, quote: Quote):
        self.search(f"{ quote.anime } Wallpaper")
        
        src = self.driver.execute_script(self.script)

        quote.animeImage = src
