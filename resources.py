import os
import shutil

mainPath = os.path.dirname(os.path.abspath(__file__))


def move_resources(move_resources_path, type_file =".mp4"):
    files_video = filter_for_extension(type_file)

    for video in files_video:
        shutil.move(video, move_resources_path)
    return


def filter_for_extension(extension):
    try:
        # Obtener una lista de archivos en la carpeta
        file = os.listdir(mainPath)

        # Filtrar los archivos por su extensión
        files_filter = [archivo for archivo in file if archivo.endswith(extension)]

        return files_filter
    except Exception as e:
        print(f"Error al filtrar los archivos: {str(e)}")
        return []
