import requests

from animequotevideo.models.quote import Quote
from animequotevideo.repositories.quotecache import QuoteCache

class QuoteApi:
    def __init__(self) -> None:
        self.url = "https://animechan.xyz/api"

    def randomQuote(self) -> Quote:
        response = requests.get(f"{self.url}/random")

        with QuoteCache() as cache: 
            try:
                data = response.json()

                quote = Quote(
                    anime = data.get("anime"),
                    character = data.get("character"),
                    quote = data.get("quote"),
                )

                if not cache.exitsQuote(quote):
                    cache.store(quote)

                return quote
            except:
                return cache.randomQuote()

    def randomQuotes(self) -> list[Quote]:
        response = requests.get(f"{self.url}/quotes")

        with QuoteCache() as cache: 
            try:
                data = response.json()

                quotes = []

                for quoteData in data:
                    quote = Quote(
                        anime = quoteData.get("anime"),
                        character = quoteData.get("character"),
                        quote = quoteData.get("quote"),
                    )

                    if not cache.exitsQuote(quote):
                        cache.store(quote)

                    quotes.append(quote)

                return quotes
            except:
                return cache.randomQuotes()
