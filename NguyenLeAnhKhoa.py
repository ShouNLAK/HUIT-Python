EN_VN_Dict={
    'hello' : {'n' : 'xin chào'},
    'bat' : {'n' : "con dơi",'v' : 'đánh bóng'}
    }

def Show_Dict():
    print("{Tiếng Anh} : {Tiếng Việt} (Loại từ)")
    for key, value in EN_VN_Dict.items():
        for type, mean in value.items() :
            print(f"{key}: {mean} ({type})")

def Them_Tu ():
    EN = input("Hãy viết từ Tiếng Anh cần được thêm vào từ điển : ").lower()
    ListMean = {}
    while True :
        VN = input("Hãy viết nghĩa của từ đó bằng tiếng Việt : ").lower()
        Type = input("Hãy nhập loại từ của nghĩa đó (n/v/adj/adv): ").lower()
        ListMean[Type] = VN
        MutipleMeaning = input("Bạn có muốn nhập thêm nghĩa không? (y/n) : ").lower()
        if MutipleMeaning == "n" :
            break
    Add(EN,ListMean)
    
    
def Tim_Tu() :
    Tu = input("Hãy viết từ tiếng Anh hoặc nghĩa tiếng Việt cần tìm : ").lower()
    Finding(Tu)
        
def Xoa_Tu():
    EN = input("Hãy nhập từ còn xóa : ").lower()
    Erase(EN)
    
def CapNhat_Nghia():
    EN = input("Hãy viết từ tiếng Anh cần cập nhật nghĩa: ").lower()
    if Finding(EN) : 
        Update_Meaning̣(EN)

def Add(English,ListOfMeanings) :
    if English in EN_VN_Dict :
        print(f"Từ {English} đã tồn tại trong từ điển")
    else :
        EN_VN_Dict[English] = ListOfMeanings
        print(f"Đã thêm thành công {English} vào từ điển")
        Show_Dict()
    
def Finding(Word) :
    if Word in EN_VN_Dict:
        print(f"Đã tìm thấy khóa {Word} dưới nghĩa của {EN_VN_Dict[Word]}")
        return True
    for EN, Mean in EN_VN_Dict.items() :
        for type, VN in Mean.items():
            if VN == Word :
                Tran = EN  
                print(f"Đã tìm thấy từ {Word} ({type}) là nghĩa của {Tran}")
                return True
    else :
        print(f"Không tìm thấy {Word} trong từ điển")
        return False
        
def Erase(EN) :
    if (Finding(EN)) :
        del EN_VN_Dict[EN]
        print(f"Đã xóa {EN} ra khỏi từ điển")
        Show_Dict()
        
def Show_By_Conditions() :
    print("--- Menu ---")
    print("1. Theo loại ")
    print("2. Theo từ")
    print("3. Theo từ và loại từ")
    print("------------")
    print("-1 . Thoát chương trình ")
    Choose = int(input("Hãy nhập chương trình bạn muốn chạy : "))
    if Choose != -1 :
        if Choose == 1:
            Show_Type = input("Nhập loại từ muốn hiển thị (n/v/adj/adv): ")
            for key, value in EN_VN_Dict.items():
                for type, mean in value.items() :
                    if Show_Type == type :
                        print(f"{key}: {mean} ({type})")
        elif Choose == 2 :
            Show_Name = input("Nhập từ muốn hiển thị : ")
            for key, value in EN_VN_Dict.items():
                if key == Show_Name :
                    for type, mean in value.items() :
                        print(f"{key}: {mean} ({type})")
        else:
             print("Lỗi nhập sai cú pháp - Vui lòng nhập lại")
        Menu()
        
def Update_Meaning̣(EN) :
    print("---------------")
    print("1. Thêm nghĩa")
    print("2. Xóa nghĩa")
    print("---------------")
    print("-1. Thoát chương trình")
    Choose = int(input("Nhập lựa chọn của bạn : "))
    if Choose != -1 :
        if Choose == 1:
            New_Meaning = input("Hãy viết nghĩa của từ đó bằng tiếng Việt : ").lower()
            Type = input("Hãy nhập loại từ của nghĩa đó : ").lower()
            Old = [EN_VN_Dict[EN][Type]]
            Old.append(New_Meaning)
            EN_VN_Dict[EN][Type] = Old
        elif Choose == 2:
            Found = False
            Deleting_Meaning = input(f"Nhập nghĩa muốn xóa của từ {EN} : ").lower()
            for EN ,ListOfMeaning in EN_VN_Dict.items() :
                for type, VN in ListOfMeaning.items() :
                    if VN == Deleting_Meaning :
                        Old = [EN_VN_Dict[EN][type]]
                        Old.remove(Deleting_Meaning)
                        EN_VN_Dict[EN][type] = Old
                        Found = True
            if Found:
                print(f"Đã xóa nghĩa {Deleting_Meaning} ra khỏi {EN}")
            else:
                    print("Không tồn tại nghĩa {Deleting_Meaning} trong {EN}")
        Update_Meaning̣(EN)
    value = EN_VN_Dict.get(EN)
    if value is not None:
        if not value:
            del EN_VN_Dict[EN]
        for type in list(value.keys()):
            if value[type] == []:
                del value[type]
    else:
        print(f"Từ '{EN}' không còn tồn tại trong từ điển do không còn .")
                
                
def Menu() :
    print("--- Menu ---")
    print("1. Thêm từ tiếng Anh - Định nghĩa tiếng Việt")
    print("2. Hiển thị toàn bộ danh sách từ điển hiện tại đang có")
    print("3. Tìm từ trong từ điển")
    print("4. Xóa từ trong từ ")
    print("5. Cập nhật nghĩa của từ ")
    print("6. Xem danh sách theo điều kiện")
    print("------------")
    print("-1 . Thoát chương trình ")
    Choose = int(input("Hãy nhập chương trình bạn muốn chạy : "))
    if Choose != -1 :
        if Choose == 1:
            Them_Tu()
        elif Choose == 2 :
            Show_Dict()
        elif Choose == 3:
            Tim_Tu()
        elif Choose == 4 :
            Xoa_Tu()
        elif Choose == 5 :
            CapNhat_Nghia()
        elif Choose == 6:
            Show_By_Conditions()
        else:
             print("Lỗi nhập sai cú pháp - Vui lòng nhập lại")
        Menu()

Menu()