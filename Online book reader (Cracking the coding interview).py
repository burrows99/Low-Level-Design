import enum
class OnlineBookReader:
    def __init__(self,name,url,server):
        self.name=name
        self.url=url
        self.server=server
    def createAccount(self,id,password):
        return(self.server.createAccount(id,password))
    def deleteAccount(self,id):
        return(self.server.deleteAccount(id))
    def purchaseBook(self,customerId,bookId):
        return(self.server.purchaseBook(self,customerId,bookId))
    def readBook(self,customerId,book):
        return(self.server.readBook(self,customerId,book))
    def addBook(self,book):
        return(self.server.addBook(book))
    def removeBook(self,book):
        return(self.server.removeBook(book))
    

class Server:
    def __init__(self,url,bookService,customerService,paymentService,sessionService):
        self.url=url
        self.bookService=bookService
        self.customerService=customerService
        self.paymentService=paymentService
        self.sessionService=sessionService
    def createAccount(self,id,password):
        return(self.customerService.createAccount(id,password))
    def deleteAccount(self,id):
        return(self.customerService.deleteAccount(id))
    def purchaseBook(self,book):
        return(self.paymentService.purchaseBook(self,book))
    def readBook(self,book):
        return(self.paymentService.readBook(self,book))
    def addBook(self,book):
        return(self.bookService.addBook(book))
    def removeBook(self,book):
        return(self.bookService.removeBook(book))
        
class Service:
    def __init__(self,url):
        self.url=url
        self.database={}
        
class BookService(Service):
    def addBook(self,book):
        if(book.__getattribute__('id') in self.database):
            print('Book already present')
            return(False)
        else:
            self.database[book.__getattribute__('id')]=book
            return(True)
    def removeBook(self,book):
        try:
            del self.database[book.__getattribute__('id')]
            return(True)
        except:
            print('Book not in database')
            return(False)
            
class CustomerService(Service):
    def createAccount(self,id,password):
        if(id not in self.database):
            self.database[id]=password
            print('Account successfully created')
            return(True)
        else:
            print('Account already exists')
            return(False)
    def deleteAccount(self,id):
        if(id in self.database):
            del self.database[id]
            print('Account successfully deleted')
            return(True)
        else:
            print('Account doesnt exsist')
            return(False)
            
class PaymentService(Service):
    def purchaseBook(self,book):
        id=book.__getattrbiute__('id')
        if(self.database[id]==False):
            self.database[id]=True
            print('Purchased book successfully')
            return(True)
        else:
            print('Book already purchased ')
            return(False)
    def readBook(self,book):
        id=book.__getattrbiute__('id')
        if(id in self.database):
            if(self.databse[id]==True):
                print('Here is your book')
                return(book)
            else:
                print('Please purchase book first')
                return(False)
        else:
            print('Book unavailable')
            return(False)
            
class Book:
    def __init__(self,id,name,author,content,publisher,bookType):
        self.id=id
        self.name=name
        self.author=author
        self.content=content
        self.publisher=publisher
        self.bookType=bookType

class Account:
    def __init__(self,id,password,onlineBookReader):
        self.id=id
        self.password=password
        self.onlineBookReader=onlineBookReader
    def createAccount(self):
        return(self.onlineBookReader.createAccount(self.id,self.password))
    def deleteAccount(self):
        return(self.onlineBookReader.deleteAccount(self.id))
    
class AccountFactory(Account):
    def __init__(self,id,password,onlineBookReader,accountType):
        super().__init__(self,id,password,onlineBookReader)
        self.accountType=accountType
        if(accountType==AccountType.CUSTOMER):
            return(Customer(self.id,self.password,self.onlineBookReader))
        elif(accountType==AccountType.ADMIN):
            return(Admin(self.id,self.password,self.onlineBookReader))
        else:
            raise Exception('Account type invalid')

class Customer(Account):
    def purchaseBook(self,bookId):
        return(self.onlineBookReader.purchaseBook(self,self.id,bookId))
    def readBook(self,bookId):
        return(self.onlineBookReader.readBook(self,self.id,bookId))
        
class Admin(Account):
    def addBook(self,book):
        return(self.onlineBookReader.addBook(book))
    def removeBook(self,book):
        return(self.onlineBookReader.removeBook(book))
        
class BookType(enum.Enum):
    HARDCOVER=1
    PAPERBACK=2
    MAGAZINE=3
    NEWSPAPER=4

class AccountType(enum.Enum):
    CUSTOMER=1
    ADMIN=2
