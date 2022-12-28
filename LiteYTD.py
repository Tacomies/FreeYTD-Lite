from tkinter import *
from tkinter import messagebox
from pytube import YouTube
from pathlib import Path
window = Tk()

#Main function for downloading video and catching errors during the process
def download_video(link):
    path = Path(__file__).with_name("downloads")
    if link:
        try:
            video = YouTube(link)
        except: #Catches invalid links
            messagebox.showerror(title="Link error", message="Invalid URL\nMake sure video exists")
            return None
        while True:
            try: #Retries download if YouTube server fails
                video = video.streams.get_highest_resolution()
                video.download(path)
                break
            except:
                continue
        messagebox.showinfo(title=None, message=f"Video downloaded to {path}")
    else: #Catches download attempt with no given URL
        messagebox.showerror(title="Link error", message="URL can't be empty")
#Function for setting up the GUI
def setup():
    window.title("FreeYTD")
    wd = window.winfo_screenwidth()/2
    hd = window.winfo_screenheight()/2
    window.geometry('%dx%d+%d+%d' % (225, 45, wd-125, hd-125))
    linkfield = Entry(window, width=35)
    Label(window, text="Link:").grid(row=0)
    linkfield.grid(row=0, column=1)
    btn = Button(window, text="DOWNLOAD", command=lambda: download_video(linkfield.get()))
    btn.place(x=0, y=20)
    tag = Label(window, text = "DC: Tacomies#2616")
    tag.config(font =("Courier", 10))
    tag.place(x=85, y=20)
#Main function for style reasons
def main():
    setup()
    mainloop()

main()