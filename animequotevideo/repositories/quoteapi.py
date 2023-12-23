import requests

import logging

from animequotevideo.models.quote import Quote
from animequotevideo.repositories.quotecache import QuoteCache
from animequotevideo.repositories.quoterepository import QuoteRepository

class QuoteApi(QuoteRepository):
    def __init__(self) -> None:
        super().__init__()
        
        self.url = "https://animechan.xyz/api"

    def randomQuote(self) -> Quote:
        logging.info(f"get quote on {self.url}/random")

        response = requests.get(f"{self.url}/random")

        try:
            data = response.json()

            quote = Quote(
                anime = data.get("anime"),
                character = data.get("character"),
                quote = data.get("quote"),
            )

            with QuoteCache() as cache: 
                if not cache.exitsQuote(quote):
                    cache.store(quote)

            return quote
        except:
            with QuoteCache() as cache: 
                return cache.randomQuote()

    def randomQuotes(self) -> list[Quote]:
        logging.info(f"get quotes on {self.url}/quotes")

        response = requests.get(f"{self.url}/quotes")

        try:
            data = response.json()

            quotes = []

            for quoteData in data:
                quote = Quote(
                    anime = quoteData.get("anime"),
                    character = quoteData.get("character"),
                    quote = quoteData.get("quote"),
                )

                with QuoteCache() as cache: 
                    if not cache.exitsQuote(quote):
                        cache.store(quote)

                quotes.append(quote)

            return quotes
        except:
            with QuoteCache() as cache:
                return cache.randomQuotes()
