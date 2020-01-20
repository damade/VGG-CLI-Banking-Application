import webbrowser
import math
import random
import re


bankAccounts = { 'damilola5@gmail.com':{'password':'dammy','balance':5000.00},
                 'adeoye.damilola@gmail.com':{'password':'adeoye123','balance':1500.00}}

regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'

class Transaction:
    def __init__(self):
        return

    def deposit(self, x, y):
        self.a = x
        self.b = y
        cD = self.a + self.b
        return cD

    def transfer(self, x, y):
        self.a = x
        self.b = y
        cT = self.a - self.b
        return cT

    def withdraw(self, x, y):
        self.a = x
        self.b = y
        cW = self.a - self.b
        return cW

transactCalc = Transaction();

def transactionAnyOther(account):
    print("\n-------------KINDLY CHOOSE WHAT NEXT-------------\n")
    print("1. Do you want to perform any transaction?")
    print("2. Do you want to return to home page?")
    print("3. Do you want to exit\n")
    promptQuestion = input("Reply: ")
    if (promptQuestion == '1'):
       transactionOptions(account)
    elif (promptQuestion == '2'):
        homePage()
    elif (promptQuestion == '3'):
        exit()
    else:
        exit()

def homeAnyOther():
    print("\n-------------KINDLY CHOOSE WHAT NEXT-------------\n")
    print("1. Do you want to return to home page?")
    print("2. Do you want to exit\n")
    promptQuestion = input("Reply: ")
    if (promptQuestion == '1'):
        homePage()
    elif (promptQuestion == '2'):
        exit()
    else:
        exit()

def verifyAccount(email):
   if email in bankAccounts.keys():
       return email
   return False

def createAccount():
    print("\n-------------CREATE NEW ACCOUNT-------------")
    newEmail = input("Enter a valid email address: ").lower();
    if(re.search(regex,newEmail)):
        if verifyAccount(newEmail):
            print("Email Address Already exists! Try again")
            createAccount()
        else:
            newPassword = input("Enter a valid password: ")
            confirmNewPassword = input("Confirm password for entry: ")
            if((len(newPassword) >= 6) and (newPassword == confirmNewPassword)):
                bankAccounts[newEmail] = {'password': newPassword,'balance': 0.00}
                print("Your account has been created successfully!")
                homePage()
    else:
        print("Invalid Email Address")
        createAccount();

def authenticateUser():
    print("\n-------------LOG IN-------------")
    userEmail = input("Enter email address: ").lower()
    userPassword = input("Enter password: ")
    if userEmail in bankAccounts.keys():
        if bankAccounts[userEmail]['password'] == userPassword:
            transactionOptions(userEmail);
    else:
        print("You are not authorized!\n---------------------------\nCreate an Account\n")
        print("\n-------------KINDLY CHOOSE WHAT NEXT-------------\n")
        print("1. Do you want to attempt the log in again?")
        print("2. Do you want to return to home page?")
        print("3. Do you want to open an Account with us\n")
        promptQuestion = input("Reply: ")
        if(promptQuestion == '1'):
            authenticateUser()
        elif(promptQuestion == '2'):
            homePage()
        elif(promptQuestion == '3'):
            createAccount()
        else:
            exit()

def transactionOptions(account):
    print("\n******** TRANSACTION PAGE ********")
    print(" Press 1: Check Balance")
    print(" Press 2: Deposit")
    print(" Press 3: Withdraw")
    print(" Press 4: Transfer")
    print(" Press 0: Home")
    theOptionSelected = int(input("Reply: "))
    if theOptionSelected == 1:
        Balance(account);
    elif theOptionSelected == 2:
        Deposit(account);
    elif theOptionSelected == 3:
        Withdraw(account);
    elif theOptionSelected == 4:
        Transfer(account);
    elif theOptionSelected == 0:
        homePage()
    else:
        print("Enter a valid response")
        transactionOptions()

def Balance(account):
    print("\n******** CHECK BALANCE ********\n")
    print("Your account balance is: ",bankAccounts[account]['balance'])
    transactionAnyOther(account)

def Withdraw(account):
    print("\n******** MAKE WITHDRAWAL ********\n")
    withdrawalAmount = int(input("Input amount to withdraw:\n"))
    oldBalance = bankAccounts[account]['balance']

    if oldBalance == 0.00:
        print("You have no money in your account.\nKindly make deposit and try again\n")
        transactionAnyOther(account)
    elif oldBalance < withdrawalAmount:
        print("Cannot withdraw more than you have in your account\n")
        transactionAnyOther(account)
    else:
        newBalance = transactCalc.withdraw(oldBalance,withdrawalAmount);
        bankAccounts[account]['balance'] = newBalance
        print("\n========== Withdrawal Sucessful ==========\n Amount withdrawn: "
              +str(withdrawalAmount)+"\nCurrent available balance: " + str(newBalance));
        transactionAnyOther(account)
        
def Transfer(account):
    print("\n******** MAKE TRANSFER ********\n")
    beneficiaryAccount = input("Enter beneficiary's email: ").lower()
    transferAmount = int(input("Input amount to be transfered:\n"))
    oldBalance = bankAccounts[account]['balance']

    if transferAmount > oldBalance:
        print("You have *** Insufficient *** funds to perform transaction!"
              "\nKindly make deposit and try again\n")
        transactionAnyOther(account)
    else:
        if verifyAccount(beneficiaryAccount):
            #making the effect of the transfer on the beneficiary's account
            beneficiaryBalance = bankAccounts[beneficiaryAccount]['balance']
            beneficiaryCurrentBal = beneficiaryBalance + transferAmount
            bankAccounts[beneficiaryAccount]['balance'] = beneficiaryCurrentBal;
            # User's current balance after transfer
            newBalance = transactCalc.withdraw(oldBalance, transferAmount);
            bankAccounts[account]['balance'] = newBalance
            print("\n========== Transfer Sucessful ==========\n Amount transfered: "
              + str(transferAmount) + "\nBeneficiary's email: " + beneficiaryAccount);
            transactionAnyOther(account)
        else:
            print("\n========== Transfer Failed ==========\n ------- Invalid Beneficiary -------\n")
            transactionAnyOther(account)
    
def Deposit(account):
    print("\n******** MAKE DEPOSIT ********\n")
    depositAmount = int(input("Enter amount to deposit:\n"))
    oldBalance = bankAccounts[account]['balance']
    newBalance = transactCalc.deposit(oldBalance,depositAmount);
    bankAccounts[account]['balance'] = newBalance
    print("\n********Deposit Successful ********\nAmount deposited: "+str(depositAmount)+"\nAvailable balance: "+str(newBalance));
    transactionAnyOther(account)

def homePage():
    print("\n---------------WELCOME TO VGG BANK---------------\n")
    print("<<<<<<<<<< HOME PAGE >>>>>>>>>>\n")
    print("1. Are you a new customer and you want to open an account with us?")
    print("2. Are you an existing customer and you want to transact?")
    print("3. Do you want to exit\n")

    promptQuestion = int(input("Reply: "))
    if (promptQuestion == 1):
        createAccount()
    elif (promptQuestion == 2):
        authenticateUser()
    elif (promptQuestion == 0):
        exit()
    else:
        print("Enter a valid option")
        homeAnyOther()


homePage();

