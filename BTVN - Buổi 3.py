def Split () :
    Chuoi = "Nguyen Van A"
    Tach = Chuoi.split(' ')
    for Tu in Tach :
        print(Tu)

#Split()

def Split_Condition() :
    Chuoi = "Cam , Tao , Le , Xoai"
    Tach = Chuoi.split(',')
    for Tu in Tach :
        print(Tu)

#Split_Condition()

def Split_Limit():
    Chuoi = "a-b-c-d"
    Tach = Chuoi.split('-',maxsplit=2)
    for Tu in Tach :
        print(Tu)

#Split_Limit()

def Join():
    Arr = ["HN","HCM","DN"]
    print(','.join(Arr))

#Join()

def Join_2() :
    Arr = ["data" , "science" , '101']
    print(' - '.join(Arr))

#Join_2()

def Fix_Join_Error() :
    print("-".join(["A","1","C"]))

#Fix_Join_Error()

def Split_Count():
    So_Tu = 0
    Chuoi = "Hello world, Python"
    Tach = Chuoi.split(' ')
    for Tu in Tach : 
        So_Tu += 1
    print(f"Chuoi : {Chuoi} co tong cong {So_Tu} tu")

#Split_Count()

def Split_Mutiple_Ways():
    Chuoi = "A,B;C,D;E"
    Tach = Chuoi.split(';')
    for Phan in Tach:
        for Tu in Phan.split(','):
            print(Tu)

#Split_Mutiple_Ways()

def Chuan_Hoa():
    Chuoi = "  XiN Chao   cAC   bAn  "
    Tach = Chuoi.split()
    for Tu in Tach:
        if Tu == '':
            Tach.remove(Tu)
    
    Chuoi = ' '.join(Tach)
    Chuoi = Chuoi.lower().title()
    print(Chuoi)

#Chuan_Hoa()

def Tu_Dien_Sang_Dict():
    Chuoi = "name=Alice;age=20;city=Hue"
    Tach = Chuoi.split(';')
    Tu_Dien = {}
    for Phan in Tach:
        Key, Value = Phan.split('=')
        Tu_Dien[Key] = Value
    print(Tu_Dien)

#Tu_Dien_Sang_Dict()

def Merge_Strings_Condition():
    Chuoi = ["CNTT1","","CNTT2","CNTT1","KT"]
    Chuoi_Moi = []
    for Tu in Chuoi:
        if Tu != "" and Tu not in Chuoi_Moi:
            Chuoi_Moi.append(Tu)
    print('|'.join(Chuoi_Moi))

#Merge_Strings_Condition()

def Cut_Log():
    Log = "2025-09-05 14:33:01 | INFO | user=trang | action=login"
    Thanh_Phan = Log.split('|')
    result = {}
    result['INFO'] = ""
    user_part = Thanh_Phan[2]
    action_part = Thanh_Phan[3]
    if '=' in user_part:
        key, value = user_part.split('=')
        result[key] = value
    if '=' in action_part:
        key, value = action_part.split('=')
        result[key] = value
    print(result)

#Cut_Log()

def Split_Sentence_Remove_Punctuation():
    Chuoi = "Xin chào, bạn ổn chứ? Mình học Python!"
    for char in ',.?!;:-_()[]}{"/''':
        Chuoi = Chuoi.replace(char, ' ')
    Tu_List = Chuoi.split()
    print(Tu_List)

#Split_Sentence_Remove_Punctuation()


def Join_Lines():
    lines = ["Ta","đi","giữa","đất","trời"]
    result = ' '.join(lines)
    print(result)

#Join_Lines()

def CSV_To_List_And_Back():
    csv = "1,2,3,4,5"
    num_list = [int(x) for x in csv.split(',')]
    print(num_list)
    csv_semicolon = ';'.join(str(x) for x in num_list)
    print(csv_semicolon)

#CSV_To_List_And_Back()
