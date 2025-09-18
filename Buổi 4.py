def Menu():
    print("-------------------------------------------------------")
    print("1. Xuất đầy đủ họ tên (Đã chuẩn hóa)")
    print("2. Xuất Họ - Tên - Đệm - Tên viết tắt - Username gợi ý")
    print("3. Đếm số từ trong họ tên")
    print("4. So sánh 2 họ tên")
    print("5. Sắp xếp theo tên hoặc theo toàn bộ họ tên")
    print("6. Khảo sát tần xuất theo tên")
    print("7. Khởi tạo Email")
    print("8. Kiểm tra tính hợp lệ của tên")
    print("9. Viết tên viết ngược (Theo dạng EU - US)")
    Choose = int(input("Hãy nhập lựa chọn của bạn : "))
    print("-------------------------------------------------------")
    if (Choose == 1) : 
        print(f"Họ và tên : {name}")
    elif (Choose == 2) :
        Ho,Ten,Dem = Ho_Ten(name)
        tenVietTat = TenVietTat(name)
        User = Username(name)
        print(f"Họ : {Ho}\nĐệm : {Dem}\nTên : {Ten}")
        print(f"Tên viết tắt : {tenVietTat}\nUsername gợi ý : {User}")
    elif (Choose == 3) :
        print(f"Độ dài họ tên : {Count(name)}")
    elif (Choose == 4) :
        SecondName = Nhap_Name()
        SecondName = chuan_hoa(SecondName)
        print(f"Kết quả trùng tên : {Compare(name,SecondName)}")
    elif(Choose == 5) :
        print(f"Danh sách sắp xếp theo tên : {Sort_ByName(Arr)}")
        print(f"Danh sách sắp xếp theo toàn bộ từ Họ -> Tên : {Sort_FullName(Arr)}")
    elif(Choose == 6) :
        KhaosatTanxuat(Arr)
    elif(Choose == 7):
        print(f"Tên email : {Email_Generator(name)}")
    elif(Choose == 8) :
        print(f"Tính hợp lệ của tên : {Check_Valid(name)}")
    elif(Choose == 9) :
        print(f"Tên viết ngược của bạn là : {EU_US_Format(name)}")
    else :
        print("Nhập sai chương trình")
    Menu()
    
def Nhap_Name() :
    return input("Nhập họ tên của bạn : ")

def chuan_hoa(name):
    return " ".join([word.capitalize() for word in name.strip().split()])

def Ho_Ten(name) :
    word = name.split()
    return word[0],word[-1]," ".join(word[1:(len(word)-1)])

def TenVietTat(name) : 
        return ".".join([word[0].capitalize() for word in name.strip().split()])

def Username(name) :
    Ho,Ten,Dem = Ho_Ten(name)
    return Ten.lower() + Ho.lower()[0] + "".join([Word[0].lower() for Word in Dem.split()])
    
def Count(name) :
    return len(name.split())

def Compare (name,SecondName) :
    Ho,Ten,Dem = Ho_Ten(name)
    Last,First,Middle = Ho_Ten(SecondName)
    if (Ten == First):
        return True
    else:
        return False
    
def Sort_ByName(Arr) :
    Arr.sort(key=lambda x: x.split()[-1])
    print(Arr)
    
def Sort_FullName(Arr):
    Arr.sort(key=lambda x: x.split())
    print(Arr)
    
def KhaosatTanxuat(Arr) :
    Tansuat={}
    for Word in Arr:
        Word = Word.split()[-1]
        if Word in Tansuat :
            Tansuat[Word] += 1
        else:
            Tansuat[Word] = 1
    print(Tansuat)

def Email_Generator(name):
    User = Username (name)
    return User + "@huit.edu.vn"

def Check_Valid(name):
    Valid = True
    Not_allow = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '!', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '"', '^', '_', '`', '{', '|', '}', '~']
    for i in range(len(Not_allow)) :
        if Not_allow[i] in name :
            Valid = False
    return Valid

def EU_US_Format(name) :
    Ho,Ten,Dem = Ho_Ten(name)
    return Dem + " " + Ten + " " + Ho

Arr = ["Nguyễn Văn D" , "Trần Văn B" , "Lê Thị A", "Bùi Quang D" , "Bùi Hương A"]
name = Nhap_Name()
name = chuan_hoa(name)
Menu()
