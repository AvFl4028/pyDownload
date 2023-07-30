# this file is for the functions for download the videos
from resources import *
import os
try:
    from pytube import Playlist, YouTube
    from art import *

except Exception:
    os.system("pip install pytube")
    os.system("pip install art")


def get_playlist(playlists, path_resources):
    urls = []
    playlist_url = Playlist(playlists)
    for url in playlist_url:
        urls.append(url)
        print(url)
        download_video(url)
        move_resources(path_resources)
    return urls


def download_video(url):
    try:
        # Crear un objeto YouTube
        video = YouTube(url)

        # Seleccionar el formato de mayor resolución disponible para descargar
        video_stream = video.streams.get_highest_resolution()

        # Descargar el video en el directorio actual
        video_stream.download()
        print(f"video descargado: {video_stream.title}")
    except Exception as e:
        print('Error al descargar el video:', str(e))

