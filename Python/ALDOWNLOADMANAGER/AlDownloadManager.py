import time
from tkinter import *
from tkinter import font
import tkinter.ttk as ttk
from tkinter.constants import *
from pySmartDL import SmartDL
import threading
import os
import pyttsx3
from PIL import ImageTk, Image
import sys

cwd = os.path.dirname(os.path.realpath(__file__))

class AlDownloadManager():
    
    def __init__(self):
        root = Tk(className = " ALDOWNLOADMANAGER ")
        root.geometry("700x360+1200+635")
        root.resizable(0,0)
        root.iconbitmap(os.path.join(cwd+'\\UI\\icons', 'aldownloadmanager.ico'))
        root.config(bg="#ffffff")
        self.defaultColor = ''
        self.isPaused = False
        self.downloadObject = ''
        self.inputLink = StringVar()
        self.statusMessage = StringVar()
        self.speedMessage = StringVar()
        self.destinationMessage = StringVar()
        self.sizeMessage = StringVar()
        self.timeMessage = StringVar()
        textHighlightFont = font.Font(family='OnePlus Sans Display', size=15, weight='bold')
        appHighlightFont = font.Font(family='OnePlus Sans Display', size=12, weight='bold')
        textFont = font.Font(family='OnePlus Sans Text', size=10, weight='bold')
        self.destination = os.path.join(cwd,'AlDownloadManager')
        root.overrideredirect(1)
        
        def callback(event):
            root.geometry("700x360+1200+635")

        def showScreen(event):
            root.deiconify()
            root.overrideredirect(1)

        def screenAppear(event):
            root.overrideredirect(1)

        def hideScreen():
            root.overrideredirect(0)
            root.iconify()

        def speak(audio):
            engine = pyttsx3.init('sapi5')
            voices = engine.getProperty('voices')
            engine.setProperty('voice', voices[0].id)
            engine.say(audio)
            engine.runAndWait()
        
        def terminate(object):
            if object:
                object.stop()
            pauseButton['state'] = DISABLED
            stopButton['text'] = 'STOP'
            stopButton['state'] = DISABLED
            stopButton['bg'] = self.defaultColor
            pauseButton['text'] = "PAUSE"
            downloadButton['state'] = NORMAL

        def pauseResume(object):
            if self.isPaused:
                object.resume()
                pauseButton['text'] = "PAUSE"
                pauseButton['fg'] = "white"
                pauseButton.flash()
                self.isPaused = not self.isPaused
            else:
                object.pause()
                pauseButton['text'] = "RESUME"
                pauseButton['fg'] = "white"
                pauseButton.flash()
                self.isPaused = not self.isPaused

        def download(__url__):
            url = __url__
            self.destination = str(self.destination)
            stopButton['command'] = lambda: terminate(self.downloadObject)
            stopButton['state'] = NORMAL
            pauseButton['command'] = lambda: pauseResume(self.downloadObject)
            pauseButton['state'] = NORMAL

            def doDownload(sem):
                with sem:
                    try:
                        if self.downloadObject:
                            self.downloadObject.start()
                    except Exception as e:
                        print(f"------> {e}")
                        print(f"object error ---> {self.downloadObject.get_errors()}")
                        self.statusMessage.set(f"   Status: {e}")
                        root.update_idletasks()

            def showProgress(sem):
                with sem:
                    time.sleep(1)
                    startTime = time.perf_counter()
                    if self.downloadObject:
                        while not self.downloadObject.isFinished() and len(self.downloadObject.get_errors()) == 0:
                            self.statusMessage.set(f"   Status: {self.downloadObject.get_status().capitalize()}")
                            self.speedMessage.set(f"   Speed: {self.downloadObject.get_speed(human=True)}")
                            self.destinationMessage.set(f"   Working directory: {self.destination}")
                            self.sizeMessage.set(f"   Downloaded so far: {self.downloadObject.get_dl_size(human=True)}")
                            self.timeMessage.set(f"   Elapsed Time: {round(time.perf_counter() - startTime, 1)}" if self.downloadObject.get_status() != 'paused' else '   Elapsed Time: . . . ')
                            progress['value'] = 100 * self.downloadObject.get_progress()
                            time.sleep(0.2)
                            root.update_idletasks()
                        if len(self.downloadObject.get_errors()) == 0:
                            startPoint = time.perf_counter()
                            while time.perf_counter() - startPoint < 2:
                                self.statusMessage.set(f"   Status: {self.downloadObject.get_status().capitalize()}")
                                self.speedMessage.set(f"   Speed: {self.downloadObject.get_speed(human=True)}")
                                self.destinationMessage.set(f"   Saved at: {self.downloadObject.get_dest()}")
                                self.sizeMessage.set(f"   Total File Size: {self.downloadObject.get_final_filesize(human=True)}")
                                self.timeMessage.set(f"   Total Time: {str(self.downloadObject.get_dl_time(human=True))}")
                                progress['value'] = 100 * self.downloadObject.get_progress()
                                time.sleep(0.2)
                                root.update_idletasks()
                            if progress['value'] == 100:
                                speak('File Downloaded')
                        else:
                            self.statusMessage.set(f"   Status: Download Failed")
                            self.speedMessage.set(f"   Reason: {self.downloadObject.get_errors()[0]}")
                            root.update_idletasks()
                            speak('Download Failed')

            if len(url) == 0:
                downloadButton.flash()
            else:
                try:
                    self.downloadObject = SmartDL(url, self.destination)
                except Exception as e:
                    print(f"Error in {e}")
                    self.statusMessage.set(f"   Status: {e}")
                    root.update_idletasks()
                semaphore = threading.Semaphore(2)
                threading.Thread(target=doDownload, args=(semaphore,)).start()
                threading.Thread(target=showProgress, args=(semaphore,)).start()

        def doPopup(event):
            try:
                menuWindow.tk_popup(event.x_root, event.y_root)
            finally:
                menuWindow.grab_release()

        def cut(__input__):
            i = __input__
            entryLink.clipboard_clear()
            entryLink.clipboard_append(i)
            self.inputLink.set('')

        def copy(__input__):
            i = __input__
            entryLink.clipboard_clear()
            entryLink.clipboard_append(i)

        def paste(__input__):
            i0 = __input__
            i1 = entryLink.clipboard_get()
            print(i1)
            self.inputLink.set(i0 + i1)

        def pasteDownload(__input__):
            i0 = __input__
            i1 = entryLink.clipboard_get()
            self.inputLink.set(i0 + i1)
            link = entryLink.get()
            if link != '':
                download(link)
                downloadButton.flash()
                downloadButton['state'] = DISABLED
                self.defaultColor = stopButton.cget('background')
            else:
                downloadButton.flash()

        def clearReset():
            self.inputLink.set('')
            terminate(self.downloadObject)
            downloadButton['state'] = NORMAL

        def startDownloading():
            link = entryLink.get()
            if link != '':
                download(link)
                downloadButton.flash()
                downloadButton['state'] = DISABLED
                self.defaultColor = stopButton.cget('background')
            else:
                downloadButton.flash()

        titleBar = Frame(root, bg='#141414', relief=SUNKEN, bd=0)
        icon = Image.open(os.path.join(cwd+'\\UI\\icons', 'aldownloadmanager.ico'))
        icon = icon.resize((30,30), Image.ANTIALIAS)
        icon = ImageTk.PhotoImage(icon)
        iconLabel = Label(titleBar, image=icon)
        iconLabel.photo = icon
        iconLabel.config(bg='#141414')
        iconLabel.grid(row=0,column=0,sticky="nsew")
        titleLabel = Label(titleBar, text='ALDOWNLOADMANAGER', fg='#909090', bg='#141414', font=appHighlightFont)
        titleLabel.grid(row=0,column=1,sticky="nsew")
        closeButton = Button(titleBar, text="x", bg='#141414', fg="#909090", borderwidth=0, command=root.destroy, font=appHighlightFont)
        closeButton.grid(row=0,column=3,sticky="nsew")
        minimizeButton = Button(titleBar, text="-", bg='#141414', fg="#909090", borderwidth=0, command=hideScreen, font=appHighlightFont)
        minimizeButton.grid(row=0,column=2,sticky="nsew")
        titleBar.grid_columnconfigure(0,weight=1)
        titleBar.grid_columnconfigure(1,weight=75)
        titleBar.grid_columnconfigure(2,weight=1)
        titleBar.grid_columnconfigure(3,weight=1)
        titleBar.pack(side=TOP, fill=X)

        frameInput = Frame(root, relief=RIDGE, borderwidth=0, bg='#333c4e')
        frameInput.pack(fill=BOTH, expand=1)
        
        frameStatus = LabelFrame(root, text="  Information----------------------------------------------------------------------------------", relief=SUNKEN, bg='#16a4fa', borderwidth=0,font=textHighlightFont,fg='white')
        frameStatus.pack(fill=BOTH, expand=1)
        
        frameProgress = Frame(root, relief=GROOVE, borderwidth=0, bg='white')
        frameProgress.pack(fill=BOTH, expand=1)
        
        frameAction = Frame(root, relief=GROOVE, borderwidth=0, bg='white')
        frameAction.pack(fill=BOTH, expand=1)

        labelLink = Label(frameInput, text="Enter URL", font=textHighlightFont,bg='#333c4e',fg='#9cabc4')
        labelLink.pack(fill=X)
        entryLink = Entry(frameInput, textvariable=self.inputLink, font=textFont)
        entryLink.pack(fill=X, expand=1, side=LEFT, padx=10,pady=5)
        
        labelStatus = Label(frameStatus, textvariable=self.statusMessage, justify=LEFT,bg='#16a4fa',fg='white',font=textFont)
        labelStatus.grid(row=1, column=0, sticky=W)
        labelSpeed = Label(frameStatus, textvariable=self.speedMessage, justify=LEFT,bg='#16a4fa',fg='white',font=textFont)
        labelSpeed.grid(row=2, column=0, sticky=W)
        labelSize = Label(frameStatus, textvariable=self.sizeMessage, justify=LEFT,bg='#16a4fa',fg='white',font=textFont)
        labelSize.grid(row=3, column=0, sticky=W)
        labelTime = Label(frameStatus, textvariable=self.timeMessage, justify=LEFT,bg='#16a4fa',fg='white',font=textFont)
        labelTime.grid(row=4, column=0, sticky=W)
        labelDestination = Label(frameStatus, textvariable=self.destinationMessage, justify=LEFT,bg='#16a4fa',fg='white',font=textFont)
        labelDestination.grid(row=5, column=0, sticky=W)

        style = ttk.Style()
        style.theme_use('clam')
        style.configure("bar.Horizontal.TProgressbar", troughcolor='white', bordercolor='#16a4fa', background='#16a4fa', lightcolor='#16a4fa', darkcolor='#16a4fa')
        progress = ttk.Progressbar(frameProgress, style="bar.Horizontal.TProgressbar", orient=HORIZONTAL, length=700, mode='determinate')
        progress.pack(fill=X, expand=1,padx=10, pady=7)
        
        downloadButton = Button(frameAction, text="DOWNLOAD", command=lambda: startDownloading(), width=16, height=2, fg="white", bd=0, bg='#16a4fa', font=textFont)
        downloadButton.grid(row=1,column=1,padx=20)
        pauseButton = Button(frameAction, state=DISABLED, text="PAUSE", width=16, height=2, fg="white",bd=0, bg='#16a4fa', font=textFont)
        pauseButton.grid(row=1,column=2,padx=20)
        stopButton = Button(frameAction, state=DISABLED, text="STOP", width=16, height=2, fg="white",bd=0, bg='#16a4fa', font=textFont)
        stopButton.grid(row=1,column=3,padx=20)
        clearButton = Button(frameAction, text="CLEAR", command=lambda: clearReset(), width=16, height=2, fg="white",bd=0, bg='#16a4fa', font=textFont)
        clearButton.grid(row=1,column=4,padx=20)

        entryLink.bind("<Button-3>", doPopup)

        titleBar.bind("<B1-Motion>", callback)
        titleBar.bind("<Button-3>", showScreen)
        titleBar.bind("<Map>", screenAppear)

        root.mainloop()
        root.quit()

if __name__ == "__main__":
    AlDownloadManager() 
    sys.exit()