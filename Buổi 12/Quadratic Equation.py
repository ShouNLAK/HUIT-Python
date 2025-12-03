import tkinter as tk
import math
from tkinter import messagebox

def Tinh_PTB2():
    try:
        a = float(EntryA.get())
        b = float(EntryB.get())
        c = float(EntryC.get())
        
        if a == 0 :
            if (b == 0) :
                if (c == 0) :
                    Result_label.config(text=f"Vô số nghiệm")
                else :
                    Result_label.config(text=f"Vô nghiệm")
            else :
                Result_label.config(text=f"Nghiệm của phương trình = {c *(-1) / b}")
        else:
            delta = b**2 - 4*a*c
            if delta > 0 :
                Result_label.config(text=f"Nghiệm thứ nhất = {(b*-1 - math.sqrt(delta))/2*a}\n Nghiệm thứ hai = {(b*-1 + math.sqrt(delta))/(2*a)}")
            elif delta == 0 :
                Result_label.config(text=f"Nghiệm chung = {b*-1 / (2*a)}")
            else :
                Result_label.config(text=f"Vô nghiệm")
        
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập một số hợp lệ!")
        
root = tk.Tk()
root.title("Tính phương trình bậc 2")
root.geometry("500x400")

tk.Label(root,text="Hệ số a : ").grid(row=0,column=0,padx=10,pady=10)
EntryA = tk.Entry(root)
EntryA.grid(row=0,column=1,padx=10,pady=10)


tk.Label(root,text="Hệ số b : ").grid(row=1,column=0,padx=10,pady=10)
EntryB = tk.Entry(root)
EntryB.grid(row=1,column=1,padx=10,pady=10)

tk.Label(root,text="Hệ số c : ").grid(row=2,column=0,padx=10,pady=10)
EntryC = tk.Entry(root)
EntryC.grid(row=2,column=1,padx=10,pady=10)

tk.Button(root,text="Tính toán",command=Tinh_PTB2).grid(row=3,column=0,padx=10,pady=10,columnspan = 2)
Result_label = tk.Label(root)
Result_label.grid(row=4,column=0,padx=10,pady=10,columnspan = 2)

root.mainloop()