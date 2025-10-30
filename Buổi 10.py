import random
class Game():
    def __init__(self):
        self.Win = 0
        self.Lost = 0
        self.Total = 0
            
    def Add_Record(self,W,L,T):
        self.Win += W
        self.Lost += L
        self.Total += T
        
    def Show_History(self,History):
        for Record in History:
            print(Record)
        
    def DoanSo(self):
        Win = 0
        Lost = 0
        Total = 0
        PlayNo = 0
        History = []
        while(True):
            PlayNo += 1
            Number = random.randint(1,10)
            Guess = int(input(f"Nhap so ban dang doan tu {1} -> {10} | 0 để thoát game :"))
            if (Guess == 0):
                break
            if (Guess == Number) :
                print("Bạn đã đoán đúng! Bạn thắng!")
                Win += 1
            elif (Guess != Number) :
                print(f"Sai rồi! Số đúng là {Number}")
                Lost+= 1
            Total += 1
            History.append(f"{PlayNo:<4} | {Number:<2} | {Guess:<2} | {'Win' if Guess == Number else 'Lose'}")
        self.Add_Record(Win,Lost,Total)
        print("Lần chơi |   Số   |   Đoán   | Kết quả")
        self.Show_History(History)
        print(f"Thông số - Tổng số lần chơi : {Total} | Tổng số lần thắng : {Win} ")
        
    def DoanXu(self):
        Win = 0
        Lost = 0
        Total = 0
        PlayNo = 0
        History = []
        Xu = ["Xấp","Ngửa"]
        while(True):
            PlayNo += 1
            Guess = input(f"Chọn mặt đồng xu (Xấp - Ngửa) | 0 để thoát game :").lower()
            Mat_Xu = random.choice(Xu)
            if (Guess == '0'):
                break
            if (Guess == Mat_Xu.lower()) :
                print("Bạn đã đoán đúng! Bạn thắng!")
                Win += 1
            elif (Guess != Mat_Xu.lower()) :
                print(f"Sai rồi! Mặt đồng xu là : {Mat_Xu}")
                Lost+= 1
            Total += 1
            History.append(f"{PlayNo:<4} | {Mat_Xu:<2} | {Guess:<2} | {'Win' if Guess == Mat_Xu.lower() else 'Lose'}")
        self.Add_Record(Win,Lost,Total)
        print("Lần chơi | Mặt xu | Đoán | Kết quả")
        self.Show_History(History)
        print(f"Thông số hiện tại - Tổng số lần chơi : {Total} | Tổng số lần thắng : {Win} ")
    
    def List_Of_Cards(self):
        Chat = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        Hang = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
        Full_Deck = []
        for loai in Chat:
            for so in Hang:
                Full_Deck.append(f"{so} of {loai}")
        random.shuffle(Full_Deck)
        return Full_Deck
    
    def Value_Of_Cards(self,Cards):
        value = 0
        for card in Cards:
            if card.split(' ')[0].isdigit() and 2 <= int(card.split(' ')[0]) <= 9:
                value += int(card.split(' ')[0])
            elif card.split(' ')[0] in ('10', 'Jack', 'Queen', 'King'):
                value += 10
        for card in Cards:
            if (card.split(' ')[0] == 'Ace'):
                if (value + 11 <= 21):
                    value += 11
                else:
                    value += 1
        return value 

    def BlackJack(self):
        Win = 0
        Lost = 0
        Total = 0
        PlayNo = 0
        History = []
        while (True):
            PlayNo += 1
            chon = 0
            Host_Hand = []
            Your_Hand = []
            bai = self.List_Of_Cards()
            Host_Hand.append(bai.pop(0))
            Your_Hand.append(bai.pop(0))
            Host_Hand.append(bai.pop(0))
            Your_Hand.append(bai.pop(0))
            print(f"Người chơi : {Your_Hand} | Giá trị : {self.Value_Of_Cards(Your_Hand)}")
            while (chon != 2):
                chon = int(input("1 - Lấy tiếp bài | 2 - Dừng bài"))
                if chon == 1:
                    Your_Hand.append(bai.pop(0))
                    print(f"Người chơi : {Your_Hand} | Giá trị : {self.Value_Of_Cards(Your_Hand)}")
                    if (self.Value_Of_Cards(Your_Hand) > 21):
                        break
                if (chon == 2) :
                    print(f"Nhà cái : {Host_Hand} | Giá trị : {self.Value_Of_Cards(Host_Hand)}")
                    while ((self.Value_Of_Cards(Host_Hand) < self.Value_Of_Cards(Your_Hand)) and self.Value_Of_Cards(Your_Hand) <= 21) :
                        Host_Hand.append(bai.pop(0))
                        print(f"Nhà cái : {Host_Hand} | Giá trị : {self.Value_Of_Cards(Host_Hand)}")
                else :
                    print("Nhập sai")
            print("Kết quả : ")
            print(f"Nhà cái : {Host_Hand} | Giá trị : {self.Value_Of_Cards(Host_Hand)}")
            print(f"Người chơi : {Your_Hand} | Giá trị : {self.Value_Of_Cards(Your_Hand)}")
            if (self.Value_Of_Cards(Host_Hand) > self.Value_Of_Cards(Your_Hand) or self.Value_Of_Cards(Your_Hand) > 21):
                Lost+= 1
            elif (self.Value_Of_Cards(Host_Hand) < self.Value_Of_Cards(Your_Hand)) :
                Win += 1
            Total += 1
            History.append(f"{PlayNo:<10} | {self.Value_Of_Cards(Host_Hand):<10} | {self.Value_Of_Cards(Your_Hand):<10} | {'Win' if self.Value_Of_Cards(Host_Hand) < self.Value_Of_Cards(Your_Hand) else 'Lose'}")
            if (input("Nhập 0 để kết thúc chương trình") == '0'):
                break
        self.Add_Record(Win,Lost,Total)
        print("Lần chơi | Nhà cái | Người chơi | Kết quả")
        self.Show_History(History)
        print(f"Thông số hiện tại - Tổng số lần chơi : {Total} | Tổng số lần thắng : {Win} ")
                
    
def Menu():
    print("1. Đoán số")
    print("2. Đoán mặt xu")
    print("3. BlackJack")
    print("--------------")
    print("0. Thoát chương trình")
    
    
def Process():
    Player = Game()
    while (True):
        Menu()
        chon = int(input("Chọn chương trình thực thi : "))
        if (chon == 1):
            Player.DoanSo()
        elif (chon == 2):
            Player.DoanXu()
        elif (chon == 3):
            Player.BlackJack()
            
        elif (chon == 0):
            break
        
Process()
