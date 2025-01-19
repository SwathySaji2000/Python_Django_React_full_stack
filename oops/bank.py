# # wap for bank acnt


class Bank:

    def user(self,name,ac_type,balance):

        self.name = name

        self.ac_type = ac_type
     
        self.balance = balance

        print(f"Welcome to our bank {name} have a nice day!")

    

    def withdrew(self, w_amount):


        if self.balance >= w_amount:
            print(f"The  transction successful")

            self.balance -= w_amount
            print(f"The current balance is: {self.balance}")
        else:
            print("Insufficient balance")   
    

    def deposit(self,d_amount):

        print(f"Your current balance is {self.balance + d_amount}")
        
obj = Bank()
obj.user(name="swathy",ac_type="savings",balance=5000)
obj.withdrew(w_amount=2000)
obj.deposit(d_amount=3000)   




         