
from pathlib import Path
from tkinter import Canvas, Button, PhotoImage, ttk

ASSETS_DIR_NAME = "assets"
ASSETS_FRAME_NAME = "menu"
ASSETS_PATH = Path(__file__).resolve().parent / ASSETS_DIR_NAME / ASSETS_FRAME_NAME

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path) 

def create_menu(root, switch_to_page):
    menu_page = ttk.Frame(root)
    
    canvas = Canvas(
        menu_page,
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

    btn_sell_image = PhotoImage(file=relative_to_assets("button_1.png"))
    btn_sell = Button( menu_page, image=btn_sell_image,**button_options,command=lambda: switch_to_page("order"))
    btn_sell.image = btn_sell_image
    btn_sell.place(x=93.0, y=87.0, width=355.0, height=180.0)

    btn_stock_img = PhotoImage(file=relative_to_assets("button_2.png"))
    btn_stock = Button( menu_page, image=btn_stock_img,**button_options,command=lambda: switch_to_page("stock"))
    btn_stock.image = btn_stock_img
    btn_stock.place(x=579.0,y=87.0,width=355.0,height=180.0)


    btn_report_img = PhotoImage(file=relative_to_assets("button_4.png"))
    btn_report = Button( menu_page, image=btn_report_img,**button_options,command=lambda: switch_to_page("report"))
    btn_report.image = btn_report_img
    btn_report.place(x=93.0,y=341.0,width=355.0,height=180.0)

    btn_setting_img = PhotoImage(file=relative_to_assets("button_3.png"))
    btn_setting = Button( menu_page, image=btn_setting_img,**button_options,command=lambda: switch_to_page("setting"))
    btn_setting.image = btn_setting_img
    btn_setting.place(x=579.0,y=341.0,width=355.0,height=180.0)


    return menu_page
