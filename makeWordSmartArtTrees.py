__Version__ = '0.1'
__Author__='Henry Letellier'
__fileName__='makeWordSmartArtTrees'
__Home__='https://hanralatalliardwork.github.io/smart-art-trees/'
from tkinter import *
from tkinter import ttk
from webbrowser import open_new_tab
import os, requests#, shutil
print("class root")
class root:
    def __init__(self,home,version,author,fileName):
        print("initialising root")
        #---------------------------------KILL ALL--------------------------------
        self.kill=False
        #---------------------------------LINKS-----------------------------------
        self.homeWebsite=home
        self.fileSection="files/program/"
        self.imageFolder="img/"
        self.downloadSection="files/download/"
        #---------------------------------STATUS----------------------------------
        self.isOnline=boot.get.online.isActive()
        #---------------------------------VERSIONS--------------------------------
        self.version=version
        self.latestVersion=boot.get.version(self)#boot.get.version(self.homeWebsite,self.fileSection)
        self.author=author
        self.fileName=fileName
        #---------------------------------LOOPS-----------------------------------
        self.continueMainLoop=True
        #---------------------------------TKINTER---------------------------------
        self.universalBackground="white"
        self.maxDots=35
        #---------------------------------ICON------------------------------------
        self.icon=""
        self.displayIcon=False
        #---------------------------------DISPLAY---------------------------------
        self.window_size_x=424
        self.window_size_y=200
        self.window_geometry=f"{self.window_size_x}x{self.window_size_y}"
        #---------------------------------TEXT------------------------------------
        self.cursor="none"
        self.person="gumby"
        self.text_cells_width=51
        self.text_cells_height=22
        self.window_cell_size_x=self.window_size_x
        self.window_cell_size_y=self.window_size_y+250
        self.window_geometry_cell=f"{self.window_cell_size_x}x{self.window_cell_size_y}"
        self.cursor="X_cursor"
        self.watermark=f"{chr(169)} Created by Henry Letellier"
        #--------------------------------Main Menu --------------------------------
        self.mainMenuPadX=5
        self.MS="Microsoft"
        self.MSVersions=[f"{self.MS} Powerpoint",f"{self.MS} Excel",f"{self.MS} Word",f"{self.MS} Outlook",f"{self.MS} Sharepoint",f"{self.MS} Publisher",f"{self.MS} Access",f"{self.MS} Forms",f"{self.MS} OneNote",f"{self.MS} Tasks",f"{self.MS} Sway",f"{self.MS} Skype",f"{self.MS} Power Automate",f"{self.MS} OneDrive",f"{self.MS} Office",f"{self.MS} Parental control",f"{self.MS} Calendar",f"{self.MS} Bing",f"{self.MS} MSN",f"{self.MS} Rewards",f"{self.MS} Teams"]
        self.yes="possible"
        self.maibye="maibye"
        self.no="impossible"
        self.MSVersionsDict={f"{self.MS} Powerpoint":self.yes,f"{self.MS} Excel":self.yes,f"{self.MS} Word":self.yes,f"{self.MS} Outlook":self.yes,f"{self.MS} Sharepoint":self.maibye,f"{self.MS} Publisher":self.no,f"{self.MS} Access":self.no,f"{self.MS} Forms":self.no,f"{self.MS} OneNote":self.no,f"{self.MS} Tasks":self.no,f"{self.MS} Sway":self.no,f"{self.MS} Skype":self.no,f"{self.MS} Power Automate":self.no,f"{self.MS} OneDrive":self.no,f"{self.MS} Office":self.no,f"{self.MS} Parental control":self.no,f"{self.MS} Calendar":self.no,f"{self.MS} Bing":self.no,f"{self.MS} MSN":self.no,f"{self.MS} Rewards":self.no,f"{self.MS} Teams":self.no}
    def pause():
        pause=input("Press enter to continue ...")
    def unstring(rule="=",string="",take=1):
        try:
            try:
                d=string.split(rule)[take]
                print(f"""
........................................................\n........................................................\n........................................................\n........................................................\n........................................................\n........................................................
d='{string}'.split(rule='{rule}'[take='{take}'])='{d}', type('{d}')={type(d)}""")
                try:
                    print("in try:try:")
                    return float(d)
                except:
                    print("in try:except:")
                    version=""
                    for i in d:
                        if i==".":
                            print(f"i='{i}',version='{version}{i}'")
                            version+=i
                        elif i==" " or i=="\'" or i=="\"":
                            print(f"ignored: '{i}'")
                            pass
                        else:
                            try:
                                print(f"in try:except:try:,i='{i}'")
                                version+=int(i)
                                print(f"version='{version}', type('{version}')={type(version)}")
                            except:
                                print("in try:except:except:")
                                print(f"i='{i}'")
                                pass
                    try:
                        print("try:except:try:")
                        return float(version)
                    except:
                        print("try:except:except:")
                        print(f"d='{d}',type('{d}')={type(d)})")
                        for i in d.split("'"):
                            if len(i)>0:
                                print(f"i='{i}'")
                                return i
                        return d
            except:
                print("in except, line 80")
                f=string.split(rule)[take]
                print(f"f='{f}'")
                word=""
                A=0
                for i in f:
                    if f=="'" or f=="\"":
                        if A==0:
                            A=1
                        else:
                            try:
                                return float(word)
                            except:
                                for i in word:
                                    try:
                                        b=float(i)
                                        print(b)
                                        return b
                                    except:
                                        pass
                                print(f"word='{word}',type('{word}')='{type(word)})'")
                                for i in word.split("'"):
                                    if len(i)>0:
                                        print(i)
                                        return i
                                return word
                    elif A==1:
                        word+=i
        except:
            return None
class boot(root):
    print("class get")
    class get(root):
        class online:
            def tempFile(url="http://www.a.fr"):
                road=requests.get(url).content
                try:
                    abs_path = os.path.abspath(road)
                    if not abs_path.startswith(os.path.abspath(SAFE_BASE_DIR)):
                        raise ValueError("Path traversal attempt blocked.")
                    with open(abs_path, "rb") as f:
                        content = f.read()
                        print("r")
                        return content
                except:
                    try:
                        abs_path = os.path.abspath(road)
                        if not abs_path.startswith(os.path.abspath(SAFE_BASE_DIR)):
                            raise ValueError("Path traversal attempt blocked.")
                        with open(abs_path, "r") as f:
                            content = f.read()
                            print("r")
                            return content
                    except:
                        try:
                            e=road.decode()
                            print("decode")
                            return e
                        except:
                            return road
                
            def file(url="http://www.a.fr",path=".", name="file.txt"):
                e=requests.get(url).content
                open("{}/{}".format(path,name), 'wb').write(e)
                return e,f"{path}/{name}"
            def isActive():
                try:
                    boot.get.online.tempFile(RI.homeWebsite)
                    return True
                except:
                    return False
        class older:
            def versions(self,path):
                fileNames=os.listdir(path=".")
                self.All_the_versions={}
                for i in range(len(fileNames)):
                    if os.path.isfile(fileNames[i]):
                        fileContent=open(f"{path}/{fileNames[i]}","r").read()
                        self.All_the_versions[f"{path}/{fileNames[i]}"]=boot.get.fileVersions(fileContent)
                    else:
                        print(f"{fileNames[i]} is a folder.")
                print(f"All_the_versions={self.All_the_versions}")
                if len(self.All_the_versions)>1:
                    older_found=False
                    self.older_fileNames=[]
                    for i in self.All_the_versions:
                        if self.All_the_versions[i]<float(self.version):
                            older_found=True
                            self.older_fileNames.append(i)
                    if older_found==True:
                        boot.Tkinter.window.askBeforeDelete(self)
            def fileRemoved(self,To,window):
                def update_Status(string,inc,windows):
                    print(string)
                    windows.insert(float(inc),string)
                error_files={}
                o=0
                for i in self.All_the_versions:#range(-1):
                    inc=f"{o+1}.0"
                    if self.All_the_versions[i]<float(self.version):
                        if os.path.exists(i)==True:
                            try:
                                os.remove(i)
                                update_Status(string=f"{i}{boot.get.dots(i,self.maxDots)}[DELETED]\n",inc=inc,windows=To)
                            except:
                                error_files[i]="[FAILED]"
                                update_Status(string=f"{i}{boot.get.dots(i,self.maxDots)}[FAILED]\n",inc=inc,windows=To)
                        else:
                            error_files[i]="[Not Found]"
                            update_Status(string=f"{i}{boot.get.dots(i,self.maxDots)}[NOT FOUND]\n",inc=inc,windows=To)
                    else:
                        error_files[i]="[MORE RECENT]"
                        update_Status(string=f"{i}{boot.get.dots(i,self.maxDots)}[MORE RECENT]\n",inc=inc,windows=To)
                    window.update()
                    o+=1
                return error_files
        def fileVersions(fileContent):
            fileContent=fileContent.split("\n")
            print(f"fileContent(1)={fileContent}")
            
            try:
                print("try:\n####################################################################\na")
                RI.a=fileVersion=boot.unstring(rule="=",string=fileContent[0],take=1)
                print("####################################################################\nb")
                RI.b=fileAuthor=boot.unstring(rule="=",string=fileContent[1],take=1)
                print("####################################################################\nc")
                RI.c=fileName=boot.unstring(rule="=",string=fileContent[2],take=1)
                print("####################################################################\nresult")
                print(f"\n\n\n\na={RI.a},b={RI.b},c={RI.c}\n\n\n\n")
                print(f"\n\n\n\nfileVersion={fileVersion}\nfileAuthor={fileAuthor}\nfileName={fileName}")
                if fileAuthor==RI.author and fileName==RI.fileName:
                    print("\n\n\n\nIn if")
                    try:
                        print(f"\n\n\n\nIn try of if, fileVersion={fileVersion}")
                        return float(fileVersion)
                    except:
                        print("\n\n\n\nin except of if")
                        return float(float(RI.version)+1)
                else:
                    print("\n\n\n\nIn else")
                    return float(float(RI.version)+1)
            except:
                print("\n\n\n\nin Except")
                return float(float(RI.version)+1)
        def version(self):
            try:
                versions=boot.get.online.tempFile(f"{self.homeWebsite}{self.fileSection}versions.txt").split("\n")
                latest=versions[len(versions)-1]
            except:
                latest=self.version
            return latest
        def dots(word="",maxDots=10):
            word=len(word)
            maxDots=maxDots-word
            result=""
            for i in range(maxDots):result+="."
            return result
    print("class check")
    class check(root):
        class ifExists:
            def file(path=".",file=f"no_file_specified.py",url=__Home__):
                if os.path.exists(f"{path}/{file}")==False:
                    boot.get.online.file(url,path, file)
            def folder(path=".",folder="folder"):
                if os.path.exists(f"{path}/{folder}")==False:
                    if os.path.exists(path)==True:
                        os.mkdir(f"{path}/{folder}")
                    else:
                        try:
                            os.mkdir(path)
                            return "[CREATED]"
                        except:
                            assert f"\'{path}\' One or more folder do not exist, please create them first before creating \'{folder}\'"
                else:
                    return "[ALREADY EXITSTS]"
            def path(lst=[],p_and_type={},index=0,maxLength=-1,isCorrect=False,current_path="./",difference=0,window="",important=0,step_by_step=False,talk=0):
                if index==maxLength:
                    RI.kill=False
                    return "[DONE]"
                if isCorrect==False:
                    if len(lst)==0:
                        if important==1:
                            # print("len(lst)==0:=true")
                            RI.kill=True
                        a="The list of files (and/or folders) (lst) must have at least one element."
                        print(a)
                        assert a
                    elif len(p_and_type)==0:
                        if important==1:
                            # print("len(p_and_type)==0:=true")
                            RI.kill=True
                        a="The dictionnary containing the type of each file (and/or folders) (p_and_type) must have at least one element."
                        print(a)
                        assert a
                    elif len(lst)>len(p_and_type) or len(p_and_type)>len(lst):
                        if important==1:
                            # print("len(lst)>len(p_and_type) or len(p_and_type)>len(lst):=true")
                            RI.kill=True
                        a="The list of files (and/or folders) (lst) and dictionnary (containing the type of each file (and/or folders)) (p_and_type) must be the same length."
                        print(a)
                        assert a
                    else:
                        isCorrect=True
                    if maxLength==-1:
                        maxLength=len(lst)
                        isCorrect=True
                    if len(current_path)>0:
                        current_path="./"
                        isCorrect=True
                if talk==1:print(f"isCorrect={isCorrect}")
                if step_by_step==True:root.pause()
                if talk==1:print(f"maxLength={maxLength}")
                if talk==1:print(f"index={index}")
                if step_by_step==True:root.pause()
                if isCorrect==True:
                    if talk==1:print("in isCorrect")
                    if step_by_step==True:root.pause()
                    if str(p_and_type[lst[index]]).lower()=="<dir>" or str(p_and_type[lst[index]]).lower()=="dir":
                        if talk==1:print("In dir")
                        if step_by_step==True:root.pause()
                        try:
                            if talk==1:print("in try:")
                            if step_by_step==True:root.pause()
                            if os.path.exists(f"{current_path}{lst[index]}")==False:
                                os.mkdir(f"{current_path}{lst[index]}")
                                if talk==1:print(f"Created {lst[index]} in {current_path}")
                            else:
                                if talk==1:print(f"Added '{lst[index]}' to path: '{current_path}' because folder allready exists")
                            current_path+=f"{lst[index]}/"
                            #dots=boot.get.dots(f"{lst[index]}",self.maxDots)
                            #dots1=boot.get.dots(f"{current_path}",self.maxDots)
                            #window.insert(float(index+1+difference),f"in{dots1}{current_path}")
                            #window.insert(float(index+2+difference),f"{lst[index]}{dots}[CREATED]")
                            return boot.check.ifExists.path(lst,p_and_type,index+1,maxLength,isCorrect,current_path,difference+1,window)
                        except:
                            if talk==1:print("in except")
                            if step_by_step==True:root.pause()
                            dots=boot.get.dots(f"{current_path}{lst[index]}",RI.maxDots)
                            #window.insert(float(index+2+difference),f"{lst[index]}{dots}[FAILED]")
                            if talk==1:print(f"Failed to create {lst[index]} in {current_path}")
                            if important==1:
                                # print("if:except:=true")
                                RI.kill=True
                            return f"Path:{current_path}{lst[index]}{dots}[ERROR]"
                    elif str(p_and_type[lst[index]]["type"]).lower()=="<file>" or str(p_and_type[lst[index]]["type"]).lower()=="file":
                        if talk==1:print("in file")
                        if step_by_step==True:root.pause()
                        try:
                            if talk==1:print("in try")
                            if step_by_step==True:root.pause()
                            if talk==1:print(f"file={p_and_type[lst[index]]}\ntype={p_and_type[lst[index]]['type']}\nfileName={p_and_type[lst[index]]['fileName']}\nfileContent={p_and_type[lst[index]]['fileContent']}")
                            f=open(f"{current_path}{p_and_type[lst[index]]['fileName']}","w")
                            f.write(str(p_and_type[lst[index]]['fileContent']))
                            f.close()
                            if talk==1:print(f"Created {p_and_type[lst[index]]['fileName']} in {current_path} with {p_and_type[lst[index]]['fileContent']}")
                            #dots=boot.get.dots(f"{lst[index]}",self.maxDots)
                            #dots1=boot.get.dots(f"{current_path}",self.maxDots)
                            #window.insert(float(index+1+difference),f"in{dots1}{current_path}")
                            #window.insert(float(index+2+difference),f"{lst[index]}{dots}[CREATED]")
                            return boot.check.ifExists.path(lst,p_and_type,index+1,maxLength,isCorrect,current_path,difference+1,window)
                        except:
                            if talk==1:print("in except")
                            if step_by_step==True:root.pause()
                            dots=boot.get.dots(f"{current_path}{lst[index]}",RI.maxDots)
                            #window.insert(float(index+2+difference),f"{lst[index]}{dots}[FAILED]")
                            if talk==1:print(f"Failed to create {lst[index]} in {current_path}")
                            if important==1:
                                # print("elif:except:=true")
                                RI.kill=True
                            return f"Path:{current_path}{lst[index]}{dots}[ERROR]"
                    else:
                        a=f"Unknown type for {lst[index]}, type {p_and_type[lst[index]]} doesn't exist in this recursivity.\nType can only be '<dir>' or 'dir' for a directory anf '<file>' or 'file' for a file."
                        print(a)
                        assert a
                        if important==1:
                            # print("else:=true")
                            RI.kill=True

    print("class tkinter")
    class Tkinter(root):
        class window:
            def askBeforeDelete(self):
                def delete():
                    TT.destroy()
                    boot.Tkinter.window.deletingFiles(RI)
                TT=Tk()
                if self.displayIcon==True:
                    TT.iconbitmap(self.icon)
                TT.geometry(self.window_geometry)
                TT.minsize(self.window_size_x,self.window_size_y)
                TT.title("Deleting older versions...")
                TT['bg']=self.universalBackground
                TitleLabel=Label(TT,text="Older versions have been found.",bg=self.universalBackground)
                TitleLabel.pack(side=TOP,fill=X)
                ProgressWindow=Text(
                    TT,
                    cursor=self.person,
                    state="normal",
                    wrap="none",
                    bg=self.universalBackground,
                    fg="black",
                    exportselection=0,
                    width=self.text_cells_width,
                    height=self.text_cells_height-14,
                    padx=5,pady=5,
                    relief=FLAT)#,font=(self.FontBoard,self.SizeBoard,self.weightB))
                ProgressWindow.pack()
                for i in range(len(self.older_fileNames)):
                    ProgressWindow.insert(float(i+1),f"{self.older_fileNames[i]}{boot.get.dots(self.older_fileNames[i],self.maxDots)}[OLDER]\n")
                
                FrameButton=Frame(TT,bg=self.universalBackground,borderwidth=1,relief=FLAT)
                FrameButton.pack(side=TOP,fill=X)
                DownloadButton=Button(FrameButton,text="Delete older files (recommended)",command=delete,bg=self.universalBackground)
                DownloadButton.pack(side=LEFT)
                ContinueButton=Button(FrameButton,text="Continue without deleting",command=TT.destroy,bg=self.universalBackground)
                ContinueButton.pack(side=RIGHT)
                MessageLabel=Label(TT,text=self.watermark,bg=self.universalBackground,anchor="center")
                MessageLabel.pack(side=RIGHT,fill=X)
                TT.mainloop()
                
            def update_Status(string,inc,windows):
                print(string)
                windows.insert(float(inc),string)
            def deletingFiles(self):
                print("Deleting files...")
                TT=Tk()
                if self.displayIcon==True:
                    TT.iconbitmap(self.icon)
                TT.geometry(self.window_geometry)
                TT.minsize(self.window_size_x,self.window_size_y)
                TT.title("Deleting older versions...")
                TT['bg']=self.universalBackground
                TitleLabel=Label(TT,text="Deleting older versions...",bg=self.universalBackground,anchor="center")
                TitleLabel.pack(side=TOP,fill=X)
                ProgressWindow=Text(TT,cursor=self.cursor,state="normal",insertbackground="lightGreen",wrap="none",bg="black",fg="lightGreen",exportselection=0,width=self.text_cells_width,height=self.text_cells_height-14,padx=5,pady=5,relief=FLAT)#,font=(self.FontBoard,self.SizeBoard,self.weightB))
                ProgressWindow.pack()
                boot.get.older.fileRemoved(self,ProgressWindow,TT)
                FrameButton=Frame(TT,bg=self.universalBackground,borderwidth=1,relief=FLAT)#"green"
                FrameButton.pack(side=TOP,fill=X)
                DownloadButton=Button(FrameButton,text="Great!",command=TT.destroy,bg=self.universalBackground)
                DownloadButton.pack(side=TOP,fill=X)
                MessageLabel=Label(TT,text=self.watermark,bg=self.universalBackground,anchor="center")
                MessageLabel.pack(side=RIGHT,fill=X)
                TT.mainloop()
                
            def notifyUpdate(self):
                def newVersion():
                    TT.destroy()
                    open_new_tab(f"{RI.homeWebsite}{self.downloadSection}/{self.latestVersion[0]}/{self.latestVersion}")
                    self.continueMainLoop=False
                TT=Tk()
                if self.displayIcon==True:
                    TT.iconbitmap(self.icon)
                TT.geometry(self.window_geometry)
                TT.minsize(self.window_size_x,self.window_size_y)
                TT.title("New version available")
                TT['bg']=self.universalBackground
                LabelTitle=Label(TT,text="A new version is available",anchor="center",bg=self.universalBackground)
                LabelTitle.pack(side=TOP,fill=X)
                SubTitle1=Label(TT,text=f"Version {self.latestVersion} is available.",anchor="center",bg=self.universalBackground)
                SubTitle1.pack(side=TOP,fill=X)
                SubTitle2=Label(TT,text=f"Your current version is {self.version}",anchor="center",bg=self.universalBackground)
                SubTitle2.pack(side=TOP,fill=X)
                FrameButton=Frame(TT,bg=self.universalBackground,borderwidth=1,relief=FLAT)
                FrameButton.pack(side=TOP,fill=X)
                DownloadButton=Button(FrameButton,text="Download new version",command=newVersion,bg=self.universalBackground)
                DownloadButton.pack(side=LEFT)
                ContinueButton=Button(FrameButton,text="Proceed anyway",command=TT.destroy,bg=self.universalBackground)
                ContinueButton.pack(side=RIGHT)
                MessageLabel=Label(TT,text=self.watermark,bg=self.universalBackground,anchor="center")
                MessageLabel.pack(side=RIGHT,fill=X)
                TT.mainloop()
class Jacques_Henri(root):
    def initialise(self):
        Jacques_Henri.Tkinter.mainMenu(self)
    class Tkinter:
        def mainMenu(self):
            def one():
                TT.destroy()
                Jacques_Henri.Tkinter.one(self)
            def two():
                TT.destroy()
                Jacques_Henri.Tkinter.two(self)
            def three():
                TT.destroy()
                Jacques_Henri.Tkinter.three(self)
            def four():
                TT.destroy()
                self.kill=True
                TTQ=Tk()
                if self.displayIcon==True:
                    TTQ.iconbitmap(self.icon)
                self.window_size_y=90
                self.window_geometry=f"{self.window_size_x}x{self.window_size_y}"
                TTQ.geometry(self.window_geometry)
                TTQ.minsize(self.window_size_x,self.window_size_y)
                TTQ.title("Goodbye")
                TTQ['bg']=self.universalBackground
                TitleLabel=Label(TTQ,text="Goodbye",bg=self.universalBackground,anchor="center")
                TitleLabel.pack(side=TOP,fill=X)
                MessageLabel=Label(TTQ,text="Goodbye, see you soon. :-)",bg=self.universalBackground,anchor="center")
                MessageLabel.pack(side=TOP,fill=X)
                ContinueButton=Button(TTQ,text="Close",command=TTQ.destroy,bg=self.universalBackground,anchor="center")
                ContinueButton.pack(fill=X,padx=self.mainMenuPadX)
                MessageLabel=Label(TTQ,text=self.watermark,bg=self.universalBackground,anchor="center")
                MessageLabel.pack(side=RIGHT,fill=X)
                TTQ.mainloop()
            TT=Tk()
            if self.displayIcon==True:
                TT.iconbitmap(self.icon)
            TT.geometry(self.window_geometry)
            TT.minsize(self.window_size_x,self.window_size_y)
            TT.title("Main Menu")
            TT['bg']=self.universalBackground
            TitleLabel=Label(TT,text="Main Menu",bg=self.universalBackground,anchor="center")
            TitleLabel.pack(side=TOP,fill=X)
            DropDown_options=()
            FrameMainButton=Frame(TT,bg=self.universalBackground,borderwidth=1,relief=FLAT)
            FrameMainButton.pack(side=TOP,fill=X)
            FrameButtonTop=Frame(FrameMainButton,bg=self.universalBackground,borderwidth=1,relief=FLAT)
            FrameButtonTop.pack(side=TOP,fill=X)
            DownloadButton=Button(FrameButtonTop,text="Tutorial on how to manually use Smart Art",command=one,bg=self.universalBackground)
            DownloadButton.pack(side=LEFT,fill=X,padx=self.mainMenuPadX)
            DownloadButton=Button(FrameButtonTop,text="Generate a Smart Art scheme",command=two,bg=self.universalBackground)
            DownloadButton.pack(side=RIGHT,fill=X,padx=self.mainMenuPadX)
            FrameButtonBottom=Frame(FrameMainButton,bg=self.universalBackground,borderwidth=1,relief=FLAT)
            FrameButtonBottom.pack(side=TOP,fill=X)
            DownloadButton=Button(FrameButtonBottom,text="Generate a Smart Art in word\n(i'm looking for somebody to write the VBA script)",command=three,bg=self.universalBackground)
            DownloadButton.pack(side=LEFT,fill=X,padx=self.mainMenuPadX)
            ContinueButton=Button(FrameButtonBottom,text="Quit",command=four,bg=self.universalBackground)
            ContinueButton.pack(side=RIGHT,fill=X,padx=self.mainMenuPadX)
            MessageLabel=Label(TT,text=self.watermark,bg=self.universalBackground,anchor="center")
            MessageLabel.pack(side=RIGHT,fill=X)
            TT.mainloop()
        def one(self):
            def open_in_browser():
                open_new_tab(f"{self.home}")
            TT=Tk()
            if self.displayIcon==True:
                TT.iconbitmap(self.icon)
            TT.geometry(self.window_geometry)
            TT.minsize(self.window_size_x,self.window_size_y)
            TT.title("How to manually use Smart Art")
            TT['bg']=self.universalBackground
            TitleLabel=Label(TT,text="How to manually use Smart Art",bg=self.universalBackground,anchor="center")
            TitleLabel.pack(side=TOP,fill=X)
            DropDown_options=()
            FrameMainButton=Frame(TT,bg=self.universalBackground,borderwidth=1,relief=FLAT)
            FrameMainButton.pack(side=TOP,fill=X)
            DownloadButton=Button(FrameMainButton,text="View in Browser",command=open_in_browser,bg=self.universalBackground)
            DownloadButton.pack(side=LEFT,fill=X,padx=self.mainMenuPadX)
            ContinueButton=Button(FrameMainButton,text="Close",command=TT.destroy,bg=self.universalBackground)
            ContinueButton.pack(side=RIGHT,fill=X,padx=self.mainMenuPadX)
            MessageLabel=Label(TT,text=self.watermark,bg=self.universalBackground,anchor="center")
            MessageLabel.pack(side=RIGHT,fill=X)
            TT.mainloop()
        def two(self):
            def helpButton():
                print("")
            def update_options(*args):
                e=listeCombo.get()
                e=self.MSVersionsDict[e]
                # print(e)
                if e==self.no:
                    GenerateButton.config(state="disable")
                    numberOfColums.config(state="disable")
                    numberOfLeaves.config(state="disable")

                else:
                    GenerateButton.config(state="normal")
                    numberOfColums.config(state="normal")
                    numberOfLeaves.config(state="normal")
            def tree():
                e=numberOfColums.get()
                r=numberOfLeaves.get()
                print(f"number_of_colums={e}, number_of_leaves={r}")
            TT=Tk()
            if self.displayIcon==True:
                TT.iconbitmap(self.icon)
            TT.geometry(self.window_geometry)
            TT.minsize(self.window_size_x,self.window_size_y)
            TT.title("Generate a Smart Art Scheme")
            TT['bg']=self.universalBackground
            TitleLabel=Label(TT,text="Generate a Smart Art Scheme",bg=self.universalBackground,anchor="center")
            TitleLabel.pack(side=TOP,fill=X)
            FrameMain=Frame(TT,bg=self.universalBackground,borderwidth=1,relief=FLAT)
            FrameMain.pack(side=TOP,fill=X)
            FrameTop=Frame(FrameMain,bg=self.universalBackground,borderwidth=1,relief=FLAT)
            FrameTop.pack(side=TOP,fill=X)
            FrameMid=Frame(FrameMain,bg=self.universalBackground,borderwidth=1,relief=FLAT)
            FrameMid.pack(side=TOP,fill=X)
            FrameBottom=Frame(FrameMain,bg=self.universalBackground,borderwidth=1,relief=FLAT)
            FrameBottom.pack(side=TOP,fill=X)
            FrameBottomBottom=Frame(FrameMain,bg=self.universalBackground,borderwidth=1,relief=FLAT)
            FrameBottomBottom.pack(side=TOP,fill=X)
            HelpButton=Button(FrameTop,text="?",command=helpButton,bg=self.universalBackground)#tutorial on how this section works
            HelpButton.pack(side=RIGHT,fill=X,padx=self.mainMenuPadX)
            MidLabel=Label(FrameMid,text="Tree Type",bg=self.universalBackground)
            MidLabel.pack(side=LEFT,fill=X)
            FrameDropdown=Frame(FrameMid,bg=self.universalBackground,relief=FLAT,border=0)
            FrameDropdown.pack(side=LEFT,fill=X)
            listeCombo = ttk.Combobox(FrameDropdown, values=self.MSVersions,width=100)
            listeCombo.current(0)
            listeCombo.pack()#fill=Y,pady=1,padx=5)
            listeCombo.bind("<<ComboboxSelected>>",update_options)#,command=youjerk
            treeImage=()
            MidLabelBefore=Label(FrameBottom,text="The tree has",bg=self.universalBackground)
            MidLabelBefore.pack(side=LEFT,fill=X)
            numberOfColums=Spinbox(FrameBottom, from_=1, to=999, increment=1, wrap=True)
            numberOfColums.pack(side=LEFT, padx=5)
            MidLabelAfter=Label(FrameBottom,text="colum(s).",bg=self.universalBackground)
            MidLabelAfter.pack(side=LEFT,fill=X)
            MidLabelBefore1=Label(FrameBottomBottom,text="The colum has",bg=self.universalBackground)
            MidLabelBefore1.pack(side=LEFT,fill=X)
            numberOfLeaves=Spinbox(FrameBottomBottom, from_=1, to=999, increment=1, wrap=True)
            numberOfLeaves.pack(side=LEFT, padx=5)
            MidLabelAfter1=Label(FrameBottomBottom,text="leaves(s).",bg=self.universalBackground)
            MidLabelAfter1.pack(side=LEFT,fill=X)
            GenerateButton=Button(TT,text="Generate the tree", command=tree,bg=self.universalBackground)
            GenerateButton.pack(side=TOP,fill=X,padx=self.mainMenuPadX)
            MessageLabel=Label(TT,text=self.watermark,bg=self.universalBackground,anchor="center")
            MessageLabel.pack(side=RIGHT,fill=X)
            TT.mainloop()
        def three(self):
            TT=Tk()
            if self.displayIcon==True:
                TT.iconbitmap(self.icon)
            TT.geometry(self.window_geometry)
            TT.minsize(self.window_size_x,self.window_size_y)
            TT.title("Main Menu")
            TT['bg']=self.universalBackground
            TitleLabel=Label(TT,text="Main Menu",bg=self.universalBackground,anchor="center")
            TitleLabel.pack(side=TOP,fill=X)
            DropDown_options=()
            FrameMainButton=Frame(TT,bg=self.universalBackground,borderwidth=1,relief=FLAT)
            FrameMainButton.pack(side=TOP,fill=X)
            FrameButtonTop=Frame(FrameMainButton,bg=self.universalBackground,borderwidth=1,relief=FLAT)
            FrameButtonTop.pack(side=TOP,fill=X)
            DownloadButton=Button(FrameButtonTop,text="Tutorial on how to manually use Smart Art",command=TT.destroy,bg=self.universalBackground)
            DownloadButton.pack(side=LEFT,fill=X,padx=self.mainMenuPadX)
            DownloadButton=Button(FrameButtonTop,text="Generate a Smart Art scheme",command=TT.destroy,bg=self.universalBackground)
            DownloadButton.pack(side=RIGHT,fill=X,padx=self.mainMenuPadX)
            FrameButtonBottom=Frame(FrameMainButton,bg=self.universalBackground,borderwidth=1,relief=FLAT)
            FrameButtonBottom.pack(side=TOP,fill=X)
            DownloadButton=Button(FrameButtonBottom,text="Generate a Smart Art in word\n(i'm looking for somebody to write the VBA script)",command=TT.destroy,bg=self.universalBackground)
            DownloadButton.pack(side=LEFT,fill=X,padx=self.mainMenuPadX)
            ContinueButton=Button(FrameButtonBottom,text="Quit",command=TT.destroy,bg=self.universalBackground)
            ContinueButton.pack(side=RIGHT,fill=X,padx=self.mainMenuPadX)
            MessageLabel=Label(TT,text=self.watermark,bg=self.universalBackground,anchor="center")
            MessageLabel.pack(side=RIGHT,fill=X)
            TT.mainloop()
            
print("RI=root()")
RI=root(__Home__,__Version__,__Author__,__fileName__)
print("success")
main_root_lst=[["B","a","a.txt","b","b.txt","c","c.txt","d","d.txt","e","e.txt","f","f.txt","g","g.txt","h","h.txt","i","i.txt","j","j.txt","k","k.txt","l","l.txt","m","m.txt","n","n.txt","o","o.txt","p","p.txt","q","q.txt","r","r.txt","s","s.txt","t","t.txt","u","u.txt","v","v.txt","w","w.txt","x","x.txt","y","y.txt","z","z.txt"]]
main_root_dict=[{"B":"dir","a":"dir","a.txt":{"type":"file","fileName":"a.txt","fileContent":"eeeeeeeeee"},"b":"dir","b.txt":{"type":"file","fileName":"b.txt","fileContent":"eeeeeeeeee"},"c":"dir","c.txt":{"type":"file","fileName":"c.txt","fileContent":"eeeeeeeeee"},"d":"dir","d.txt":{"type":"file","fileName":"d.txt","fileContent":"eeeeeeeeee"},"e":"dir","e.txt":{"type":"file","fileName":"e.txt","fileContent":"eeeeeeeeee"},"f":"dir","f.txt":{"type":"file","fileName":"f.txt","fileContent":"eeeeeeeeee"},"g":"dir","g.txt":{"type":"file","fileName":"g.txt","fileContent":"eeeeeeeeee"},"h":"dir","h.txt":{"type":"file","fileName":"h.txt","fileContent":"eeeeeeeeee"},"i":"dir","i.txt":{"type":"file","fileName":"i.txt","fileContent":"eeeeeeeeee"},"j":"dir","j.txt":{"type":"file","fileName":"j.txt","fileContent":"eeeeeeeeee"},"k":"dir","k.txt":{"type":"file","fileName":"k.txt","fileContent":"eeeeeeeeee"},"l":"dir","l.txt":{"type":"file","fileName":"l.txt","fileContent":"eeeeeeeeee"},"m":"dir","m.txt":{"type":"file","fileName":"m.txt","fileContent":"eeeeeeeeee"},"n":"dir","n.txt":{"type":"file","fileName":"n.txt","fileContent":"eeeeeeeeee"},"o":"dir","o.txt":{"type":"file","fileName":"o.txt","fileContent":"eeeeeeeeee"},"p":"dir","p.txt":{"type":"file","fileName":"p.txt","fileContent":"eeeeeeeeee"},"q":"dir","q.txt":{"type":"file","fileName":"q.txt","fileContent":"eeeeeeeeee"},"r":"dir","r.txt":{"type":"file","fileName":"r.txt","fileContent":"eeeeeeeeee"},"s":"dir","s.txt":{"type":"file","fileName":"s.txt","fileContent":"eeeeeeeeee"},"t":"dir","t.txt":{"type":"file","fileName":"t.txt","fileContent":"eeeeeeeeee"},"u":"dir","u.txt":{"type":"file","fileName":"u.txt","fileContent":"eeeeeeeeee"},"v":"dir","v.txt":{"type":"file","fileName":"v.txt","fileContent":"eeeeeeeeee"},"w":"dir","w.txt":{"type":"file","fileName":"w.txt","fileContent":"eeeeeeeeee"},"x":"dir","x.txt":{"type":"file","fileName":"x.txt","fileContent":"eeeeeeeeee"},"y":"dir","y.txt":{"type":"file","fileName":"y.txt","fileContent":"eeeeeeeeee"},"z":"dir","z.txt":{"type":"file","fileName":"z.txt","fileContent":"eeeeeeeeee"}}]
for i in range(len(main_root_lst)):
    print(boot.check.ifExists.path(lst=main_root_lst[i],p_and_type=main_root_dict[i],index=0,maxLength=-1,isCorrect=False,current_path="",difference=0,window="",important=1,talk=0))
    # print(i)
    # print(f"RI.kill={RI.kill}")
if RI.kill==False: 
    print("in boot.get.older.versions")
    boot.get.older.versions(RI,".")
    print(RI.latestVersion)
    # RI.latestVersion="0.3"
    RI.isOnline=boot.get.online.isActive()
    if float(RI.version)<float(RI.latestVersion) and RI.isOnline==True:
        boot.Tkinter.window.notifyUpdate(RI)
while RI.kill==False:
    Jacques_Henri.initialise(RI)



if RI.kill==False:#True:
    root.pause()
    root.pause()
    root.pause()
    root.pause()
    root.pause()
    root.pause()
