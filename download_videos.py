# this file is for the functions for download the videos
from resources import *
import os

try:
    from pytube import Playlist, YouTube
    from art import *
    from moviepy.editor import *

except Exception:
    os.system("pip install pytube")
    os.system("pip install art")
    os.system("pip install moviepy")


def get_playlist(playlists):
    urls = []
    playlist_url = Playlist(playlists)
    for url in playlist_url:
        urls.append(url)
    return urls


def download_video(url, type_file="mp4"):
    try:
        # Crear un objeto YouTube
        video = YouTube(url)

        # Seleccionar el formato de mayor resolución disponible para descargar
        video_stream = video.streams.get_highest_resolution()

        # Descargar el video en el directorio actual
        video_stream.download()
        print(f"video descargado: {video_stream.title}")

        if type_file == "mp4":
            return

        convert_to_mp3()
        delete_videos = filter_for_extension(".mp4")
        for delete in delete_videos:
            os.remove(delete)
    except Exception as e:
        print('Error al descargar el video:', str(e))


def convert_to_mp3():
    i = 0
    mp4_files_name = filter_for_extension(".mp4")
    for mp4 in mp4_files_name:
        i += 1
        videoClip = VideoFileClip(mp4)
        audioclip = videoClip.audio
        audioclip.write_audiofile(f"{mp4}.mp3")
        audioclip.close()
        videoClip.close()
