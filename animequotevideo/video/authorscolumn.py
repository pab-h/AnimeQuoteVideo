from moviepy.editor import VideoClip
from moviepy.editor import ColorClip
from moviepy.editor import ImageClip
from moviepy.editor import CompositeVideoClip

from animequotevideo.video.base import Base
from animequotevideo.models.quote import Quote
from animequotevideo.repositories.images import Images

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFilter

from numpy import array
from numpy import dstack

class AuthorsColumn(Base):
    def __init__(self, quotes: list[Quote]) -> None:
        super().__init__()
        
        self.quotes = quotes
        self.current = -1

    def __iter__(self):
        return self
 
    def __next__(self): 
        if self.current == len(self.quotes):
            raise StopIteration()

        self.current += 1

        return self

    def prepareImage(self, quote: Quote, blur = True) -> ImageClip:
        character = Image.open(quote.characterImage)
        character = character.resize((60, 60))

        alpha = Image.new("L", character.size, 0)

        drawer = ImageDraw.Draw(alpha)

        shape = [0, 0, character.size[0] - 1, character.size[1] - 1]

        drawer.pieslice(
            shape,
            start = 0,
            end = 360,
            fill = 255
        )

        if blur:
            character = character.filter(ImageFilter.BoxBlur(5))

        character = dstack([array(character), array(alpha)])

        return ImageClip(character)

    def build(self) -> VideoClip:
        for quote in self.quotes:
            if not quote.characterImage:
                with Images() as images:
                    images.getCharacter(quote)

        background = ColorClip((1280, 720), (0, 0, 0, 0))

        clips = [background]

        y = 15
        offsetY = 10
        offsetX = 15

        for i, quote in enumerate(self.quotes):
            character = self.prepareImage(quote, i >= self.current)
            character = character.set_position((offsetX, y))

            height = character.img.shape[0]
            y += height + offsetY 

            clips.append(character)

        video = CompositeVideoClip(clips)
        video = video.set_duration(10)
        video = video.set_fps(1)

        return video
    