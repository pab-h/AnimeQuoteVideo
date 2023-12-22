from animequotevideo.video.video import Video

from animequotevideo.repositories.quotecache import QuoteCache

with QuoteCache() as cache:
    Video(cache).\
        build().\
        write_videofile("resultado.mp4")
