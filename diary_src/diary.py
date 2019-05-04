class Diary:
    def __init__(self):
        self.buf = ""
        self.date_list = []
    
    def diary_write(self, date):
        self.diary_file = open('diary.txt', 'r'); 
        
        while True: #check opberlapped date! 
            self.line = self.diary_file.readline()
            if not self.line: break 
            if self.line.rstrip('\n') == date:
                print("date is overlapped!")
                self.diary_file.close()
                return
        self.diary_file.close()
        
        #write mode
        self.diary_file = open('diary.txt', 'a');
        self.diary_file.write('\n'+date+"\n")
    
        #input until not input 
        while True:
            self.buf = input("input your string : ")
            if self.buf == "":
                break
            else:
                self.buf+="\n"
                self.diary_file.write(self.buf)
        self.diary_file.close()
        return

    #readl to file  and check exist date! 
    def diary_read(self, date):
        self.diary_file = open('diary.txt', 'r'); 
        while True: #check opberlapped date! 
            self.line = self.diary_file.readline()
            if not self.line: break 
            if self.line.rstrip('\n') == date: 
                while True:
                    if self.line == "":
                        break
                    self.line=self.diary_file.readline().rstrip('\n')
                    print(self.line)
                self.diary_file.close()
                return
        print("hey...none exist date!")
        self.diary_file.close()
        return

 

diary = Diary()

while True:
    select = (input("input your choice, 1) write, 2) read, 3) exit : "))
    if select == '1':
        date = input("choice your date want to write! : ")
        diary.diary_write(date)

    elif select == '2':
        date = input("choice your date want to read : ")
        diary.diary_read(date)

    elif select == '3':
        exit()

    else:
        print("your choice is Wrong here is My flag{Python_is_so_powerful!}")

