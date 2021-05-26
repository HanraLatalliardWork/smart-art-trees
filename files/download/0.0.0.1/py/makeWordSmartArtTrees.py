from tkinter import *
from webbrowser import open_new_tab
import os, requests
class root:
    def __init__(self):
        self.version="0.0.0.1"
        self.latestVersion=get.version(self)
        self.homeWebsite="https://hanralatalliardwork.github.io/smart-art-trees/"
        self.fileSection="files/program/img/"
        self.downloadSection="files/download/"
        #---------------------------------TKINTER---------------------------------
        self.universalBackground="white"
class get(root):
    class online:
        def tempFile(url="http://www.a.fr"):
            return open(requests.get(url).content,"r").read()
        def onlineFile(url="http://www.a.fr",path=".", name="file.txt"):
            e=requests.get(url).content
            open("{}/{}".format(path,name), 'wb').write(e)
            return e,f"{path}/{name}"
    
    def version(self):
        version=get.online.tempFile(f"{self.homeWebsite}/{self.fileSection}/versions.txt")
        versions=version.split("\n")
        latest=len(versions)-1
        return latest
class Tkinter(root):
    class window:
        def notifyUpdate(self):
            def newVersion():
                open_new_tab(f"{self.homeWebsite}{self.downloadSection}{self.latestVersion}")
            TT=Tk()
            TT.title("New version avaidable")
            TT['bg']=self.universalBackground
            LabelTitle=Label(TT,text="A new version is avaidable",anchor=center)
            LabelTitle.pack(side=TOP,fill=X)
            SubTitle1=Label(TT,text=f"Version {self.latestVersion} is available."anchor=center)
            SubTitle1.pack(side=TOP,fill=X)
            SubTitle2=Label(TT,text=f"Your current version is {self.version}",anchor=center)
            SubTitle2.pack(side=TOP,fill=X)
            FrameButton=Frame(TT,bg=self.universalBackground,borderwidth=1,border=FLAT)
            FrameButton.pack(side=TOP,fill=X)
            DownloadButton=Button(FrameButton,text="Download new version",command=)
RI=root()
if RI.version<RI.latestVersion:
    Tkinter.window.notifyUpdate(RI)
