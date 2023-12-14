from animequotevideo.models.quote import Quote

from animequotevideo.video.needquote import NeedQuote
from animequotevideo.video.quote import QuoteVideo
from animequotevideo.video.answer import Answer

from moviepy.editor import VideoClip
from moviepy.editor import concatenate_videoclips

class Quiz(NeedQuote):
    def __init__(self, quote: Quote) -> None:
        super().__init__(quote)

    def build(self) -> VideoClip:
        quote = QuoteVideo(self.quote).build()
        answer = Answer(self.quote).build()

        return concatenate_videoclips([quote, answer])