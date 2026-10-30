import yt_dlp

ydl_opts = {
    'format': 'bestaudio/best',
    # 'ffmpeg_location': r'C:\ffmpeg\bin',
    'postprocessors': [
        {
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }
    ],
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
  ydl.download(['https://youtu.be/nyDvaivsBrg?si=T6FoXR88Qy-blqS5'])

  # WHERET TO PLACE YOUR MUSIC AFTER downloading
  # CHECK HOW TO DO META DATA EG ALBUM,THE YEAR,IMAGE
  # I need to learn more on how to learn