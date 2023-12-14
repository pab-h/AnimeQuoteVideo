from moviepy.editor import VideoClip

from abc import ABC
from abc import abstractmethod

class Base(ABC):      
   @abstractmethod
   def build(self) -> VideoClip():
      raise NotImplementedError()