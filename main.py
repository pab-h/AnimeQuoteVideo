from animequotevideo.video.video import Video

from animequotevideo.repositories.quotecache import QuoteCache

import logging

logging.basicConfig(
    format = "[%(levelname)s] %(asctime)s %(message)s", 
    datefmt = "%H:%M:%S", 
    level = logging.INFO
)

with QuoteCache() as cache:
    Video(cache).\
        build().\
        write_videofile("resultado.mp4")
