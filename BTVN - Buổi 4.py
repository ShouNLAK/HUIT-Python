def Viet_Hoa_Chu_Cai_Dau_Tien(chuoi):
    # Tach cau
    Dau_Cau = ".!?;:()[]"
    chuoi = chuoi.strip()
    if len(chuoi) == 0:
        return chuoi
    # Viet hoa chu cai dau tien cua chuoi
    chuoi = chuoi[0].capitalize() + chuoi[1:]
    # Viet hoa chu cai dau tien sau cac dau cau
    for i in range(1, len(chuoi)):
        if chuoi[i - 1] in Dau_Cau and chuoi[i] == " " and i + 1 < len(chuoi):
            chuoi = chuoi[:i + 1] + chuoi[i + 1].capitalize() + chuoi[i + 2:]
    print("KQ : Viet hoa chu cai dau tien trong cau : ", chuoi)
    return chuoi

def Viet_Hoa_Tat_Ca_Chu_Cai_Dau_Tien(chuoi):
    chuoi = chuoi.strip()
    if len(chuoi) == 0:
        return chuoi
    # Viet hoa chu cai dau tien cua moi tu
    chuoi = chuoi.title()
    print("KQ : Viet hoa tat ca chu cai dau tien trong cau :", chuoi)
    return chuoi

def Viet_Thuong_Toan_Bo_Chuoi(chuoi):
    chuoi = chuoi.strip()
    if len(chuoi) == 0:
        return chuoi
    # Viet thuong toan bo chuoi
    chuoi = chuoi.lower()
    print("KQ : Viet thuong toan bo chuoi :", chuoi)
    return chuoi

def Viet_Hoa_Toan_Bo_Chuoi(chuoi):
    chuoi = chuoi.strip()
    if len(chuoi) == 0:
        return chuoi
    # Viet hoa toan bo chuoi
    chuoi = chuoi.upper()
    print("KQ : Viet hoa toan bo chuoi :", chuoi)
    return chuoi

def Dem_So_Tu(chuoi):
    if len(chuoi) == 0:
        print("KQ : So tu trong chuoi la : 0")
        return 0
    # Dem so tu trong chuoi
    so_tu = len(chuoi.split())
    print("KQ : So tu trong chuoi la :", so_tu)
    return so_tu

def Tim_Tu_Khoa(chuoi, tu_khoa):
    chuoi = chuoi.strip()
    if len(chuoi) == 0 or len(tu_khoa) == 0:
        print("KQ : Khong tim thay tu khoa trong chuoi.")
        return 0
    # Dem so lan xuat hien cua tu khoa (khong phan biet hoa thuong)
    so_lan_xuat_hien = chuoi.lower().count(tu_khoa.lower())
    if so_lan_xuat_hien > 0:
        print(f"KQ : Tim thay tu khoa '{tu_khoa}' trong chuoi {so_lan_xuat_hien} lan.")
    else:
        print(f"KQ : Khong tim thay tu khoa '{tu_khoa}' trong chuoi.")
    return so_lan_xuat_hien

def Thay_The_Tu_Khoa(chuoi, tu_khoa_cu, tu_khoa_moi):
    chuoi = chuoi.strip()
    if len(chuoi) == 0 or len(tu_khoa_cu) == 0 or len(tu_khoa_moi) == 0:
        print("KQ : Khong the thay the tu khoa.")
        return chuoi    
    # Thay the tu khoa cu bang tu khoa moi (khong phan biet hoa thuong)
    chuoi = chuoi.replace(tu_khoa_cu, tu_khoa_moi)
    print("KQ : Chuoi sau khi thay the :", chuoi)
    return chuoi

def Trich_va_Phan_biet_Tu_Duy_Nhat(chuoi):
    chuoi = chuoi.strip()
    if chuoi == "":
        print("KQ : Chuoi rong.")
        return []
    tu_list = chuoi.split()
    # Phan biet tu duy nhat va tu trung lap
    tu_duy_nhat = []
    tu_trung_lap = []
    for tu in tu_list:
        if tu in tu_duy_nhat and tu not in tu_trung_lap:
            tu_trung_lap.append(tu)
            tu_duy_nhat.remove(tu)
        tu_duy_nhat.append(tu)
    print("KQ : Cac tu duy nhat trong chuoi :", tu_duy_nhat)
    print("KQ : Cac tu trung lap trong chuoi :", tu_trung_lap)
    return tu_duy_nhat

def Tan_suat_Xuat_Hien_Cua_Tu(chuoi):
    chuoi = chuoi.strip()
    if chuoi == "":
        print("KQ : Chuoi rong.")
        return {}
    # Dem tan suat xuat hien cua moi tu
    tu_list = chuoi.split()
    tan_suat = {}
    for tu in tu_list:
        if tu in tan_suat:
            tan_suat[tu] += 1
        else:
            tan_suat[tu] = 1
    print("KQ : Tan suat xuat hien cua cac tu trong chuoi :", tan_suat)
    return tan_suat

def Thay_The_Theo_Anh_Xa(chuoi, anh_xa):
    chuoi = chuoi.strip()
    if chuoi == "":
        print("KQ : Chuoi rong.")
        return chuoi
    # Thay the cac tu theo anh xa trong tu dien
    for tu_cu, tu_moi in anh_xa.items():
        chuoi = chuoi.lower().replace(tu_cu, tu_moi)
    print("KQ : Chuoi sau khi thay the theo anh xa :", chuoi)
    return chuoi

def Kiem_tra_Tu_Cam(chuoi, danh_sach_tu_cam):
    chuoi = chuoi.lower()
    da_thay_the = False
    for tu_cam in danh_sach_tu_cam:
        tu_cam_lower = tu_cam.lower()
        if tu_cam_lower in chuoi:
            censored = tu_cam[0] + '***'
            chuoi = chuoi.replace(tu_cam_lower, censored)
            da_thay_the = True
    if da_thay_the:
        print("KQ : Chuoi sau khi thay tu cam :", chuoi)
    else:
        print("KQ : Khong phat hien tu cam.")
    return da_thay_the

def Thong_Ke_Chuoi(chuoi):
    if not chuoi.strip():
        print("KQ : Chuoi rong.")
        return {}
    # Tach cau dua tren cac dau cau
    dau_cau = ".!?;:()[]"
    cau_list = []
    cau = ""
    for char in chuoi:
        if char in dau_cau:
            if cau.strip():
                cau_list.append(cau.strip())
            cau = ""
        else:
            cau += char
    if cau.strip():
        cau_list.append(cau.strip())
    so_cau = len(cau_list)
    do_dai_cau = [len(c.split()) for c in cau_list]
    cau_ngan_nhat = min(do_dai_cau) if do_dai_cau else 0
    cau_dai_nhat = max(do_dai_cau) if do_dai_cau else 0
    thong_ke = {
        "so_cau": so_cau,
        "do_dai_tung_cau": do_dai_cau,
        "cau_ngan_nhat": cau_ngan_nhat,
        "cau_dai_nhat": cau_dai_nhat
    }
    print("KQ : Thong ke chuoi :", thong_ke)
    return thong_ke

def Chuan_hoa_Chuoi(chuoi):
    chuoi = chuoi.strip()
    if not chuoi:
        print("KQ : Chuoi rong.")
        return chuoi
    # Thay tab va newline bang 1 khoang trang
    chuoi = chuoi.replace('\t', ' ').replace('\n', ' ')
    # Xoa khoang trang thua giua cac tu
    chuoi = ' '.join(chuoi.split())
    # Viet hoa chu cai dau cau
    chuoi = Viet_Hoa_Chu_Cai_Dau_Tien(chuoi)
    return chuoi

test_str = "   xin chao! day la mot vi du.   \nday la cau thu hai.\tday la cau thu ba!   "

print("\n--- Chuan_hoa_Chuoi ---")
test_str = Chuan_hoa_Chuoi(test_str)


print("\n--- Viet_Hoa_Chu_Cai_Dau_Tien ---")
Viet_Hoa_Chu_Cai_Dau_Tien(test_str)

print("\n--- Viet_Hoa_Tat_Ca_Chu_Cai_Dau_Tien ---")
Viet_Hoa_Tat_Ca_Chu_Cai_Dau_Tien(test_str)

print("\n--- Viet_Thuong_Toan_Bo_Chuoi ---")
Viet_Thuong_Toan_Bo_Chuoi(test_str)

print("\n--- Viet_Hoa_Toan_Bo_Chuoi ---")
Viet_Hoa_Toan_Bo_Chuoi(test_str)

print("\n--- Dem_So_Tu ---")
Dem_So_Tu(test_str)

print("\n--- Tim_Tu_Khoa ---")
Tim_Tu_Khoa(test_str, "la")

print("\n--- Thay_The_Tu_Khoa ---")
Thay_The_Tu_Khoa(test_str, "vi du", "demo")

print("\n--- Trich_va_Phan_biet_Tu_Duy_Nhat ---")
Trich_va_Phan_biet_Tu_Duy_Nhat(test_str)

print("\n--- Tan_suat_Xuat_Hien_Cua_Tu ---")
Tan_suat_Xuat_Hien_Cua_Tu(test_str)

print("\n--- Thay_The_Theo_Anh_Xa ---")
Thay_The_Theo_Anh_Xa(test_str, {"xin chao": "hello", "vi du": "example", "cau": "sentence"})

print("\n--- Kiem_tra_Tu_Cam ---")
Kiem_tra_Tu_Cam(test_str, ["hai", "vi du"])

print("\n--- Thong_Ke_Chuoi ---")
Thong_Ke_Chuoi(test_str)

