
from pathlib import Path
from tkinter import Canvas, Entry, Text, Button, PhotoImage, ttk

ASSETS_DIR_NAME = "assets"
ASSETS_FRAME_NAME = "setting"
ASSETS_PATH = Path(__file__).resolve().parent / ASSETS_DIR_NAME / ASSETS_FRAME_NAME

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path) 

def create_setting(root, switch_to_page):
    setting_page = ttk.Frame(root)
    
    canvas = Canvas(
        setting_page,
        bg="#252525",
        height=600,
        width=1024,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )
    canvas.place(x=0, y=0)
    
    # Load button images
    button_options = {
        "borderwidth": "0",
        "highlightthickness": "0",
        "relief":"flat",
        "cursor":"hand2"
    }

    ################## HEADER
    btn_back_image = PhotoImage(file=relative_to_assets("button_1.png"))
    btn_back = Button( setting_page, image=btn_back_image,**button_options,command=lambda: switch_to_page("menu"))
    btn_back.image = btn_back_image
    btn_back.place(x=10.0,y=10.0,width=80.0,height=40.0)

    image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(512.0,30.0,image=image_image_1)
    canvas.image_1 = image_image_1

    ################## END HEADER

    image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(511.0,267.0,image=image_image_2)
    canvas.image_2 = image_image_2

    entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(341.5,182.5,image=entry_image_1)
    canvas.entry_bg_1 = image_image_2


    entry_options = {
        # "borderwidth": "1",
        "font": ("Times", 24),
        "bd": "0",
        "fg": "#000716",
        "bg": "#D9D9D9",
        "highlightthickness": "0"
    }


    entry_store_name_image = PhotoImage(file=relative_to_assets("entry_1.png"))
    entry_store_name_bg = canvas.create_image(341.5,182.5,image=entry_store_name_image)
    canvas.entry_store_name_bg = entry_store_name_bg
    entry_store_name = Entry(setting_page,**entry_options)
    entry_store_name.place(x=188.0,y=162.0,width=307.0,height=39.0)


    entry_store_tax_image = PhotoImage(file=relative_to_assets("entry_2.png"))
    entry_store_tax_bg = canvas.create_image(341.5,182.5,image=entry_store_tax_image)
    canvas.entry_store_tax_bg = entry_store_tax_bg
    entry_store_tax = Entry(setting_page,**entry_options)
    entry_store_tax.place(x=531.0,y=164.0,width=307.0,height=39.0)

    
    entry_store_tel_image = PhotoImage(file=relative_to_assets("entry_3.png"))
    entry_store_tel_bg = canvas.create_image(341.5,182.5,image=entry_store_tel_image)
    canvas.entry_store_tel_bg = entry_store_tel_bg
    entry_store_tel = Entry(setting_page,**entry_options)
    entry_store_tel.place(x=187.0,y=262.0,width=307.0,height=39.0)

    entry_store_mail_image = PhotoImage(file=relative_to_assets("entry_4.png"))
    entry_store_mail_bg = canvas.create_image(341.5,182.5,image=entry_store_mail_image)
    canvas.entry_store_mail_bg = entry_store_mail_bg
    entry_store_mail = Entry(setting_page,**entry_options)
    # entry_store_mail.place(x=186.0,y=364.0,width=652.0,height=39.0)
    entry_store_mail.place(x=531.0,y=262.0,width=307.0,height=39.0)
    
    entry_store_address_image = PhotoImage(file=relative_to_assets("entry_5.png"))
    entry_store_address_bg = canvas.create_image(341.5,182.5,image=entry_store_address_image)
    canvas.entry_store_address_bg = entry_store_address_bg
    entry_store_address = Entry(setting_page,**entry_options)
    # entry_store_address.place(x=531.0,y=262.0,width=307.0,height=39.0)
    entry_store_address.place(x=186.0,y=364.0,width=652.0,height=39.0)

    entry_val = {
        'store_name': entry_store_name,
        'store_tax': entry_store_tax,
        'store_tel': entry_store_tel,
        'store_mail': entry_store_mail,
        'store_address': entry_store_address
    }
    
    btn_save_image = PhotoImage(file=relative_to_assets("button_2.png"))
    btn_save = Button( setting_page, image=btn_save_image,**button_options,command=lambda: save(entry_val))
    btn_save.image = btn_save_image
    btn_save.place(x=176.0,y=439.0,width=670.0,height=87.0)

    return setting_page

def save(entry_val):
    entry_val_set = {
        'store_name': entry_val['store_name'].get(),
        'store_tax': entry_val['store_tax'].get(),
        'store_tel': entry_val['store_tel'].get(),
        'store_mail': entry_val['store_mail'].get(),
        'store_address': entry_val['store_address'].get()
    }
    print(entry_val_set)
