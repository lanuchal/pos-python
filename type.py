import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=1024
        height=600
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)




        GButton_101=tk.Button(root)
        GButton_101["bg"] = "#009688"
        GButton_101["borderwidth"] = "0px"
        ft = tkFont.Font(family='Times',size=16)
        GButton_101["font"] = ft
        GButton_101["fg"] = "#ffffff"
        GButton_101["justify"] = "center"
        GButton_101["text"] = "เพิ่ม"
        GButton_101.place(x=675,y=432,width=110,height=45)
        GButton_101["command"] = self.GButton_101_command

        GButton_425=tk.Button(root)
        GButton_425["bg"] = "#ffb800"
        GButton_425["borderwidth"] = "0px"
        ft = tkFont.Font(family='Times',size=16)
        GButton_425["font"] = ft
        GButton_425["fg"] = "#ffffff"
        GButton_425["justify"] = "center"
        GButton_425["text"] = "แก้ไข"
        GButton_425.place(x=792,y=432,width=110,height=45)
        GButton_425["command"] = self.GButton_425_command

        GButton_213=tk.Button(root)
        GButton_213["bg"] = "#cc0000"
        GButton_213["borderwidth"] = "0px"
        ft = tkFont.Font(family='Times',size=16)
        GButton_213["font"] = ft
        GButton_213["fg"] = "#ffffff"
        GButton_213["justify"] = "center"
        GButton_213["text"] = "ลบ"
        GButton_213.place(x=910,y=432,width=110,height=45)
        GButton_213["command"] = self.GButton_213_command



    def GButton_173_command(self):
        print("command")


    def GButton_101_command(self):
        print("command")


    def GButton_425_command(self):
        print("command")


    def GButton_213_command(self):
        print("command")


    def GButton_77_command(self):
        print("command")


    def GButton_664_command(self):
        print("command")


    def GButton_250_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
