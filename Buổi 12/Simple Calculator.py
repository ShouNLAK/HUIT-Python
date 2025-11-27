import tkinter as tk
from tkinter import messagebox

def Calculate():
    try :
        So1 = float(Entry1.get())
        So2 = float(Entry2.get())
        Dau = operations.get()
        
        if Dau == "+" :
            Result = So1 + So2
        elif Dau == "-" :
            Result = So1 - So2
        elif Dau == "*" :
            Result = So1 * So2
        elif Dau == "/" :
            if So2 == 0 : 
                messagebox.showerror("Lỗi", "Mẫu không được khác 0 !")
            Result = So1 / So2
        Result_Out.delete(0,tk.END)
        Result_Out.insert(0, str(Result))
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập một số hợp lệ!")
        
root = tk.Tk()
root.title("Máy tính đơn giản")
root.geometry("400x200")

tk.Label(root, text="Số thứ nhất").grid(row=0, column=0, padx=10, pady=10)
Entry1 = tk.Entry(root)
Entry1.grid(row=0,column =1,padx = 10, pady = 10)

tk.Label(root, text="Số thứ hai").grid(row=1, column=0, padx=10, pady=10)
Entry2 = tk.Entry(root)
Entry2.grid(row=1,column =1,padx = 10, pady = 10)

operations = tk.StringVar(value="none")

tk.Label(root, text="Phép tính").grid(row=2, column=0, padx=10, pady=10)

frame_radio = tk.Frame(root)
frame_radio.grid(row=2, column=1, padx=10, pady=5)

tk.Radiobutton(frame_radio, text="Cộng", variable=operations,value="+").pack(side="left")
tk.Radiobutton(frame_radio, text="Trừ", variable=operations, value="-").pack(side="left")
tk.Radiobutton(frame_radio, text="Nhân", variable=operations, value="*").pack(side="left")
tk.Radiobutton(frame_radio, text="Chia", variable=operations, value="/").pack(side="left")

tk.Label(root, text="Kết quả = ").grid(row=3, column=0, padx=10, pady=10)
Result_Out = tk.Entry(root)
Result_Out.grid(row=3,column =1,padx = 10, pady = 10)

tk.Button(root,text="Tính toán",command=Calculate).grid(row=4,column =0,padx = 10, pady = 10,columnspan = 2)

root.mainloop()