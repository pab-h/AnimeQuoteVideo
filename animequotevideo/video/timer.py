from animequotevideo.models.quote import Quote
from animequotevideo.video.base import Base

from moviepy.editor import VideoClip
from moviepy.editor import ImageSequenceClip

from moviepy.video.fx.fadein import fadein
from moviepy.video.fx.fadeout import fadeout

from PIL import Image
from PIL import ImageDraw

from numpy import array

class Timer(Base):
    def __init__(self) -> None:
        super().__init__()

    def create_timer_frame(self, t: int, duration: int) -> Image.Image:
        bar_width = 400

        frame = Image.new(mode = "RGBA", size = (bar_width, 25))

        drawer = ImageDraw.Draw(frame)

        progress = t / duration

        bar_progress = int(bar_width * progress)

        drawer.rounded_rectangle(
            xy = (0, 0, bar_width, 25), 
            radius = 19,
            outline = "white",
            width = 3        
        )

        drawer.rounded_rectangle(
            xy = (0, 0, bar_progress, 25), 
            radius = 19,
            fill = "yellow" ,
            outline = "white",
            width = 3
        )

        return frame

    def create_timer(self, duration: int):
        frames = []
        
        fps = 60

        for t in range(duration * fps):
            frame = self.create_timer_frame(t, duration * fps)
            frame = array(frame)

            frames.append(frame)

        return ImageSequenceClip(
            frames, 
            fps = fps, 
            durations = duration * fps
        ) 

    def build(self) -> VideoClip:
        timer = self.create_timer(10)
        timer = timer.margin(bottom = 75, opacity=0)
        timer = timer.set_position("bottom")
        timer = fadein(timer, 5)
        timer = fadeout(timer, 2)

        return timer