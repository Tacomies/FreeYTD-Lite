from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from pytube import YouTube
import os
window = Tk()


def download_video(vid, path): #function for downloading Mp4 format
    while True: #Trying in loop because download is often failed for YouTube server reasons
        try:
            video = vid.streams.get_highest_resolution()
            video.download("downloads")
            messagebox.showinfo(title="Download successful", message=f"Video downloaded to\n{path}")
            break
        except:
            continue

def download_audio(aud, path): #function for downloading Mp3 format
    while True: #Trying in loop because download is often failed for YouTube server reasons
        try:
            audio = aud.streams.filter(only_audio=True).first()
            audio = audio.download("downloads")
            base, ext = os.path.splitext(audio)
            new_file = base + '.mp3'
            os.rename(audio, new_file)
            messagebox.showinfo(title="Download successful", message=f"Audio downloaded to\n{path}")
            break
        except:
            continue

def get_video(link): #Function for making sure YouTube link exists/works
    try:
        video = YouTube(link)
        return video
    except:
        messagebox.showerror(title="URL ERROR", message="Make sure that video URL is neither empty or invalid")

def selection(option, link): #Selecting output format
    path = os.getcwd()
    video = get_video(link)
    if video:
        match(option):
            case "Mp4":
                download_video(video, path)
            case "Mp3":
                download_audio(video, path)
            case _:
                messagebox.showerror(title="FORMAT ERROR", message="Select format!")

    
def setup(): #Function for setting up the GUI
    window.title("FreeYTD")
    wd = window.winfo_screenwidth()/2
    hd = window.winfo_screenheight()/2
    window.geometry('%dx%d+%d+%d' % (225, 45, wd-125, hd-125))
    window.resizable(False, False)
    linkfield = Entry(window, width=24)
    options = ["Mp4", "Mp3"]
    select = ttk.Combobox(window, value=options, width=5)
    select.place(x=175)
    Label(window, text="Link:").grid(row=0)
    linkfield.grid(row=0, column=1)
    btn = Button(window, text="DOWNLOAD", command=lambda: selection(select.get(), linkfield.get()))
    btn.place(x=0, y=20)
    tag = Label(window, text = "DC: Tacomies#2616")
    tag.config(font =("Courier", 10))
    tag.place(x=85, y=20)

def main(): #Main function for style reasons
    setup()
    mainloop()


if __name__ == "__main__":
    main()