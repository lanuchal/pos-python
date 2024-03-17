
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
    
def create_stock(root, switch_to_page):
    stock_page = ttk.Frame(root)
    style = ttk.Style()
    style.configure("stock_page.TFrame") 
    stock_page.configure(style="stock_page.TFrame")
    name_label = ttk.Label(stock_page, text="")
    name_label.pack(pady=10)
    # options common
    btn_options = {
        "borderwidth": "0",
        "font": ("Times", 18),
        "fg": "#ffffff",
        "justify": "center",
        "relief": "raised",
    }
    # end options common

    ##### header
    header_lb_options = {
        "font": ("Times", 22),
        "justify": "center",
        "fg": "#ffffff",
        "bg": "#06335f",
    }
    header_lb = tk.Label(stock_page, **header_lb_options, text="สต็อค / สินค้า")
    header_lb.place(x=0,y=0,width=1024,height=50)

    btn_back_ontion = {
        "borderwidth": "0",
        "font": ("Times", 26),
        "fg": "#ffffff",
        "bg": "#ffb800",
        "justify": "center",
        "relief": "raised",
        "text": "กลับ",
    }
    btn_back = tk.Button(stock_page, **btn_back_ontion, cursor="hand2", command=lambda: switch_to_page("menu"))
    btn_back.place(x=5,y=5,width=70,height=40)
    ##### end header

    #### box layout barcode
    label_product = tk.Label(stock_page,  bg="#393d49")
    label_product.place(x=670,y=50,width=355,height=440)

    lb_product_option = {
        "borderwidth": "0",
        "font": ("Times", 16),
        "fg": "#ffffff",
        "bg": "#393d49",
        "justify": "left",
    }
    label_barcode = tk.Label(stock_page, **lb_product_option ,text="บาร์โค้ดสินค้า")
    label_barcode.place(x=680,y=70,width=333,height=25)
    label_product_name = tk.Label(stock_page, **lb_product_option ,text="ชื่อสินค้า")
    label_product_name.place(x=680,y=150,width=333,height=25)
    label_product_type = tk.Label(stock_page, **lb_product_option ,text="ประเภทสินค้า")
    label_product_type.place(x=680,y=230,width=333,height=25)
    label_product_cost = tk.Label(stock_page, **lb_product_option ,text="ต้นทุน")
    label_product_cost.place(x=680,y=300,width=117,height=30)
    label_product_price = tk.Label(stock_page, **lb_product_option ,text="ราคาขาย")
    label_product_price.place(x=810,y=300,width=120,height=30)
    label_product_amount = tk.Label(stock_page, **lb_product_option ,text="จำนวน")
    label_product_amount.place(x=940,y=300,width=70,height=30)

    entry_options = {
        "borderwidth": "0",
        "font": ("Times", 18),
        "bg": "#ffffff",
        "justify": "left"
    }
    barcode_entry = tk.Entry(stock_page, **entry_options)
    barcode_entry.place(x=680,y=100,width=333,height=40)
    product_name_entry = tk.Entry(stock_page, **entry_options)
    product_name_entry.place(x=680,y=180,width=333,height=40)
    product_type_entry = tk.Entry(stock_page, **entry_options)
    product_type_entry.place(x=680,y=260,width=333,height=35)
    product_cost_entry = tk.Entry(stock_page, **entry_options)
    product_cost_entry.place(x=680,y=330,width=117,height=35)
    product_price_entry = tk.Entry(stock_page, **entry_options)
    product_price_entry.place(x=810,y=330,width=119,height=35)
    product_amount_entry = tk.Entry(stock_page, **entry_options)
    product_amount_entry.place(x=940,y=330,width=71,height=35)


    btn_save = tk.Button(stock_page, **btn_options,bg="#1e9fff", text="บันทึก", cursor="hand2", command=lambda: save_product(barcode_entry, product_name_entry, product_type_entry,product_cost_entry,product_price_entry,product_amount_entry))
    btn_save.place(x=675,y=380,width=345,height=45)

    btn_add = tk.Button(stock_page, **btn_options,bg="#009688", text="เพิ่ม", cursor="hand2", command=lambda: add_product())
    btn_add.place(x=675,y=432,width=110,height=45)

    btn_edit = tk.Button(stock_page, **btn_options,bg="#ffb800", text="แก้ไข", cursor="hand2", command=lambda: edit_product())
    btn_edit.place(x=792,y=432,width=110,height=45)

    btn_delete = tk.Button(stock_page, **btn_options,bg="#cc0000", text="ลบ", cursor="hand2", command=lambda: delete_product())
    btn_delete.place(x=910,y=432,width=110,height=45)

    #### end box layout barcode

    #### box layout type
    label_type = tk.Label(stock_page,  bg="#999999")
    label_type.place(x=670,y=490,width=355,height=110)



    btn_type = tk.Button(stock_page, **btn_options,bg="#840856", text="ประเภทสินค้า", cursor="hand2", command=lambda: switch_to_page("type"))
    btn_type.place(x=680,y=515,width=162,height=62)

    btn_free = tk.Button(stock_page, **btn_options,bg="#fb4e18", text="สินค้าสิ้นเปลือง", cursor="hand2", command=lambda: switch_to_page("type"))
    btn_free.place(x=853,y=515,width=162,height=62)

    #### end box layout type


    #### box layout product_list
    label_product_list = tk.Label(stock_page,  bg="#00babd")
    label_product_list.place(x=5,y=55,width=660,height=540)
    #### end box layout product_list

    return stock_page

def save_product(barcode_entry, product_name_entry, product_type_entry,product_cost_entry,product_price_entry,product_amount_entry):
    barcode = barcode_entry.get()
    product_name = product_name_entry.get()
    product_type = product_type_entry.get()
    cost = product_cost_entry.get()
    price = product_price_entry.get()
    amount = product_amount_entry.get()

    print(barcode)
    print(product_name)
    print(product_type)
    print(cost)
    print(price)
    print(amount)

def add_product():
    print("add_product")
def edit_product():
    print("edit_product")
def delete_product():
    print("delete_product")