import json

class SinhVien:
    def __init__(self, ma, ten, diem):
        self.Ma = ma
        self.Ten = ten
        if diem >= 0:
            self.Diem = diem
        else:
            raise Exception("Diem phai lon hon 0")

    def to_dict(self):
        return {"maSV": self.Ma, "hoTen": self.Ten, "diem": self.Diem}

    def XepLoai(self):
        if self.Diem >= 8.5:
            return "Gioi"
        elif self.Diem >= 6.5:
            return "Kha"
        elif self.Diem >= 5:
            return "Trung binh"
        elif self.Diem >= 3.5:
            return "Kem"
        else:
            return "Yeu"

    def __str__(self):
        return f"{self.Ma} | {self.Ten} | {self.Diem}"


class DSSV:
    def __init__(self):
        self.DS = []

    def Nhap_DS_JSON(self, tenFile):
        with open(tenFile, 'r', encoding='utf-8') as file:
            data = json.load(file)
            for item in data:
                self.DS.append(SinhVien(item["maSV"], item["hoTen"], float(item["diem"])))

    def Them_SV(self, ma, ten, diem):
        for sv in self.DS:
            if sv.Ma == ma:
                return False
        self.DS.append(SinhVien(ma, ten, diem))
        return True

    def HienThi_DS(self):
        print("Ma SV | Ten SV | Diem")
        for sv in self.DS:
            print(sv)

    def Tim_SV(self, ma):
        for sv in self.DS:
            if sv.Ma == ma:
                return sv
        return None

    def LietKe_Gioi(self):
        return [sv for sv in self.DS if sv.XepLoai() == "Gioi"]

    def SapXep_Giam_Theo_Diem(self):
        self.DS.sort(key=lambda sv: sv.Diem, reverse=True)

    def XoaTheoMa(self, ma):
        for i, sv in enumerate(self.DS):
            if sv.Ma == ma:
                del self.DS[i]
                return True
        return False

    def ThongKe_Theo_Loai(self):
        stats = {}
        for sv in self.DS:
            loai = sv.XepLoai()
            if loai not in stats:
                stats[loai] = 1
            else:
                stats[loai] += 1
        return stats

    def Ghi_SV_Gioi_Vao_File(self, tenFile="sv_gioi.json"):
        gioi = self.LietKe_Gioi()
        data = [sv.to_dict() for sv in gioi]
        with open(tenFile, 'w', encoding='utf-8') as fileO:
            json.dump(data, fileO, ensure_ascii=False, indent=2)
        return True

    def Luu_DS_Vao_File(self, tenFile="dssv.json"):
        data = [sv.to_dict() for sv in self.DS]
        with open(tenFile, 'w', encoding='utf-8') as fileO:
            json.dump(data, fileO, ensure_ascii=False, indent=2)
        return True


def main():
    dssv = DSSV()
    dssv.Nhap_DS_JSON("DSSV.json")
    while True:
        print("------ MENU ------")
        print("1. Hien thi danh sach sinh vien")
        print("2. Them sinh vien")
        print("3. Tim sinh vien theo ma so")
        print("4. Liet ke sinh vien gioi")
        print("5. Sap xep sinh vien giam dan theo diem")
        print("6. Xoa sinh vien theo ma so")
        print("7. Thong ke so luong sinh vien theo loai")
        print("8. Ghi danh sach sinh vien gioi vao file")
        print("9. Luu danh sach sinh vien vao file")
        print("0. Thoat")
        choice = input("Chon (0-9): ").strip()
        if choice == "1":
            dssv.HienThi_DS()
        elif choice == "2":
            ma = input("Ma: ").strip()
            ten = input("Ho ten: ").strip()
            diem = float(input("Diem: ").strip())
            if dssv.Them_SV(ma, ten, diem):
                print("Them thanh cong.")
            else:
                print("Ma da ton tai.")
        elif choice == "3":
            ma = input("Nhap ma can tim: ").strip()
            sv = dssv.Tim_SV(ma)
            if sv:
                print("Tim thay:", sv)
            else:
                print("Khong tim thay sinh vien.")
        elif choice == "4":
            gioi = dssv.LietKe_Gioi()
            if not gioi:
                print("Khong co sinh vien gioi.")
            else:
                for sv in gioi:
                    print(sv)
        elif choice == "5":
            dssv.SapXep_Giam_Theo_Diem()
            print("Da sap xep giam dan theo diem.")
        elif choice == "6":
            ma = input("Nhap ma can xoa: ").strip()
            if dssv.XoaTheoMa(ma):
                print("Xoa thanh cong.")
            else:
                print("Khong tim thay ma.")
        elif choice == "7":
            stats = dssv.ThongKe_Theo_Loai()
            for loai, cnt in stats.items():
                print(f"{loai}: {cnt}")
        elif choice == "8":
            dssv.Ghi_SV_Gioi_Vao_File()
            print("Da ghi sinh vien gioi vao file.")
        elif choice == "9":
            dssv.Luu_DS_Vao_File()
            print("Da luu danh sach vao file.")
        elif choice == "0":
            print("Thoat.")
            break
        else:
            print("Lua chon khong hop le.")


if __name__ == "__main__":
    main()
