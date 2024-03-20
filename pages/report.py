
from pathlib import Path
from tkinter import Canvas, Entry, Text, Button, PhotoImage, ttk
from tkcalendar import DateEntry

ASSETS_DIR_NAME = "assets"
ASSETS_FRAME_NAME = "report"
ASSETS_PATH = Path(__file__).resolve().parent / ASSETS_DIR_NAME / ASSETS_FRAME_NAME

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path) 

def create_report(root, switch_to_page):
    report_page = ttk.Frame(root)
    
    canvas = Canvas(
        report_page,
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
    btn_back = Button( report_page, image=btn_back_image,**button_options,command=lambda: switch_to_page("menu"))
    btn_back.image = btn_back_image
    btn_back.place(x=10.0,y=10.0,width=80.0,height=40.0)

    image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(512.0,30.0,image=image_image_1)
    canvas.image_1 = image_image_1

    ################## END HEADER

    ############# report ##############
    image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(252.0,121.0,image=image_image_2)
    canvas.image_2 = image_image_2

    entry_options = {
        "font": ("Times", 20),
        "borderwidth ":"0"
    }
    
    entry_day_start = DateEntry(report_page,**entry_options,showweeknumbers=False,date_pattern="dd/mm/y",locale="th_TH")
    entry_day_start.place(x=28.0,y=127.0,width=187.0,height=28.0)

    
    entry_day_end = DateEntry(report_page,**entry_options,showweeknumbers=False,date_pattern="dd/mm/y",locale="th_TH")
    entry_day_end.place(x=284.0,y=127.0,width=187.0,height=28.0)


    btn_top_image = PhotoImage(file=relative_to_assets("button_7.png"))
    btn_top = Button( report_page, image=btn_top_image,**button_options,command=lambda: print("btn_top"))
    btn_top.image = btn_top_image
    btn_top.place(x=15.0,y=191.0,width=476.0,height=87.0)

    
    btn_each_day_image = PhotoImage(file=relative_to_assets("button_4.png"))
    btn_each_day = Button( report_page, image=btn_each_day_image,**button_options,command=lambda: print("btn_each_day"))
    btn_each_day.image = btn_each_day_image
    btn_each_day.place(x=15.0,y=294.0,width=476.0,height=87.0)
    
    btn_profit_all_image = PhotoImage(file=relative_to_assets("button_5.png"))
    btn_profit_all = Button( report_page, image=btn_profit_all_image,**button_options,command=lambda: print("btn_profit_all"))
    btn_profit_all.image = btn_profit_all_image
    btn_profit_all.place(x=15.0,y=395.0,width=476.0,height=87.0)

    
    btn_profit_order_image = PhotoImage(file=relative_to_assets("button_6.png"))
    btn_profit_order = Button( report_page, image=btn_profit_order_image,**button_options,command=lambda: print("btn_profit_order"))
    btn_profit_order.image = btn_profit_order_image
    btn_profit_order.place(x=15.0,y=496.0,width=476.0,height=87.0)


    btn_day_all_image = PhotoImage(file=relative_to_assets("button_2.png"))
    btn_day_all = Button( report_page, image=btn_day_all_image,**button_options,command=lambda: print("btn_day_all"))
    btn_day_all.image = btn_day_all_image
    btn_day_all.place(x=530.0,y=393.0,width=476.0,height=87.0)


    btn_month_all_image = PhotoImage(file=relative_to_assets("button_3.png"))
    btn_month_all = Button( report_page, image=btn_month_all_image,**button_options,command=lambda: print("btn_month_all"))
    btn_month_all.image = btn_month_all_image
    btn_month_all.place(x=530.0,y=496.0,width=476.0,height=87.0)

    ############# stock ##############
    image_image_3 = PhotoImage(file=relative_to_assets("image_3.png"))
    image_3 = canvas.create_image(768.0,222.0,image=image_image_3)
    canvas.image_3 = image_image_3
    
    btn_stock_all_image = PhotoImage(file=relative_to_assets("button_8.png"))
    btn_stock_all = Button( report_page, image=btn_stock_all_image,**button_options,command=lambda: print("btn_stock_all"))
    btn_stock_all.image = btn_stock_all_image
    btn_stock_all.place(x=538.0,y=184.0,width=459.0,height=87.0)

    btn_stock_limit_image = PhotoImage(file=relative_to_assets("button_8.png"))
    btn_stock_limit = Button( report_page, image=btn_stock_limit_image,**button_options,command=lambda: print("btn_stock_limit"))
    btn_stock_limit.image = btn_stock_limit_image
    btn_stock_limit.place(x=538.0,y=283.0,width=459.0,height=87.0)
    


    # button_image_8 = PhotoImage(
    # file=relative_to_assets("button_8.png"))
    # button_8 = Button(
    #     image=button_image_8,
    #     borderwidth=0,
    #     highlightthickness=0,
    #     command=lambda: print("button_8 clicked"),
    #     relief="flat"
    # )
    # button_8.place(
    #     x=538.0,
    #     y=184.0,
    #     width=459.0,
    #     height=87.0
    # )
    # entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
    # entry_bg_1 = canvas.create_image(341.5,182.5,image=entry_image_1)
    # canvas.entry_bg_1 = image_image_2


    # entry_options = {
    #     # "borderwidth": "1",
    #     "font": ("Times", 24),
    #     "bd": "0",
    #     "fg": "#000716",
    #     "bg": "#D9D9D9",
    #     "highlightthickness": "0"
    # }


    # entry_day_start_image = PhotoImage(file=relative_to_assets("entry_1.png"))
    # entry_day_start_bg = canvas.create_image(341.5,182.5,image=entry_day_start_image)
    # canvas.entry_day_start_bg = entry_day_start_bg
    # entry_day_start = Entry(report_page,**entry_options)
    # entry_day_start.place(x=188.0,y=162.0,width=307.0,height=39.0)


    # entry_store_tax_image = PhotoImage(file=relative_to_assets("entry_2.png"))
    # entry_store_tax_bg = canvas.create_image(341.5,182.5,image=entry_store_tax_image)
    # canvas.entry_store_tax_bg = entry_store_tax_bg
    # entry_store_tax = Entry(report_page,**entry_options)
    # entry_store_tax.place(x=531.0,y=164.0,width=307.0,height=39.0)

    
    # entry_store_tel_image = PhotoImage(file=relative_to_assets("entry_3.png"))
    # entry_store_tel_bg = canvas.create_image(341.5,182.5,image=entry_store_tel_image)
    # canvas.entry_store_tel_bg = entry_store_tel_bg
    # entry_store_tel = Entry(report_page,**entry_options)
    # entry_store_tel.place(x=187.0,y=262.0,width=307.0,height=39.0)

    # entry_store_mail_image = PhotoImage(file=relative_to_assets("entry_4.png"))
    # entry_store_mail_bg = canvas.create_image(341.5,182.5,image=entry_store_mail_image)
    # canvas.entry_store_mail_bg = entry_store_mail_bg
    # entry_store_mail = Entry(report_page,**entry_options)
    # # entry_store_mail.place(x=186.0,y=364.0,width=652.0,height=39.0)
    # entry_store_mail.place(x=531.0,y=262.0,width=307.0,height=39.0)
    
    # entry_store_address_image = PhotoImage(file=relative_to_assets("entry_5.png"))
    # entry_store_address_bg = canvas.create_image(341.5,182.5,image=entry_store_address_image)
    # canvas.entry_store_address_bg = entry_store_address_bg
    # entry_store_address = Entry(report_page,**entry_options)
    # # entry_store_address.place(x=531.0,y=262.0,width=307.0,height=39.0)
    # entry_store_address.place(x=186.0,y=364.0,width=652.0,height=39.0)

    # entry_val = {
    #     'store_name': entry_day_start,
    #     'store_tax': entry_store_tax,
    #     'store_tel': entry_store_tel,
    #     'store_mail': entry_store_mail,
    #     'store_address': entry_store_address
    # }
    
    # btn_stock_all_image = PhotoImage(file=relative_to_assets("button_2.png"))
    # btn_stock_all = Button( report_page, image=btn_stock_all_image,**button_options,command=lambda: save(entry_val))
    # btn_stock_all.image = btn_stock_all_image
    # btn_stock_all.place(x=176.0,y=439.0,width=670.0,height=87.0)

    return report_page

def save(entry_val):
    entry_val_set = {
        'store_name': entry_val['store_name'].get(),
        'store_tax': entry_val['store_tax'].get(),
        'store_tel': entry_val['store_tel'].get(),
        'store_mail': entry_val['store_mail'].get(),
        'store_address': entry_val['store_address'].get()
    }
    print(entry_val_set)
