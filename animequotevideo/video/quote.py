from animequotevideo.models.quote import Quote
from animequotevideo.video.timer import Timer
from animequotevideo.video.needquote import NeedQuote

from moviepy.editor import VideoClip
from moviepy.editor import TextClip
from moviepy.editor import ColorClip
from moviepy.editor import CompositeVideoClip

class QuoteVideo(NeedQuote):
    def __init__(self, quote: Quote) -> None:
        super().__init__(quote)

    def build(self) -> VideoClip():
        quote = TextClip(
            f"\"{ self.quote.quote }\"", 
            color = "white", 
            fontsize = 25,
            method = "caption",
            size = (700, None),
            kerning = 1,
            font = "PlayfairDisplay-VariableFont_wght.ttf"
        )
        quote = quote.set_position("center")

        whose = TextClip(
            "Whose quote is that?",
            color = "orange",    
            fontsize = 50,
            font = "./assets/BungeeSpice-Regular.ttf",
            kerning = 1
        )
        whose = whose.set_position("top")
        whose = whose.margin(top = 100, opacity = 0)

        background = ColorClip((1280, 720), (34, 9, 44))

        timer = Timer().build()

        quoteVideo = CompositeVideoClip([ background, whose, quote, timer ])
        quoteVideo = quoteVideo.set_duration(10)
        quoteVideo = quoteVideo.set_fps(30)

        return quoteVideo