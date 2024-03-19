import tkinter as tk
from tkinter import ttk
from pages.menu import  create_menu
from stock import  create_stock
from pages.setting import  create_setting
from pages.report import  create_report

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
root.title("pos-mini")
root.configure(bg = "#252525")
###################################
# comment for rasberry pi
root.geometry("1024x600")

#use for rasberry pi
# root.attributes('-fullscreen', True) 
##############################
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)


pages = {
    "menu": create_menu(root, switch_to_page),
    "stock": create_stock(root, switch_to_page),
    "setting": create_setting(root, switch_to_page),
    "report": create_report(root, switch_to_page),
}

current_page = None
current_page = pages["menu"]
current_page.grid(column=0, row=0, padx=0, pady=0, sticky="nsew")

root.resizable(False, False)
root.mainloop()