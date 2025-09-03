# Bài 1
def MixMinList():
    a = [3,9,1,4]
    b = [2,7,4,3,2,8]

    min = len(a) if len(a) < len(b) else len(b)
    c = b if len(a) < len(b) else a

    for i in range(min):
        if a[i] < b[i] :
           c [i] = a[i]

    return c

print(f"Result : {MixMinList()}")

# Bài 2
def CreateListByCondition():
    a = [1,2,3,4,5,6,7,8,9,0]
    b = [11,12,13,14,15,16,17,18,19,20]
    c = []

    for i in a :
        if i % 2 != 0:
            c.append(i)
    for i in b :
        if i % 2 == 0 :
            c.append(i)

    return c

print(f"Result : {CreateListByCondition()}")

import random
# Bài 3
def createList():
    Dong = int(input("Nhap so dong cua ma tran : "))
    Cot = int(input("Nhap so cot cua ma tran : "))
    a = []

    for i in range(Dong) :
        b = []
        for j in range (Cot) :
            b.append(int(random.uniform(-100, 100)))
        a.insert(i,b)

    print(a)
    return a

Arr = createList()

def MeasureList(a) :
    Row = Column = MaxColumn = 0
    for i in a :
        Row += 1
        Column = 0
        for j in i :
            Column += 1
        if MaxColumn < Column :
            MaxColumn = Column
    return Row, MaxColumn

# Câu a
def Tinh_DuongCheo(a) :
    Row , Column = MeasureList (a)
    Sum_DCC = Sum_DCP = 0
    if Row == Column:
        for i in range(Row):
            Sum_DCC += a[i][i]
            Sum_DCP += a[i][Row - i - 1]
        print(f"Tong duong cheo chinh: {Sum_DCC}")
        print(f"Tong duong cheo phu: {Sum_DCP}")
        return Sum_DCC, Sum_DCP
    else:
        print("Ma tran khong phai la ma tran vuong")
        return None, None

DCC,DCP = Tinh_DuongCheo(Arr)

# Câu b
def AbsArr(Arr) :
    x = y = 0
    for i in Arr:
        y = 0
        for j in i :
            if j < 0 :
                Arr[x][y] *= -1
            y += 1         
        x += 1

    print(Arr)
    return Arr

Arr = AbsArr(Arr)

# Câu c
def DoiSoChanThanhX(Arr,X) :
    x = y = 0
    for i in Arr:
        y = 0
        for j in i :
            if j % 2 == 0 :
                Arr[x][y] = X
            y += 1         
        x += 1
    print(Arr)
    return Arr

Arr = DoiSoChanThanhX(Arr,0)

# Câu d
def checkChanArr(Arr) :
    Check = True
    for i in Arr :
        for j in i :
            if j % 2 != 0 :
                Check = False
    if (Check) :
        print("Mot mang toan so chan")
        return True
    else :
        print ("Mot mang khong hoan toan so chan")
        return False

checkChanArr(Arr)

# Câu e
def ArrDoiXung(Arr) :
    Row, Column = MeasureList(Arr)
    if Row == Column:
        for i in range(Row):
            for j in range(Column):
                if Arr[i][j] != Arr[j][i]:
                    print("Ma tran khong doi xung")
                    return False
        print("Ma tran doi xung")
        return True
    else:
        print("Ma tran khong phai la ma tran vuong")
        return False

ArrDoiXung(Arr)

# Câu f
def DCC_Increase(Arr) :
    Row, Column = MeasureList(Arr)
    Check = False
    if Row == Column:
        Check = True
        Max = Arr[0][0]
        for i in range (Row) :
            if (Max < Arr[i][i] or i == 0):
                Max = Arr[i][i]
            else :
                Check = False
    if Check :
        print ("Duong cheo chinh tang dan")
        return True
    else:
        print("Duong cheo chinh khong tang dan")
        return False

DCC_Increase(Arr)

# Câu g
def XuatTamGiacDuoiDuongCheoPhu(Arr):
    Row, Column = MeasureList(Arr)
    if Row == Column:
        print("Cac phan tu thuoc tam giac duoi cua duong cheo phu")
        for i in range(Row):
            for j in range(Row):
                if i + j >= Row - 1:
                    print(Arr[i][j], end=' ')
        print()
    else:
        print("Ma tran khong phai la ma tran vuong")

XuatTamGiacDuoiDuongCheoPhu(Arr)

# Câu h
def DCP_Decrease(Arr) :
    Row, Column = MeasureList(Arr)
    Check = False
    if Row == Column:
        Check = True
        Min = Arr[Row - 1][Row - 1]
        for i in range (Row) :
            if (Min > Arr[i][Row - i - 1] or i == 0):
                Min = Arr[i][Row - i -1]
            else :
                Check = False
    if Check :
        print ("Duong cheo phu giam dan")
        return True
    else:
        print("Duong cheo phu khong giam dan")
        return False

DCP_Decrease(Arr)