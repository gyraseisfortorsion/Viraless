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

 
FONT =("Dosis-Medium", 24)
  
class tkinterApp(tk.Tk):
     

    def __init__(self, *args, **kwargs):
         
  
        tk.Tk.__init__(self, *args, **kwargs)
         

        container = tk.Frame(self) 
        container.pack(side = "top", fill = "both", expand = True)
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
        container.config(height=1500, width=600)

        self.frames = {} 
  
  
        for F in (StartPage, Page1):
  
            frame = F(container, self)
  
            
            self.frames[F] = frame
  
            frame.grid(row = 0, column = 0, sticky ="nsew")
            frame.config(height=1500, width=600)
           
  
        self.show_frame(StartPage)
  
   
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
  

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.Frame.configure(self, bg='#0D0628') 
        tk.Frame.config(self, height=1500, width=600)
   
        
     

        menu= StringVar()
        menu.set("Please select what do you want to do")
        
        #Create a dropdown Menu
        drop= OptionMenu(self, menu, "Analyze fibre's response with field sample", "Calibration")
        dropFont=("Dosis-Medium", 18)
        drop.config(font = dropFont, foreground="#FFFFFF", bg='#0D0628', highlightbackground='#0D0628')
        drop.grid(row=0, padx = 10, pady = 10, sticky="nsew")

        e = Text(self, width=30, height = 6, bg = "#333333", fg = "#FFFFFF", relief = FLAT, font = FONT)

        e.grid(row=1, padx = 10, pady = 10, sticky="nsew")
      
        def openFile():
            openFile.tfiles = filedialog.askopenfilenames(initialdir = "/Downloads", title = "Select your data", filetypes = ((".txt", "*.txt"), ("all files", "*.*")))
            
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

                    data = open(filename, "w")
                    data.writelines(dataLines)

                    iterator_file+=1
                e.insert(INSERT, "Your data has been successfully uploaded\n")
                data.close()
                fileScript = open("Script_Calibration.m", "r")
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

                            if size==2:
                                script[i]=script[i][0:len(script[i])]
                                script[i]+="]';\n\n"
                            else:
                                script[i]=""
                        size-=1


                
            fileScript = open("final.m", "w")
            fileScript.writelines(script)  
            fileScript.close()

        uploadButton = Button(self, text = "Select your data", command = openFile, width=14, height=2, font = FONT, highlightbackground="#BB6CE6")

        uploadButton.grid(row=3, padx = 10, pady = 10, sticky="nsew")
        proceedButton = Button(self, text = "Proceed", width=10, height=2, command = lambda:controller.show_frame(Page1), font = FONT,  highlightbackground="#BB6CE6")

        proceedButton.grid(row=5, padx = 10, pady = 10, sticky="nsew")


        
  
          
  
class Page1(tk.Frame):
     
    def __init__(self, parent, controller):
         
        tk.Frame.__init__(self, parent)
        tk.Frame.configure(self, bg='#0D0628') 
        goBack = Button(self, text ="Go back", width=30, height=2, command = lambda : controller.show_frame(StartPage), font = FONT, highlightbackground= "#BB6CE6")
        goBack.grid(row=1,padx = 10, pady = 10, sticky="nsew")
        def image(imagename):
            img = ImageTk.PhotoImage(Image.open(imagename))
            label = Label(self, image = img)
            label.photo = img
            label.grid(row=5, padx = 10, pady = 10, sticky="nsew")
            filenamee="sucrose_10_"
            filenamee2="00ul.txt"
            for i in range(0, 6):
                calibFile=filenamee+str(i*2)+filenamee2
                calibrationData=open(calibFile, "w")
                calibrationData.write("")
                calibrationData.close()
            filenamee="_1_Lower.txt"
            for i in range(0, 15):
                if i==0:
                    filenamee="0.5"+filenamee
                else:
                    filenamee=str(i)+filenamee
                
                exData=open(filenamee, "w")
                exData.write("")
                exData.close()
                filenamee="_1_Lower.txt"
            return 
        def textRes():
            resultFile = open("calibration_results.txt", "r")
            text=resultFile.read()
            resultFile.close()
            results = Label(self, text=text, background='#0D0628', foreground='#FFFFFF', font = FONT)
            results.grid(row=4, padx = 10, pady = 10, sticky="nsew")
            resultFile = open("calibration_results.txt", "w")
            resultFile.write("")
            resultFile.close()
            return 
        def analyze():
            import scripts as s
            s.script()
            textRes()
            return image("ball_resonator.png")
        
        
            
        analyzeButton = Button(self, text = "Analyze ->", bg='#0D0628', width=30, height=2, command = analyze, font = FONT, highlightbackground="#BB6CE6")
        analyzeButton.grid(row=3, padx = 10, pady = 10, sticky="nsew")
        

    
        
  

app = tkinterApp()
app.title("Viraless")

app.mainloop()


