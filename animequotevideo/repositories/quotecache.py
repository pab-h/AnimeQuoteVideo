import logging

import sqlite3

from sqlite3 import Cursor

from typing import Optional

from animequotevideo.models.quote import Quote
from animequotevideo.repositories.quoterepository import QuoteRepository

class QuoteCache(QuoteRepository):
    def __init__(self) -> None:
        super().__init__()

        self.connection = sqlite3.connect("./quote-cache.db")
        self.cursor: Optional[Cursor] = None

    def __enter__(self):
        self.cursor = self.connection.cursor()

        sql = "CREATE TABLE IF NOT EXISTS quotes(anime, character, quote);"

        self.cursor.execute(sql)
        self.connection.commit()

        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.connection.commit()
        self.cursor.close()

    def store(self, quotes: Quote | list[Quote]) -> None:
        logging.info(f"saving quotes on cache")

        if isinstance(quotes, Quote):
            quotes = [quotes]
 
        sql = "INSERT INTO quotes VALUES (?, ? , ?);"

        params = []

        for quote in quotes:
            param = (quote.anime, quote.character, quote.quote)
            params.append(param)

        self.cursor.executemany(sql, params)
        self.connection.commit()

    def exitsQuote(self, quote: Quote) -> bool:
        logging.info(f"checking if a quote exists on cache")

        sql = """
            SELECT * FROM quotes 
            WHERE 
                anime = ? AND 
                character = ? AND 
                quote = ?;
        """

        params = (quote.anime, quote.character, quote.quote)

        result = self.cursor.execute(sql, params)

        return bool(result.fetchone())

    def randomQuote(self) -> Quote:
        logging.info(f"get a random quote on cache")

        sql = "SELECT * FROM quotes ORDER BY RANDOM() LIMIT 1;"

        result = self.cursor.execute(sql)
        data = result.fetchone()

        if not data:
            raise Exception("has not quote cached")
        
        return Quote(
            anime = data[0], 
            character = data[1], 
            quote = data[2]
        )

    def randomQuotes(self) -> list[Quote]:
        logging.info(f"get a random quotes on cache")

        sql = "SELECT * FROM quotes ORDER BY RANDOM() LIMIT 10;"

        result = self.cursor.execute(sql)

        quotes = []

        for data in result.fetchall():
            quote = Quote(
                anime = data[0], 
                character = data[1], 
                quote = data[2]
            )

            quotes.append(quote)

        return quotes
