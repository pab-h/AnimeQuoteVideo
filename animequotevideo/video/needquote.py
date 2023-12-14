from animequotevideo.video.base import Base
from animequotevideo.models.quote import Quote

class NeedQuote(Base):
    def __init__(self, quote: Quote) -> None:
        super().__init__()

        self.quote = quote
        