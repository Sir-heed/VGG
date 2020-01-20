"""
A Command line Banking Application
"""

accounts = [{'username':'Kola', 'password':'password', 'balance':5000.0},{'username':'Ade', 'password':'password', 'balance':0.0}]
account_users = []
for account in accounts:
    account_users.append(account['username'])

def createAccount():
    print("=======================================================================================")
    print("Enter your details to create an account")
    username = input("Enter your Username: \n")
    password = input("Enter your password: \n")
    if username in account_users:
        print("Username has been taken.")
        createAccount()
    else:
        newUser = {'username':username, 'password':password, 'balance':0.0}
        accounts.append(newUser)
        print("Account has been created successfully!!!")

def deposit(user):
    amount = input("Enter the amount you wish to deposit: \n")
    user['balance'] = user['balance'] + float(amount)

def withdraw(user):
    amount = input("Enter the amount you wish to withdraw: \n")
    balance = user['balance'] - float(amount)
    if balance < 0 :
        print("Insufficient fund, You have to deposit more")
        deposit(user)
    else:
        user['balance'] = balance
        print("You withdrew " + amount + ", Your balance is " + str(user['balance']))

def transaction():
    print("=======================================================================================")
    print("Enter your details to authenticate your account")
    username = input("Enter your Username: \n")
    password = input("Enter your password: \n")
    user = {}
    if username in account_users:
        for account in accounts:
            if ((account['username'] == username) & (account['password'] == password)):
                user = account
                if len(user) < 1:
                    print("User is not registered")
                    createAccount()
                action = input("Press 1: Check balance \nPress 2: Deposit \nPress 3: Withdraw \nPress 4: Transfer \n")
                if action == '1':
                    print("Your balance is " + str(user['balance']))
                elif action == '2':
                    deposit(user)
                    print("Your balance is " + str(user['balance']))
                elif action == '3':
                    withdraw(user)
                elif action == '4':
                    beneficiary = input("Enter the beneficiary username: \n")
                    amount = input("Enter the amount you wish to transfer: \n")
                    ben_account = {}
                    if beneficiary in account_users:
                        for account in accounts:
                            if account['username'] == beneficiary:
                                ben_account = account
                        balance = user['balance'] - float(amount)
                        if balance < 0:
                            print("Insufficient fund, You have to deposit more")
                            deposit(user)
                        else:
                            user['balance'] = balance
                            ben_account['balance'] = ben_account['balance'] + float(amount)
                            print("Your transfer is successful.")
                            # print("You've successfully transfered " + amount + "to " + beneficiary['username'] + ". Your balance is " + str(user['balance']))
                    else:
                        print("Beneficiary account does not exist.")
                else:
                    print("Invalid Input")
    else:
        print("User is not registered")
        createAccount()
    # if (username in account_users & accounts['password'] == password):
    #     print("You are here")
        

userInput = input("Press 1: Create Account \nPress 2: Transaction \n")
if userInput == '1':
    createAccount()
elif userInput == '2':
    transaction()
else:
    print("You entered an invalid input")
print(accounts)