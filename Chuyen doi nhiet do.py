import tkinter as tk
from tkinter import messagebox

def chuyen_doi():
    try:
        do_c = float(entry_c.get())
        do_f = do_c * 9/5 + 32
        result.set(f"Nhiệt độ F: {do_f:.2f}°F")
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập một số hợp lệ!")

root = tk.Tk()
root.title("Chuyển đổi C → F")
root.geometry("300x150")
root.resizable(False, False)

tk.Label(root, text="Nhiệt độ (°C):").grid(row=0, column=0, padx=10, pady=10, sticky="w")
entry_c = tk.Entry(root)
entry_c.grid(row=0, column=1, padx=10, pady=10)

tk.Button(root, text="Chuyển đổi", command=chuyen_doi).grid(row=1, column=0, columnspan=2, pady=10)

result = tk.StringVar()
tk.Label(root, textvariable=result).grid(row=2, column=0, columnspan=2)

root.mainloop()
