import tkinter as tk
from tkinter import ttk
from menu import  create_menu

def reload_page(page_name):
    if page_name in pages:
        pages[page_name] = globals()[f"create_{page_name}"](root, switch_to_page)
    return pages[page_name]

def switch_to_page(page_name):
    global current_page
    if current_page is not None:
        current_page.grid_remove()
    current_page = reload_page(page_name)
    current_page.grid(column=0, row=0, padx=0, pady=0, sticky="nsew")


root = tk.Tk()
root.title("face scan")
root.geometry("1024x600")
#for rasberry pi
# root.attributes('-fullscreen', True) 
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)


pages = {
    "menu": create_menu(root, switch_to_page),
}

current_page = None
current_page = pages["menu"]
current_page.grid(column=0, row=0, padx=0, pady=0, sticky="nsew")

root.mainloop()