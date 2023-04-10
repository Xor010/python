class Bank:

    balance = 0
    name    = ''
    age     = 18
    def __init__(self, b, n, a):
        if a > self.age:
            self.balance = b
            self.age = a
            self.name = n
            print(f'Welcome {self.name } your balance = { b }')
        else:
            print(f'sorry you must be over than 18y')
    def add_b(self,b):
        self.balance += b
        return self.balance
    def profile(self):
        print(self.name, self.age,self.balance)
        return
b1 = Bank(10, 'ahmed', 20)
print(b1.add_b(50))

ali = Bank(1000, 'ali', 300)
print(b1.add_b(54440))
ali.profile()