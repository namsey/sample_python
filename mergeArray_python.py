import tkinter as tk
from tkinter import *

class Check_Box():
    def __init__(self):
        self.main_window = tk.Tk()
        self.main_window.title("Check Box")
        self.main_window.geometry('500x500')
        self.main_window.config(bg = "white")

        self.text = tk.StringVar()
        self.text_box = Entry(self.main_window, textvariable = self.text, bg = "white", width = 50)
        self.text_box.place(x = 0, y = 0)

        self.checkbox = tk.IntVar()
        self.check_box = Checkbutton(self.main_window, text = "Sample Checkbox", variable = self.checkbox, bg = "white")
        self.check_box.place(x = 150, y = 200)

        self.get_st = tk.Button(self.main_window, text = "Get State", bg = "white", command = self.get_State)
        self.get_st.place(x = 50, y = 80)
        self.set_st = tk.Button(self.main_window, text = "Set State", bg = "white", command = self.set_State)
        self.set_st.place(x = 180, y = 80)
        self.get_lb = tk.Button(self.main_window, text = "Get Label", bg = "white", command = self.get_Label)
        self.get_lb.place(x = 310, y = 80)

    def get_State(self):
        state = self.checkbox.get()
        if state == 1:
            self.text.set("State of Checkbox : Checked")
        else:
            self.text.set("State of Checkbox : Un-Checked")
    
    def set_State(self):
        self.text.set("State of Checkbox changed from ")
        state = self.checkbox.get()
        if state == 1:
            self.checkbox.set(0)
            self.text.set(self.text.get() + "Checked to Un-Checked")
        else:
            self.checkbox.set(1)
            self.text.set(self.text.get() + "Un-Checked to Checked")

    def get_Label(self):
        self.text.set("Label of the checkbox is : " + self.check_box.cget("text"))

if __name__ == "__main__":
    Check_Box()
    mainloop()
