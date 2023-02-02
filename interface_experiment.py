from operator import le
from tkinter import *
from tkinter import filedialog
from tkinter import font
from turtle import width
import os
from PIL import ImageTk, Image
from tkinter.filedialog import asksaveasfile
import tkinter as tk
from tkinter import ttk

 
LARGEFONT =("Dosis-Medium", 24)
  
class tkinterApp(tk.Tk):
     
    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
         
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)
         
        # creating a container
        container = tk.Frame(self) 
        container.pack(side = "top", fill = "both", expand = True)
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        # initializing frames to an empty array
        self.frames = {} 
  
        # iterating through a tuple consisting
        # of the different page layouts
        for F in (StartPage, Page1):
  
            frame = F(container, self)
  
            # initializing frame of that object from
            # startpage, page1, page2 respectively with
            # for loop
            self.frames[F] = frame
  
            frame.grid(row = 0, column = 0, sticky ="nsew")
  
        self.show_frame(StartPage)
  
    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
  
# first window frame startpage
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.Frame.configure(self, bg='#0D0628') 
        # label of frame Layout 2
        
        
     
        # putting the button in its place by
        # using grid
        
     

        menu= StringVar()
        menu.set("Please select what do you want to do")
      
        #Create a dropdown Menu
        drop= OptionMenu(self, menu, "Analyze fibre's response with field sample", "Calibration")
        drop.config(font = LARGEFONT)
        drop.grid(row=2, column=0, padx = 10, pady = 10)
        e = Text(self, width=30, height = 6, bg = "#333333", fg = "#FFFFFF", relief = FLAT, font = LARGEFONT)
        e.grid(row=1, column=0)

        

        
            
        def openFile():
            openFile.tfiles = filedialog.askopenfilenames(initialdir = "/Downloads", title = "Select your data", filetypes = ((".txt", "*.txt"), ("all files", "*.*")), font = LARGEFONT)
            openFile.tfiles = list(openFile.tfiles)
            
            if menu.get()=="Calibration":
                iterator_file=0
                for i in openFile.tfiles:
                    data = open(i, "r")
                    #e.insert(INSERT, i+"\n")
                    dataLines=data.readlines()
                    filename = ""
                    for k in reversed(range(0,len(i)-1)):
                        if i[k]== "/":
                            j = k+1
                            break
                    for l in range (j, len(i)):
                        filename+=i[l]
                    #filename = "sucrose_10_"+str(iterator_file*2)+"00ul_sucrose_40_Lower.txt"
                    data = open(filename, "w")
                    data.writelines(dataLines)
                    #e.insert(INSERT, filename+" and i is "+i+"\n")
                    iterator_file+=1
                e.insert(INSERT, "Your data has been successfully uploaded\n")
                data.close()
                fileScript = open("Script_Aida.m", "r")
                script=fileScript.readlines() 
            else:
                iterator_file=0
                for i in openFile.tfiles:
                    data = open(i, "r")
                    #e.insert(INSERT, i+"\n")
                    dataLines=data.readlines()
                    filename=""
                    for k in reversed(range(0,len(i)-1)):
                        if i[k]== "/":
                            j = k+1
                            break
                    for l in range (j, len(i)):
                        filename+=i[l]
                    data = open(filename, "w")
                    data.writelines(dataLines)
                    iterator_file+=1
                e.insert(INSERT, "Your data has been successfully uploaded\n")
                data.close()
                size = len(openFile.tfiles)
                if size>15:
                    e.insert(INSERT, size)
                    e.insert(INSERT, "Number of selected items exceeds the limit of 15\n")
                
                else:
                    fileScript = open("BR_A27_old.m", "r")
                    script=fileScript.readlines()   
                    
                    temp="mg_num="
                    nums = []
                    for i in range(0, size):
                        if i==0:
                            nums.append(0.5)
                        else:
                            nums.append(i)
                    temp+=str(nums)+";\n"
                    script[5]=temp

                    for i in range(19, 34):
                        if size<=2:
                            #e.insert(INSERT, "size is "+str(size)+" i is "+str(i) +"\n")
                            if size==2:
                                script[i]=script[i][0:len(script[i])]
                                script[i]+="]';\n\n"
                            else:
                                script[i]=""
                        size-=1


                
            fileScript = open("final.m", "w")
            fileScript.writelines(script)  
            fileScript.close()
                
            
        
        
        uploadButton = Button(self, text = "Select your data", command = openFile, bg='#0D0628', width=14, height=2, font = LARGEFONT)
        uploadButton.grid(row=3, column=0, padx = 10, pady = 10)
        proceedButton = Button(self, text = "Proceed", bg='#0D0628', width=10, height=2, command = lambda:controller.show_frame(Page1), font = LARGEFONT)
        proceedButton.grid(row=4, column=0, padx = 10, pady = 10)
        
    #lambda : controller.show_frame(Page1)

        
  
          
  
  
# second window frame page1
class Page1(tk.Frame):
     
    def __init__(self, parent, controller):
         
        tk.Frame.__init__(self, parent)
        tk.Frame.configure(self, bg='#0D0628') 
        #tk.Frame.grid(self,columnspan=3)


        goBack = Button(self, text ="Go back", command = lambda : controller.show_frame(StartPage), font = LARGEFONT)
        goBack.grid(row = 1, column = 1, padx = 10, pady = 10)
        def image(imagename):
            img = ImageTk.PhotoImage(Image.open(imagename))
            label = Label(self, image = img)
            label.photo = img
            label.grid(row=5, column=1)
            return 
        def textRes():
            resultFile = open("calibration_results.txt", "r")
            text=resultFile.read()
            resultFile.close()
            results = Label(self, text=text, background='#0D0628', foreground='#FFFFFF', font = LARGEFONT)
            results.grid(row=4, column=1)
            resultFile = open("calibration_results.txt", "w")
            resultFile.write("")
            resultFile.close()
            return 
        def analyze():
            import scripts as s
            s.script()
            textRes()
            return image("ball_resonator.png")
        
        
            
        analyzeButton = Button(self, text = "Analyze ->", bg='#0D0628', width=10, height=2, command = analyze, font = LARGEFONT)
        analyzeButton.grid(row=3, column=1, padx = 10, pady = 10)
        
        #button2.grid(row = 2, column = 1, padx = 10, pady = 10)
        
        #label = ttk.Label(self)
        #label.grid(row = 0, column = 3, padx = 10, pady = 10)
  
        # button to show frame 2 with text
        # layout2
        #button1 = ttk.Button(self, text ="StartPage",
                            #command = lambda : controller.show_frame(StartPage))
     
        # putting the button in its place
        # by using grid
        #button1.grid(row = 1, column = 1, padx = 10, pady = 10)
    
        
  

  
  
# Driver Code
app = tkinterApp()
app.title("Viraless")
#app.resizable(False, False)
#app.geometry('800x600')
app.mainloop()