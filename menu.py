
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
    
def create_menu(root, switch_to_page):
    menu_page = ttk.Frame(root)
    style = ttk.Style()
    style.configure("menu_page.TFrame") 
    menu_page.configure(style="menu_page.TFrame")
    name_label = ttk.Label(menu_page, text="")
    name_label.pack(pady=10)

        # create button
    button_options = {
        "borderwidth": "0",
        "font": ("Kanit", 40),
        "fg": "#ffffff",
        "justify": "center",
        "relief": "raised",
    }

    btn_sell = tk.Button(menu_page, **button_options,bg="#1e90ff", text="หน้าจอขาย", cursor="hand2", command=lambda: switch_to_page("user"))
    btn_sell.place(x=130,y=110,width=350,height=150)

    btn_stock = tk.Button(menu_page, **button_options,bg="#1e90ff", text="สินค้า/สต็อค", cursor="hand2", command=lambda: switch_to_page("stock"))
    btn_stock.place(x=580,y=110,width=350,height=150)

    btn_report = tk.Button(menu_page, **button_options,bg="#1e90ff", text="รายงาน", cursor="hand2", command=lambda: switch_to_page("report"))
    btn_report.place(x=130,y=340,width=350,height=150)

    btn_report = tk.Button(menu_page, **button_options,bg="#1e90ff", text="ตั้งค่า", cursor="hand2", command=lambda: switch_to_page("setting"))
    btn_report.place(x=580,y=340,width=350,height=150)


    return menu_page

def logout(switch_to_page):
    result = messagebox.askyesno("ออกจากระบบ", "ยืนยันที่จะออกจากระบบ")
    if result:
        switch_to_page("login")