import os
from moviepy.editor import *
video = VideoFileClip(os.path.join("Aaron Smith - Dancin (KRONO REMIX) Cover  @brunette_e_.mp4"))
video.audio.write_audiofile(os.path.join("Dancin.mp3"))
