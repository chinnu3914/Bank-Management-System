class bank():
    def __init__(self,account_number,account_name):
        self.number=account_number
        self.name=account_name
        self.__balance=0
        self.history=[]

    def set_balance(self,amount):
        if amount <=0:
            print("-"*10)
            print("Amount greater than 0")
            print("-"*10)
        else:
            self.__balance=amount

    def get_balance(self):
            return self.__balance
            _
    def deposit(self,amount):
         if amount<0:
             print("-"*10)
             print("no negative numbers")
             print("-"*10)
         else:
           self.__balance+=amount
           self.history.append(f"deposit amount {amount}")
           print("-"*10)
           print("Amount deposited sucessfully")
           print("-"*10)
        
    def withdraw(self,amount):
        if amount > self.__balance or amount <0:
            print("-"*10)
            print("Insufficient funds or no negative vaues ")
            print("-"*10)
            return
        else:
             self.__balance -= amount
             self.history.append(f"withdrawl amount {amount}")
             print("-"*10)
             print("Amount withdrawl sucessfully")
             print("-"*10)

    def transaction(self,reciever,amount):
        
        if amount<0 or amount >self.__balance:
            print("-"*10)
            print("invalid amount or insufficient balance")
            print("-"*10)
            return

        else:
            self.__balance -=amount
            reciever.__balance+=amount
            self.history.append(f"Amount transfer {amount} to {reciever.name}")
            reciever.history.append(f"Amount recieved {amount} frm{self.name}")
            print("-"*10)
            print("Transaction Sucessfull")
            print("-"*10)

    def display(self):
         print("-"*10)
         print("Account number  :",self.number)
         print("Account Name    :",self.name)
         print("Account Balance :",self.__balance)

    def show_history(self):
        if len(self.history)==0:
            print("no transacton history")
            return
        print("-" * 30)
        print(f"Transaction History of {self.name}")
        print("-" * 30)
        for transaction in self.history:
            print(transaction)

    def save_data(self):
        return f"{self.number} {self.name} {self.__balance}\n"

accounts={
     
}
def add_account():
    try:
        number=int(input("Enter the account number  : "))
        name=input("enter the account name          : ")
        balance=int(input("enter the account balance: "))
        if number in accounts:
            print("-"*10)
            print("id already exist")
            print("-"*10)
            return
        if number <= 0 or balance <0:
             print("-"*10)
             print("--------They are not in the negative-------")
             print("-"*10)
             return

        acc=bank(number,name)
        acc.set_balance(balance)
        accounts[number]=acc

    except Exception as e:
         print("unexpected error : ",e)


def search():

    try:

        number=int(input("enter the account number :"))
    
        if number not in accounts:
            print(" --------account not found------ ")
            return

        else:
            value=accounts[number]
            value.display()

    except Exception as e:
         print("unexpected error :",e)


def withdrawl():
    number =int(input("enter the number :"))
    amount=int(input("enter the amount :"))
    if number not in accounts:
        print("Account not found")
    else:
        value=accounts[number]
        value.withdraw(amount)
        print("-"*10)
        print("amount with drawl sucessfully")
        print("-"*10)

def deposit():
    number =int(input("enter the number"))
    amount=int(input("enter the amount "))
    if number not in accounts:
        print("-"*10)
        print("Account not found")
        print("-"*10)
        return
    else:
        value=accounts[number]
        value.deposit(amount)
        print("-"*10)
        print("amount deposited sucessfully")
        print("-"*10)
def history():
    account_number=int(input("enter the account number"))
    if account_number not in accounts:
        print("Account not found")
        return
    accounts[account_number].show_history()

def transaction():
    sender_accountnumber=int(input("entet the account number"))
    reciever_accountnumber=int(input("enter the recievers account number"))
    amount=int(input("enter the amount to transfer"))
    if sender_accountnumber not in accounts:
        print("-"*10)
        print("sender account not found in the accounts")
        print("-"*10)
        return
    if reciever_accountnumber not in  accounts:
        print("-"*10)
        print("reciever account not in the account")
        print("-"*10)
        return

    sender=accounts[sender_accountnumber]
    reciver=accounts[reciever_accountnumber]

    sender.transaction(reciver,amount)
 
def showall():
    for id in accounts:
        value=accounts[id]
        value.display()
def save_file():
    with open ("banks.txt","w")as file:
        for name,details in accounts.items():
            file.write(details.save_data())

        print("Saved sucessfully")

while True:
    print("------------------------")
    print(" choose an option :")
    print("------------------------")
    print("1.add_account")
    print("2.withdrawl")
    print("3.deposit")
    print("4.search")
    print("5.show all")
    print("6.save to accounts")
    print("7.Transaction")
    print("8.Transaction history")
    print("9.exit")
    ch=int(input("enter the option : "))
    if ch==1:
        add_account()
    elif ch==2:

        withdrawl()
    elif ch== 3:
        deposit()
    elif ch==4:
        search()
    elif ch==5:
        showall()
    elif ch==6:
        save_file()
    elif ch==7:
        transaction()
    elif ch==8:
        history()
    elif ch==9:
        break
    else:
        print("invalid option")




               
     
         



              