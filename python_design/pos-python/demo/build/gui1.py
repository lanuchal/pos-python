
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\anucha\Desktop\produtions\pos-mini\pos-python\python_design\pos-python\demo\build\assets\frame1")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1024x600")
window.configure(bg = "#252525")


canvas = Canvas(
    window,
    bg = "#252525",
    height = 600,
    width = 1024,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    512.0,
    297.0,
    image=image_image_1
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=10.0,
    y=10.0,
    width=80.0,
    height=40.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=667.0,
    y=533.0,
    width=110.0,
    height=58.3333740234375
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=787.0,
    y=533.0,
    width=105.0,
    height=57.66670227050781
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
button_4.place(
    x=903.0,
    y=533.0,
    width=110.0,
    height=57.66670227050781
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_5 clicked"),
    relief="flat"
)
button_5.place(
    x=664.0,
    y=467.0,
    width=113.0,
    height=45.0
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_6 clicked"),
    relief="flat"
)
button_6.place(
    x=782.0,
    y=466.0,
    width=114.0,
    height=45.0
)

button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_7 clicked"),
    relief="flat"
)
button_7.place(
    x=901.0,
    y=466.0,
    width=114.0,
    height=45.0
)

button_image_8 = PhotoImage(
    file=relative_to_assets("button_8.png"))
button_8 = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_8 clicked"),
    relief="flat"
)
button_8.place(
    x=664.0,
    y=417.0,
    width=173.0,
    height=45.0
)

button_image_9 = PhotoImage(
    file=relative_to_assets("button_9.png"))
button_9 = Button(
    image=button_image_9,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_9 clicked"),
    relief="flat"
)
button_9.place(
    x=842.0,
    y=417.0,
    width=173.0,
    height=45.0
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    839.0,
    236.0,
    image=image_image_2
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    873.5,
    94.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#EBEBEB",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=736.0,
    y=73.0,
    width=275.0,
    height=40.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    840.0,
    175.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#EBEBEB",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=669.0,
    y=158.0,
    width=342.0,
    height=32.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    840.0,
    252.0,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#EBEBEB",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=669.0,
    y=235.0,
    width=342.0,
    height=32.0
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    723.0,
    332.0,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#EBEBEB",
    fg="#000716",
    highlightthickness=0
)
entry_4.place(
    x=669.0,
    y=312.0,
    width=108.0,
    height=38.0
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    852.0,
    332.0,
    image=entry_image_5
)
entry_5 = Entry(
    bd=0,
    bg="#EBEBEB",
    fg="#000716",
    highlightthickness=0
)
entry_5.place(
    x=798.0,
    y=312.0,
    width=108.0,
    height=38.0
)

entry_image_6 = PhotoImage(
    file=relative_to_assets("entry_6.png"))
entry_bg_6 = canvas.create_image(
    969.0,
    332.0,
    image=entry_image_6
)
entry_6 = Entry(
    bd=0,
    bg="#EBEBEB",
    fg="#000716",
    highlightthickness=0
)
entry_6.place(
    x=928.0,
    y=312.0,
    width=82.0,
    height=38.0
)
window.resizable(False, False)
window.mainloop()
