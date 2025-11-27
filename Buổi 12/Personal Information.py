import tkinter as tk
from tkinter import messagebox

def Display_Info():
    Email = EntryEmail.get()
    SDT = EntryPhone.get()
    
    Result.config(text=f"Thông tin liên lạc:\nEmail : {Email + '@gmail.com'}\nSDT : {SDT}")
    
root = tk.Tk()
root.title("Thông tin liên lạc")
root.geometry("300x300")

tk.Label(root,text="Email : ").grid(row=0,column=0,padx=10,pady=10)
EntryEmail = tk.Entry(root)
EntryEmail.grid(row=0,column=1,padx=10,pady=10)
tk.Label(root,text="@gmail.com").grid(row=0,column=2,padx=10,pady=10)

tk.Label(root,text="SDT : ").grid(row=1,column=0,padx=10,pady=10)
EntryPhone = tk.Entry(root)
EntryPhone.grid(row=1,column=1,padx=10,pady=10)

tk.Button(root,text="Xuất thông tin",command=Display_Info).grid(row=2,column=0,padx=10,pady=10,columnspan=2)

Result = tk.Label(root)
Result.grid(row=3,column=0,padx=10,pady=10,columnspan=2)

root.mainloop()