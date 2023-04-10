class users():
    #balance = 0
    #name    = ''
    age     = 18
      
    def __init__(self, b, n, a):
        if a > self.age:
            
            self.age = a
            self.name = n
            print(f'Welcome {self.name } your balance = { b }')
        else:
            print(f'sorry you must be over than 18y')
    def profile(self):
        print(self.name, self.age,self.balance)
        return  
class Bank(users):
    def __init__(self, b, n, a):
        super().__init__(b, n, a)
        self.balance = b
    def add_b(self,b):
        self.balance += b
        return self.balance
   
    def withdraw(self , hm):
        if hm < self.balance:
            self.balance -= hm
            print(f'you withdraw {hm} and your credit {self.balance}')
            return
        print(f'sorry you don\'t have credit {self.balance}')
        return
    

b1 = Bank(10, 'ahmed', 20)
print(b1.add_b(50))

ali = Bank(1000, 'ali', 300)
print(b1.add_b(54440))
ali.profile()
ali.withdraw(100)
ali.profile()
ali.withdraw(899)
ali.profile()
ali.withdraw(2)