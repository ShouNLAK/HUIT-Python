import re

Text ="Số báo danh: 12345, điểm toán: 8, lý: 7.5"
result = re.findall(r"\d+(?:\.\d+)?", Text) # Số hoặc nếu (?) tồn tại dấu thập phân (.)
print(result)

Text = "Python là ngôn ngữ lập trình rất phổ biến!"
result = re.findall(r"\b\w+\b",Text) #Tạo ranh giới (\b) mà từ (\w) bao quanh nó
print(result)

Text = ["0912345678", "1234567890", "098", "0398765432"]
for Number in Text:
    if re.match(r"^(0|\+84)[0-9]{9,10}$", Number): # Bắt đầu từ 0 hoặc +84, còn lại chỉ xuất hiện 0 - 9, độ dài 9 - 10 chữ số
        print(Number)

Text = ["abc@gmail.com", "trang123@edu.vn", "user@site", "123@domain.co"]
for Email in Text :
    if re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", Email): #3 điều kiện : Chữ @ Chữ . Chữ
        print(Email)

Text = "Hôm nay Trang đi học cùng Minh và Hoa."
Words = re.findall(r"\b[A-Z][a-z]*\b", Text) #Ranh giới - (Chữ hoa + chữ thường) - Ranh giới
print(Words)

Text = "Bạn ấy thật là ngu và xấu tính."
Filter =  re.sub(r"\b(khùng|ngu|điên)\b", "***", Text) #Bắt đầu có chữ ***
print(Filter)

Text = "Liên hệ: admin@gmail.com, support@ctu.edu.vn hoặc trang_nguyen@abc.org"
Email = re.findall(r"[\w\.-]+@[\w\.-]+\.\w+", Text)
print(Email)

Text = ["abc123", "Abc@1234", "AbcdEfgh", "1234@Ab"]
for Pass in Text:
    if re.match(r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[\W_]).{8,}$",Pass) :
        print(Pass)

Text = "Ngày sinh của tôi là 15/04/2005 và ngày nhập học là 01/09/2023."
Date = re.findall(r"\d{2,4}/\d{2,4}/\d{2,4}", Text) # 1111/2222/3333 với 1 - 2 - 3 có thể là Ngày - Tháng - Năm hoặc tùy phổ biến
print(Date)

Text = "Danh sách: SV1001, SV2345, mã lỗi SVxx12, SV5678"
MaSV = re.findall(r"SV\d{4}", Text)
print(MaSV)