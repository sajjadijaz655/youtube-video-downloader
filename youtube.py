 ##  git+https://gitlab.com/obuilds/public/pytube@ob-v1
from tkinter import *
from pytube import YouTube
import tkinter.font as font
import tkinter.filedialog as w
import tkinter.messagebox as m
a=Tk()
a.title("youtube video downloader")
a.minsize(800,600)
a.maxsize(800,600)
myfont2=font.Font(size=24)
myfont=font.Font(size=31)
        ### New window after click the search button
def new_window():
    window=Tk()
    abc=url_entry.get()
    at=str(abc)
    window.title(f"Serach results for {at}")
    window.minsize(600,600)
    window.maxsize(600,600)

    url=url_entry.get()
    videourl=str(url)
    path_raw=w.askdirectory()
    path=str(path_raw)

         ## low quality button functionality

    def lq():
        try:
            yt_obj=YouTube(videourl)
            title_raw=yt_obj.title
            title=str(title_raw)
            vidfil=yt_obj.streams.filter(progressive=True,file_extension="mp4")
            vidfil.get_lowest_resolution().download(output_path=path,filename=title)
            m.showinfo("info",f"File downloaded at {path}")
        except Exception as e:
            print(e)
            ## high quality button functionality
    def hq():
        try:
            yt_obj=YouTube(videourl)
            title_raw=yt_obj.title
            title=str(title_raw)
            vidfil=yt_obj.streams.filter(progressive=True,file_extension="mp4")
            vidfil.get_highest_resolution().download(output_path=path,filename=title)
            m.showinfo("info",f"File downloaded at {path}")
        except Exception as e:
            print(e)

            ## Audio quality  button functionallity
    def aq():
        try:
            yt_obj=YouTube(videourl)
            title_raw=yt_obj.title
            title=str(title_raw)
            #vidfil=yt_obj.streams.filter(progressive=True,file="mp4")
            yt_obj.streams.get_audio_only().download(output_path=path,filename=title)
            m.showinfo("info",f"File downloaded at {path}")
        except Exception as e:
            print(e)



     ## label
    label1=Label(window,text="Download option",padx=250,pady=50)
    label1["font"]=myfont2
    label1.grid(column=5,row=1)
             ## buttons
    lq=Button(window,text="Download in low quality",padx=40,pady=20,command=lq)
    hq=Button(window,text="Download in high quality",padx=40,pady=20,command=hq)
    audio=Button(window,text="Download as audio",padx=40,pady=20,command=aq)
       ## grid button
    lq.grid(column=5,row=2)
    hq.grid(column=5,row=4)
    audio.grid(column=5,row=6)





    window.mainloop()

                        ## label
head=Label(a,text="Welcome to youtube video downloader",padx=21,pady=50)
head["font"]=myfont
head.grid(row=1,column=1)
                       ### entery box
enter=StringVar()
url_entry=Entry(a,textvariable=enter)
url_entry["font"]=myfont2
url_entry.grid(row=2,column=1)
                    ## button
btn=Button(a,text="Search",bg="light green",fg="white",command=new_window)
btn["font"]=myfont2
btn.grid(row=3,column=1)                  

a.mainloop()
