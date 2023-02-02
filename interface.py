import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry('1200x800')
root.title("Test")

tab_frame = ttk.Notebook(root)
tab_frame.pack(fill="both", expand=1) # used pack() instead of grid()

s = ttk.Style()
s.configure('test_red.TFrame', background='red')
s.configure('test_green.TFrame', background='green')
s.configure('test_blue.TFrame', background='blue')

tab1 = ttk.Frame(tab_frame, style='test_red.TFrame')
tab2 = ttk.Frame(tab_frame, style='test_blue.TFrame')

tab_frame.add(tab1, text='Tab1')
tab_frame.add(tab2, text='Tab2')

### frames in tab
label_frame1 = ttk.Labelframe(tab1, text='Label1', style='test_green.TFrame')
label_frame1.place(x=0, y=0, relwidth=1, relheight=0.5)

label_frame2 = ttk.Labelframe(tab1, text='Label2', style='test_blue.TFrame')
label_frame2.place(x=0, rely=0.5, relwidth=1, relheight=0.5)

root.mainloop()