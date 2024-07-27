import code
from  tkinter import *
import tkinter as tk
from tkinter import filedialog
from tkinter import Text

window = tk.Tk()
window.title("osman site TEXT Editor")
window.geometry("300x300")
window.configure(bg="#CFF5E9")

def open_file():
    file_path = filedialog.askopenfilename(filetypes=(("Text File","*.txt" ),("All File","*.*")))
    
    if file_path:
        with open(file_path,"+r",encoding="utf-8") as file:
            cotent= file.read()
            tex_area.delete(1.0, tk.END)
            tex_area.insert(tk.END, cotent)
            
def save_file():
    file_path = filedialog.asksaveasfilename(filetypes=(("Text File","*.txt" ),("All File","*.*")))
    
    if file_path:
        with open(file_path,"w",encoding="utf-8") as file:
            cotent= tex_area.get(1.0,tk.END)
            file.write(cotent)           
             


open_button = tk.Button(window,text=" open file ",font=20 ,bg="orange",command=open_file)
open_button.pack(side="left",anchor="nw",padx=10,pady=10)

save_button = tk.Button(window,text=" save file ",font=20 ,bg="#2FF0B8" ,command=save_file)
save_button.pack(side="left",anchor="nw",padx=10,pady=10)

tex_area =Text(window,wrap="word")
tex_area.pack(expand=True, fill='both')


window.mainloop()
