
from tkinter import * 

from tkinter import messagebox

root=Tk()

root.title("Geometry Error")

root.geometry("600x600")

input_box = Entry(root)

input_box.pack()

def addition(): 
    
    number = 5
    
    get_input = input_box.get()
    
    try: 
        
        print(number + get_input)
        
    except(TypeError):
        
        messagebox.showinfo("Error", "Cannot add two differne tdata types : string and integer")
        
button = Button(root, text="Addition", command = addition)

button.pack()

root.mainloop()