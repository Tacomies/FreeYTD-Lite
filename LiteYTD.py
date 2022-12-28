from tkinter import *
from pytube import YouTube
from webbrowser import open
window = Tk()


def download_video(link):
    while True:
        try:
            video = YouTube(link)
            video = video.streams.get_highest_resolution()
            video.download("YTD Downloads")
            break
        except:
            continue

def setup():
    wd = window.winfo_screenwidth()/2
    hd = window.winfo_screenheight()/2
    window.wm_attributes("-transparentcolor", "#DAF7A6")
    window.geometry('%dx%d+%d+%d' % (150, 45, wd-125, hd-125))
    window.configure(bg="#DAF7A6")
    linkfield = Entry(window)
    Label(window, text="Link").grid(row=0)
    linkfield.grid(row=0, column=1)
    btn = Button(window, text="DOWNLOAD", command=lambda: download_video(linkfield.get()))
    btn.place(x=0, y=20)
    
def main():
    setup()
    mainloop()

main()