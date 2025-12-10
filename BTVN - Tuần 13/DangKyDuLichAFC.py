import tkinter as tk
from tkinter import ttk, messagebox
import json

def doc_json(ten_file):
    try:
        with open(ten_file, "r", encoding="utf-8") as tep:
            return json.load(tep)
    except FileNotFoundError:
        messagebox.showerror("Lỗi", f"Không tìm thấy file {ten_file}")
        return []

def luu_json(ten_file, du_lieu):
    with open(ten_file, "w", encoding="utf-8") as tep:
        json.dump(du_lieu, tep, ensure_ascii=False, indent=2)

ds_nhan_vien = doc_json("nhanvien.json")
ds_dia_diem = doc_json("diadiemdulich.json")
ds_tham_gia = doc_json("thamgia.json")

def danh_sach_phong_ban():
    return sorted({nv.get("phong_ban", "") for nv in ds_nhan_vien if nv.get("phong_ban")})

def danh_sach_dia_diem_con_cho():
    return [dd for dd in ds_dia_diem if dd.get("so_luong_than_nhan", 0) > 0]

def tim_nhan_vien(ma_nv):
    for nv in ds_nhan_vien:
        if nv.get("ma_nv") == ma_nv:
            return nv
    return None

def dem_nv_phong_ban(ten_phong):
    return len([nv for nv in ds_nhan_vien if nv.get("phong_ban") == ten_phong])

def dem_than_nhan_phong_ban(ten_phong):
    ma_nv_phong = {nv.get("ma_nv") for nv in ds_nhan_vien if nv.get("phong_ban") == ten_phong}
    return len([tg for tg in ds_tham_gia if tg.get("ma_nv") in ma_nv_phong])

def dem_than_nhan_nhan_vien(ma_nv):
    return len([tg for tg in ds_tham_gia if tg.get("ma_nv") == ma_nv])

def cap_nhat_bang_than_nhan(ma_nv):
    for item in bang_than_nhan.get_children():
        bang_than_nhan.delete(item)
    ds_nv = [tg for tg in ds_tham_gia if tg.get("ma_nv") == ma_nv]
    for tg in ds_nv:
        bang_than_nhan.insert("", "end", values=(tg.get("ho_ten_than_nhan", ""), tg.get("nam_sinh", ""), tg.get("quan_he", ""), tg.get("dia_diem_du_lich", "")))
    nv = tim_nhan_vien(ma_nv)
    ten_nv = nv.get("ho_ten") if nv else ""
    label_tong_than_nv.config(text=f"Tổng số thân nhân của nhân viên {ma_nv if ma_nv else ''} {ten_nv}: {len(ds_nv)}")

def cap_nhat_ton_dia_diem():
    thong_tin = []
    for dd in ds_dia_diem:
        thong_tin.append(f"{dd.get('ten_dia_diem', '')}: còn {dd.get('so_luong_than_nhan', 0)} chỗ")
        label_ton_noi_dung.config(text="\n".join(thong_tin))


def cap_nhat_combobox_dia_diem():
    ds_con_cho = [dd.get("ten_dia_diem") for dd in danh_sach_dia_diem_con_cho()]
    chon_dia_diem["values"] = ds_con_cho
    if chon_dia_diem.get() not in ds_con_cho:
        if ds_con_cho:
            chon_dia_diem.set(ds_con_cho[0])
        else:
            chon_dia_diem.set("")

def cap_nhat_thong_tin_phong_ban(event=None):
    phong = chon_phong_ban.get()
    tong_nv = dem_nv_phong_ban(phong) if phong else 0
    tong_thannhan = dem_than_nhan_phong_ban(phong) if phong else 0
    label_tong_nv.config(text=f"Tổng số nhân viên trong phòng ban: {tong_nv}")
    label_tong_than_nhan_pb.config(text=f"Tổng số thân nhân đã đăng ký: {tong_thannhan}")

def thong_ke_dia_diem():
    dem = {dd.get("ten_dia_diem"): 0 for dd in ds_dia_diem}
    for tg in ds_tham_gia:
        dia_diem = tg.get("dia_diem_du_lich")
        if dia_diem in dem:
            dem[dia_diem] += 1
    noi_dung = []
    for dd in ds_dia_diem:
        ten = dd.get("ten_dia_diem")
        noi_dung.append(f"{ten}: {dem.get(ten, 0)} người")
    messagebox.showinfo("Thống kê", "\n".join(noi_dung) if noi_dung else "Chưa có dữ liệu")

def tra_cuu_than_nhan():
    ma_nv = entry_ma_nv.get().strip()
    if not ma_nv:
        messagebox.showerror("Lỗi", "Vui lòng nhập mã nhân viên")
        return
    nv = tim_nhan_vien(ma_nv)
    if not nv:
        messagebox.showerror("Lỗi", "Không tìm thấy nhân viên")
        return
    chon_phong_ban.set(nv.get("phong_ban", ""))
    cap_nhat_thong_tin_phong_ban()
    cap_nhat_bang_than_nhan(ma_nv)

def kiem_tra_trung(ma_nv, ho_ten, dia_diem):
    for tg in ds_tham_gia:
        if tg.get("ma_nv") == ma_nv and tg.get("ho_ten_than_nhan", "").strip().lower() == ho_ten.strip().lower() and tg.get("dia_diem_du_lich") == dia_diem:
            return True
    return False

def tim_dia_diem(ten):
    for dd in ds_dia_diem:
        if dd.get("ten_dia_diem") == ten:
            return dd
    return None

def luu_du_lieu_sau_thay_doi():
    luu_json("thamgia.json", ds_tham_gia)
    luu_json("diadiemdulich.json", ds_dia_diem)
    cap_nhat_combobox_dia_diem()
    cap_nhat_ton_dia_diem()
    cap_nhat_thong_tin_phong_ban()
    if entry_ma_nv.get().strip():
        cap_nhat_bang_than_nhan(entry_ma_nv.get().strip())

def dang_ky():
    ma_nv = entry_ma_nv.get().strip()
    ho_ten = entry_ho_ten.get().strip()
    nam_sinh = entry_nam_sinh.get().strip()
    quan_he = entry_quan_he.get().strip()
    dia_diem = chon_dia_diem.get().strip()
    if not ma_nv:
        messagebox.showerror("Lỗi", "Vui lòng nhập mã nhân viên")
        return
    if not tim_nhan_vien(ma_nv):
        messagebox.showerror("Lỗi", "Không tìm thấy nhân viên")
        return
    if not (ho_ten and nam_sinh and quan_he and dia_diem):
        messagebox.showerror("Lỗi", "Vui lòng nhập đầy đủ thông tin thân nhân")
        return
    if not nam_sinh.isdigit():
        messagebox.showerror("Lỗi", "Năm sinh phải là số")
        return
    if dem_than_nhan_nhan_vien(ma_nv) >= 5:
        messagebox.showerror("Lỗi", "Mỗi nhân viên chỉ được đăng ký tối đa 5 thân nhân")
        return
    dia_diem_chon = tim_dia_diem(dia_diem)
    if not dia_diem_chon or dia_diem_chon.get("so_luong_than_nhan", 0) <= 0:
        messagebox.showerror("Lỗi", "Địa điểm đã hết chỗ")
        cap_nhat_combobox_dia_diem()
        return
    if kiem_tra_trung(ma_nv, ho_ten, dia_diem):
        messagebox.showerror("Lỗi", "Đã tồn tại thân nhân này tại địa điểm đã chọn")
        return
    ds_tham_gia.append({"ma_nv": ma_nv, "ho_ten_than_nhan": ho_ten, "nam_sinh": int(nam_sinh), "quan_he": quan_he, "dia_diem_du_lich": dia_diem})
    dia_diem_chon["so_luong_than_nhan"] -= 1
    luu_du_lieu_sau_thay_doi()
    messagebox.showinfo("Thành công", "Đăng ký thành công")
    cap_nhat_bang_than_nhan(ma_nv)

def xoa():
    chon = bang_than_nhan.selection()
    if not chon:
        messagebox.showerror("Lỗi", "Vui lòng chọn thân nhân cần xóa")
        return
    ma_nv = entry_ma_nv.get().strip()
    ho_ten, nam_sinh, quan_he, dia_diem = bang_than_nhan.item(chon[0])["values"]
    for tg in list(ds_tham_gia):
        if tg.get("ma_nv") == ma_nv and tg.get("ho_ten_than_nhan") == ho_ten and tg.get("dia_diem_du_lich") == dia_diem:
            ds_tham_gia.remove(tg)
            dia_diem_tim = tim_dia_diem(dia_diem)
            if dia_diem_tim:
                dia_diem_tim["so_luong_than_nhan"] += 1
            luu_du_lieu_sau_thay_doi()
            cap_nhat_bang_than_nhan(ma_nv)
            return

def sua():
    chon = bang_than_nhan.selection()
    if not chon:
        messagebox.showerror("Lỗi", "Vui lòng chọn thân nhân cần sửa")
        return
    ma_nv = entry_ma_nv.get().strip()
    ho_ten_moi = entry_ho_ten.get().strip()
    nam_sinh_moi = entry_nam_sinh.get().strip()
    quan_he_moi = entry_quan_he.get().strip()
    dia_diem_moi = chon_dia_diem.get().strip()
    if not (ma_nv and ho_ten_moi and nam_sinh_moi and quan_he_moi and dia_diem_moi):
        messagebox.showerror("Lỗi", "Vui lòng nhập đầy đủ thông tin")
        return
    if not nam_sinh_moi.isdigit():
        messagebox.showerror("Lỗi", "Năm sinh phải là số")
        return
    ho_ten_cu, nam_sinh_cu, quan_he_cu, dia_diem_cu = bang_than_nhan.item(chon[0])["values"]
    if (ho_ten_moi.strip().lower() != ho_ten_cu.strip().lower() or dia_diem_moi != dia_diem_cu) and kiem_tra_trung(ma_nv, ho_ten_moi, dia_diem_moi):
        messagebox.showerror("Lỗi", "Đã tồn tại thân nhân này tại địa điểm đã chọn")
        return
    dia_diem_moi_obj = tim_dia_diem(dia_diem_moi)
    dia_diem_cu_obj = tim_dia_diem(dia_diem_cu)
    if dia_diem_moi != dia_diem_cu:
        if not dia_diem_moi_obj or dia_diem_moi_obj.get("so_luong_than_nhan", 0) <= 0:
            messagebox.showerror("Lỗi", "Địa điểm mới đã hết chỗ")
            return
    for tg in ds_tham_gia:
        if tg.get("ma_nv") == ma_nv and tg.get("ho_ten_than_nhan") == ho_ten_cu and tg.get("dia_diem_du_lich") == dia_diem_cu:
            tg["ho_ten_than_nhan"] = ho_ten_moi
            tg["nam_sinh"] = int(nam_sinh_moi)
            tg["quan_he"] = quan_he_moi
            tg["dia_diem_du_lich"] = dia_diem_moi
            if dia_diem_moi != dia_diem_cu:
                if dia_diem_cu_obj:
                    dia_diem_cu_obj["so_luong_than_nhan"] += 1
                if dia_diem_moi_obj:
                    dia_diem_moi_obj["so_luong_than_nhan"] -= 1
            luu_du_lieu_sau_thay_doi()
            cap_nhat_bang_than_nhan(ma_nv)
            return

def chon_than_nhan(event=None):
    chon = bang_than_nhan.selection()
    if not chon:
        return
    ho_ten, nam_sinh, quan_he, dia_diem = bang_than_nhan.item(chon[0])["values"]
    entry_ho_ten.delete(0, tk.END)
    entry_ho_ten.insert(0, ho_ten)
    entry_nam_sinh.delete(0, tk.END)
    entry_nam_sinh.insert(0, nam_sinh)
    entry_quan_he.delete(0, tk.END)
    entry_quan_he.insert(0, quan_he)
    chon_dia_diem.set(dia_diem)

root = tk.Tk()
root.title("Quản lý đăng ký du lịch cho thân nhân nhân viên")
root.geometry("850x800")

tieu_de = tk.Label(root, text="QUẢN LÝ ĐĂNG KÝ DU LỊCH CHO THÂN NHÂN NHÂN VIÊN", font=("Arial", 16, "bold"))
tieu_de.grid(row=0, column=0, columnspan=6, pady=10)

khung_phong_ban = tk.Frame(root)
khung_phong_ban.grid(row=1, column=0, columnspan=6, sticky="w", padx=10)

label_phong = tk.Label(khung_phong_ban, text="Phòng ban:")
label_phong.grid(row=0, column=0, padx=5, pady=5, sticky="w")
chon_phong_ban = ttk.Combobox(khung_phong_ban, state="readonly", width=30, values=danh_sach_phong_ban())
chon_phong_ban.grid(row=0, column=1, padx=5, pady=5)
chon_phong_ban.bind("<<ComboboxSelected>>", cap_nhat_thong_tin_phong_ban)
btn_thong_ke = tk.Button(khung_phong_ban, text="Thống kê", width=15, command=thong_ke_dia_diem)
btn_thong_ke.grid(row=0, column=2, padx=5)

label_tong_nv = tk.Label(root, text="Tổng số nhân viên trong phòng ban: 0")
label_tong_nv.grid(row=2, column=0, columnspan=3, padx=10, sticky="w")
label_tong_than_nhan_pb = tk.Label(root, text="Tổng số thân nhân đã đăng ký: 0")
label_tong_than_nhan_pb.grid(row=3, column=0, columnspan=3, padx=10, sticky="w")

khung_ma_nv = tk.Frame(root)
khung_ma_nv.grid(row=4, column=0, columnspan=6, sticky="w", padx=10, pady=5)
label_ma_nv = tk.Label(khung_ma_nv, text="Mã nhân viên:")
label_ma_nv.grid(row=4, column=0, padx=5, pady=5)
entry_ma_nv = tk.Entry(khung_ma_nv, width=20)
entry_ma_nv.grid(row=4, column=1, padx=5, pady=5)
btn_tra_cuu = tk.Button(khung_ma_nv, text="Tra cứu thân nhân", command=tra_cuu_than_nhan)
btn_tra_cuu.grid(row=4, column=2, padx=5, pady=5)

khung_bang = tk.Frame(root)
khung_bang.grid(row=5, column=0, columnspan=6, padx=10, pady=5, sticky="nsew")
bang_than_nhan = ttk.Treeview(khung_bang, columns=("ho_ten", "nam_sinh", "quan_he", "dia_diem"), show="headings", height=8)
bang_than_nhan.heading("ho_ten", text="Họ tên")
bang_than_nhan.heading("nam_sinh", text="Năm sinh")
bang_than_nhan.heading("quan_he", text="Quan hệ")
bang_than_nhan.heading("dia_diem", text="Địa điểm")
bang_than_nhan.grid(row=0, column=0)

bang_than_nhan.bind("<<TreeviewSelect>>", chon_than_nhan)


label_tong_than_nv = tk.Label(root, text="Tổng số thân nhân của nhân viên:")
label_tong_than_nv.grid(row=6, column=0, columnspan=6, sticky="w", padx=10, pady=5)
khung_form = tk.Frame(root)
khung_form.grid(row=7, column=0, columnspan=6, padx=10, pady=5, sticky="nw")

label_thong_tin_than_nhan = tk.Label(khung_form, text="Thông tin thân nhân")
label_thong_tin_than_nhan.grid(row=0, column=0, columnspan=2, sticky="w", pady=(0,5))

label_ho_ten = tk.Label(khung_form, text="Họ tên:")
label_ho_ten.grid(row=1, column=0, padx=5, pady=2, sticky="w")
entry_ho_ten = tk.Entry(khung_form, width=30)
entry_ho_ten.grid(row=1, column=1, padx=5, pady=2, sticky="w")

label_nam_sinh = tk.Label(khung_form, text="Năm sinh:")
label_nam_sinh.grid(row=2, column=0, padx=5, pady=2, sticky="w")
entry_nam_sinh = tk.Entry(khung_form, width=15)
entry_nam_sinh.grid(row=2, column=1, padx=5, pady=2, sticky="w")

label_quan_he = tk.Label(khung_form, text="Quan hệ:")
label_quan_he.grid(row=3, column=0, padx=5, pady=2, sticky="w")
entry_quan_he = tk.Entry(khung_form, width=20)
entry_quan_he.grid(row=3, column=1, padx=5, pady=2, sticky="w")

label_dia_diem = tk.Label(khung_form, text="Địa điểm:")
label_dia_diem.grid(row=4, column=0, padx=5, pady=2, sticky="w")
chon_dia_diem = ttk.Combobox(khung_form, state="readonly", width=20)
chon_dia_diem.grid(row=4, column=1, padx=5, pady=2, sticky="w")

btn_dang_ky = tk.Button(khung_form, text="Đăng ký", width=12, command=dang_ky)
btn_dang_ky.grid(row=1, column=2, padx=15, pady=2)
btn_xoa = tk.Button(khung_form, text="Xóa", width=12, command=xoa)
btn_xoa.grid(row=2, column=2, padx=15, pady=2)
btn_sua = tk.Button(khung_form, text="Sửa", width=12, command=sua)
btn_sua.grid(row=3, column=2, padx=15, pady=2)

khung_ton = tk.Frame(root)
khung_ton.grid(row=8, column=0, columnspan=6, padx=10, pady=10, sticky="w")
label_ton = tk.Label(khung_ton, text="Thống kê địa điểm du lịch còn chỗ đăng ký:")
label_ton.grid(row=0, column=0, sticky="w")
label_ton_noi_dung = tk.Label(khung_ton, text="", justify="left", anchor="w")
label_ton_noi_dung.grid(row=1, column=0, sticky="w")

cap_nhat_combobox_dia_diem()
cap_nhat_ton_dia_diem()

if danh_sach_phong_ban():
    chon_phong_ban.set(danh_sach_phong_ban()[0])
    cap_nhat_thong_tin_phong_ban()

root.mainloop()
