from tkinter import *
import os, requests
class root:
    def __init__(self):
        self.version="0.0.0.1"
        self.latestVersion=get.version(self)
        self.homeWebsite="https://hanralatalliardwork.github.io/smart-art-trees/"
        self.fileSection="files/program/img"
        self.downloadSection="files/download"
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
            Tk
RI=root()
if RI.version<RI.latestVersion:
    Tkinter.window.notifyUpdate(RI)
