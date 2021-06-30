from tkinter import *
from pytube import YouTube
root = Tk()
root.title("YOUTUBE DOWNLOADER")
Label(root,text="YOUTUBE VIDEO DOWNLOADER",font='arial').pack()
Label(root,text="Please enter the URL of the video..",font = 'arial').place(x = 160,y=50)
link=StringVar()
our_link = Entry(root,width=60,textvariable=link).place(x=20,y=90)

def youtubeDownloader():
    given_url=YouTube(str(link.get()))
    video = given_url.streams.first()
    video.download()
    Label(root,text="video is downloaded",font ='arial').place(x=180,y=100)


Button(root,text="DOWNLOAD",font="arial", command = youtubeDownloader).place(x=180,y=150)
root.mainloop()
