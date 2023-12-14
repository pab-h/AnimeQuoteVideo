from moviepy.editor import VideoClip
from animequotevideo.repositories.images import Images
from animequotevideo.models.quote import Quote
from abc import ABC
from abc import abstractmethod


class Default(ABC):
   def __init__(self, quote: Quote) -> None:
      self.quote = quote
      self.images = Images()
      
   @abstractmethod
   def build(self) -> VideoClip():
      raise NotImplementedError()
   