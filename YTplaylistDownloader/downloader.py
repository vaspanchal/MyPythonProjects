from tkinter import *
from pytube import YouTube, Playlist

root = Tk() # initialize tkinter to create a canvas
root.geometry('500x300') # to set canvas window size
root.resizable(0,0) # to prohibit user from changing window size
root.title("YouTube Playlist  Downloader - by Vas") # obvious

Label(root,text = 'Youtube Playlist Downloader', font ='arial 20 bold').pack()
# used to display things that user cant modify
    # root = canvas window name
    # text = title of label
    # font = obv
    # pack = it packs organised widget in block

link = StringVar() # string variable that stores playlist link

Label(root,text = 'Paste Link Here : ', font ='arial 15 bold').place(x=160, y=60)

link_enter = Entry(root, width = 70,textvariable = link).place(x = 32, y = 90)
# Entry() = a widget used to create an input text field
    # textvariable - used to retrieve user input
#place() = used to place widget at specific position

def Downloader():
    p =Playlist(str(link.get()))

    for videos in p.videos:
        video = videos.streams.filter(res="1080p").first()
        video.download()

    Label(root, text = 'DOWNLOADED', font = 'arial 15').place(x= 180 , y = 210)

Button(root,text = 'DOWNLOAD', font = 'arial 15 bold' ,bg = 'grey', padx = 2, command = Downloader).place(x=180 ,y = 150)

root.mainloop()
