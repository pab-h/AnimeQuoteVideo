import logging

from numpy import array

from animequotevideo.models.quote import Quote
from animequotevideo.video.needquote import NeedQuote
from animequotevideo.repositories.images import Images

from PIL import Image
from PIL import ImageFilter

from moviepy.editor import ImageClip
from moviepy.editor import TextClip
from moviepy.editor import CompositeVideoClip
from moviepy.editor import VideoClip


class Answer(NeedQuote):
    def __init__(self, quote: Quote) -> None:
        super().__init__(quote)

    def build(self) -> VideoClip:
        logging.info("building answer clip")

        if not self.quote.animeImage:
            with Images() as images: 
                images.getAnimeWallpaper(self.quote)

        if not self.quote.characterImage:
            with Images() as images: 
                images.getCharacter(self.quote)

        background = Image.open(self.quote.animeImage)
        background = background.convert("RGB")
        background = background.resize((1280, 720))
        background = background.filter(ImageFilter.BoxBlur(10)) 
        background = ImageClip(array(background))

        photo = Image.open(self.quote.characterImage)
        photo = photo.resize((400, 400))
        photo = ImageClip(array(photo))
        photo = photo.set_position("center")

        name = TextClip(
            self.quote.character,
            color = "white",
            fontsize = 75,
            kerning = 1,
            stroke_color = "blue",
            stroke_width = 1
        )
        name = name.margin(bottom = 75, opacity = 0)
        name = name.set_position("bottom")

        video = CompositeVideoClip([ background, photo, name ])
        video = video.set_duration(5)
        video = video.set_fps(1)

        return video
    