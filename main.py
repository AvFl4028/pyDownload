from tkinter import *
from tkinter import ttk
from download_videos import *

# Values
options_media = ["mp4", "mp4", "mp3"]
options_file_path = ["Videos", "Videos", "Music", "Downloads"]
options_type_video = ["Video", "Video", "Playlist"]

path_file_video: str = f"C:/Users/{os.getlogin()}/Videos"
path_file_music: str = f"C:/Users/{os.getlogin()}/Music"
path_file_download: str = f"C:/Users/{os.getlogin()}/Downloads"

pathFiles: str = path_file_video

progress_bar_value: int = 0

# create new windows of tkinter
root = Tk()
root.resizable(width=False, height=False)
frm = ttk.Frame(root, padding=10)
frm.grid()

# main values for tkinter
root.geometry("275x125")
root.title("pyDownload")

# root.wm_iconbitmap("res/icon/pyDownload.ico")

# this function is for send all the data to the download videos function
def change_media_value():
    global pathFiles
    if option_default_file_path.get() == options_file_path[0]:
        pathFiles = path_file_video

    if option_default_file_path.get() == options_file_path[2]:
        pathFiles = path_file_music

    if option_default_file_path.get() == options_file_path[3]:
        pathFiles = path_file_download

    if option_default_media.get() == options_media[1]:
        mediaType = options_media[1]
    else:
        mediaType = options_media[2]

    resources_path = f"{pathFiles}/pyDownload"
    if yt_get_url.get() == "":
        return

    if not os.path.exists(resources_path):
        os.mkdir(resources_path)

    url_yt = yt_get_url.get()

    if option_default_type_file.get() == options_type_video[1]:
        download_video(url_yt, f"{mediaType}")
        move_resources(resources_path, f".{mediaType}")
    else:
        url_playlist = get_playlist(url_yt)
        print(f"Number of videos in the playlist: {len(url_playlist)}")
        for url in url_playlist:
            print(f"Url of video in playlist: {url}")
            download_video(url, mediaType)
            move_resources(resources_path, f".{mediaType}")

    print(pathFiles, " ", mediaType, " ", yt_get_url.get(), resources_path)

    yt_get_url.delete(0, END)

    return


# default option for selection of type of media
option_default_media = StringVar()
option_default_media.set(options_media[0])

# label for select format file
ttk.Label(frm, text="Select format file").grid(row=0, column=0)
options_file_get = ttk.OptionMenu(frm, option_default_media, *options_media)
options_file_get.grid(column=1, row=0)

# default option for selection of path for the downloads folder
option_default_file_path = StringVar()
option_default_file_path.set(options_file_path[0])

# label for select format file
ttk.Label(frm, text="Select download path").grid(row=1, column=0)
path_download_file_get = ttk.OptionMenu(frm, option_default_file_path, *options_file_path)
path_download_file_get.grid(column=1, row=1)

option_default_type_file = StringVar()
option_default_type_file.set(options_file_path[0])

# label for select format file
ttk.Label(frm, text="Select type of download").grid(row=2, column=0)
path_download_file_get = ttk.OptionMenu(frm, option_default_type_file, *options_type_video)
path_download_file_get.grid(column=1, row=2)

# label for url
ttk.Label(frm, text="Url").grid(row=3, column=0)

# create entre for yt url
yt_get_url = ttk.Entry(frm)
yt_get_url.grid(row=3, column=1)

# Button for start downloading the videos
ttk.Button(frm, text="Download", command=change_media_value).grid(row=4, column=0)

# start the window
root.mainloop()
