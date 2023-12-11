import requests

from animequotevideo.models.quote import Quote

class QuoteApi:
    def __init__(self) -> None:
        self.url = "https://animechan.xyz/api"

    def randomQuote(self) -> Quote:
        response = requests.get(f"{self.url}/random")
        data = response.json()

        return Quote(
            anime = data.get("anime"),
            character = data.get("character"),
            quote = data.get("quote"),
        )

    def randomQuotes(self) -> list[Quote]:
        response = requests.get(f"{self.url}/quotes")
        data = response.json()

        quotes = []

        for quote in data:
            quotes.append(Quote(
                anime = quote.get("anime"),
                character = quote.get("character"),
                quote = quote.get("quote"),
            ))

        return quotes
