from abc import ABC
from abc import abstractmethod

from animequotevideo.models.quote import Quote

class QuoteRepository(ABC):
   @abstractmethod
   def randomQuote(self) -> Quote:
      raise NotImplementedError()
   
   @abstractmethod
   def randomQuotes(self) -> list[Quote]: 
      raise NotImplementedError()
   