from moviepy.editor import VideoClip
from moviepy.editor import CompositeVideoClip
from moviepy.editor import AudioFileClip
from moviepy.editor import concatenate_videoclips

from moviepy.audio.fx.audio_loop import audio_loop

from animequotevideo.video.base import Base
from animequotevideo.video.authorscolumn import AuthorsColumn
from animequotevideo.video.quiz import Quiz

from animequotevideo.repositories.quoterepository import QuoteRepository

class Video(Base):
    def __init__(self, repo: QuoteRepository) -> None:
        super().__init__()

        self.repo = repo
        self.audio = "./animequotevideo/assets/Path-to-Follow.mp3"

    def build(self) -> VideoClip:
        quotes = self.repo.randomQuotes()

        # ToDo: Validar o tamanho da citacao

        authorcolumn = AuthorsColumn(quotes)

        clips = []

        for quote in quotes:
            quiz = Quiz(quote).build()
            tmp = CompositeVideoClip([ quiz, authorcolumn.build() ])
            next(authorcolumn)

            clips.append(tmp)

        video = concatenate_videoclips(clips) 
        
        audio = AudioFileClip(self.audio)
        audio = audio_loop(audio, duration = video.duration)
        
        video = video.set_audio(audio)

        return video
