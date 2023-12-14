from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from animequotevideo.models.quote import Quote
from uuid import uuid4 as uuid
from os import makedirs
from base64 import b64decode
from requests import get
from PIL import Image
from io import StringIO

class Images:
    def __init__(self) -> None:
        options = ChromeOptions()
        options.add_argument("--headless=new")
        self.driver = Chrome(options)
        self.url = "https://www.google.com/imghp"
        self.script = "return [... document.querySelectorAll(\"img[alt]\")].filter(img => img.alt)[2].src"
        makedirs("./.tmp", exist_ok = True)

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

    def downloadImage(self, src: str) -> str:
        filename = f".tmp/{ uuid() }.png"

        if "base64," in src:
            data = src.split("base64,").pop()
            data = b64decode(data)

            with open(filename, "wb") as file:
                file.write(data)
        
        if "http" in src: 
            response = get(src)
            Image\
                .open(StringIO(response.content))\
                .save(filename)

        return filename

    def getCharacter(self, quote: Quote):
        self.search(f"{ quote.character } { quote.anime }")

        src: str = self.driver.execute_script(self.script)

        filename = self.downloadImage(src)

        quote.characterImage = filename

    def getAnimeWallpaper(self, quote: Quote):
        self.search(f"{ quote.anime } Wallpaper")
        
        src: str = self.driver.execute_script(self.script)

        filename = self.downloadImage(src)

        quote.animeImage = filename
