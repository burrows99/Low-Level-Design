import enum
class ATM:
    def __init__(self,bankName,location,server):
        self.bankName=bankName
        self.location=location
        self.moneybox=[[]]*len(Denomination)
        self.server=server
    def addBundle(self,account,bundle):
        if(type(account)==AccountType.MANAGER):
            if(self.server.loginstatus(self,account.id)):
                if(bundle.denomination==Denominatio.HUNDRED):
                    while(bundle.quanity):
                        self.moneybox[0].append(Note(100))
                        bundle.quantity-=1
                if(bundle.denomination==Denominatio.FIVEHUNDRED):
                    while(bundle.quanity):
                        self.moneybox[1].append(Note(500))
                        bundle.quantity-=1
                if(bundle.denomination==Denominatio.THOUSAND):
                    while(bundle.quanity):
                        self.moneybox[2].append(Note(1000))
                        bundle.quantity-=1
            else:
                print('Login to add bundle')
        else:
            print('Unauthorized')
    def login(self,customerId,pin):
        return(self.server.login(customerId,pin))
    def logout(self,customerId):
        return(self.server.logout(customerId))
    def checkstatement(self,customerId):
        return(self.server.checkStatement(customerId))
    def withdraw(self,customerId,amount):
        return(self.server.withdraw(customerId,amount))
        
class Server:
    def __init__(self,url):
        self.url=url
        self.accountDatabase={}
        self.balanceDatabase={}
        self.sessionDatabase={}
    def login(self,customerId,pin):
        if(customerId in self.accountDatabase):
            self.sessionDatabse[customerId]=True
            return(True)
        else:
            return(False)
    def logout(self,customerId):
        if(customerId in self.accountDatabase):
            self.sessionDatabse[customerId]=False
            return(True)
        else:
            return(False)
    def checkstatement(self,customerId):
        return(self.balanceDatabase[customerId])
    def withdraw(self,customerId,amount):
        if(self.balanceDatabase[customerId]>=amount):
            self.balanceDatabase[customerId]-=amount
            return(True)
        else:
            return(False)

class Bundle:
    def __init__(self,denomination,quantity):
        self.denomination=denomination
        self.quantity=quantity
        
class Note:
    def __init__(self,value):
        self.value=value

class Account:
    def __init__(self,id,pin,atm):
        self.id=id
        self.pin=pin
        self.atm=atm
    def login(self):
        return(self.atm.login(self,self.id,self.pin))
    def logout(self):
         return(self.atm.logout(self,self.id))

class Customer(Account):
    def checkstatement(self):
        return(self.atm.checkStatement(self,self.id))
    def withdraw(self,amount):
        return(self.atm.withdraw(self,self.id,amount))

class Manager(Account):
    def addBundle(self,bundle):
        return(self.atm.addBundle(self,self.id,bundle))
        
class AccountFactory(Account):
    def __init__(self,id,pin,atm,accountType):
        super().__init__(id,pin,atm)
        if(accountType==AccountType.CUSTOMER):
            return(Customer(id,pin,atm))
        elif(accountType==AccountType.MANAGER):
            return(MANAGER(id,pin,atm))
        else:
            return(None)
    
class AccountType(enum.Enum):
    CUSTOMER=1
    MANAGER=2
        
class Denomination(enum.Enum):
    HUNDRED=100
    FIVEHUNDRED=500
    THOUSAND=1000
    
