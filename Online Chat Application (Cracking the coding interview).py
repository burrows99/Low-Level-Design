class ChatApplication:
    def __init__(self,name,url,server):
        self.name=name
        self.url=url
        self.server=server
    def createAccount(self,id,password):
        return(self.server.createAccount(id,password))
    def deleteAccount(self,id):
        return(self.server.deleteAccount(id))
    def login(self,id,password):
        return(self.server.login(id,password))
    def logout(self,id):
        return(self.server.logout(id))
    def sendMessage(self,senderId,recieverId,message):
        return(self.server.sendMessage(senderId,recieverId,message))
    def recieveMessage(self,id):
        return(self.server.recieveMessage(id))

class Server:
    def __init__(self,url,userService,messageService):
        self.url=url
        self.userService=userService
        self.messageService=messageService
    def createAccount(self,id,password):
        return(self.userService.createAccount(id,password))
    def deleteAccount(self,id):
        return(self.userService.deleteAccount(id))
    def login(self,id,password):
        return(self.userService.login(id,password))
    def logout(self,id):
        return(self.user.logout(self,id))
    def sendMessage(self,senderId,recieverId,message):
        return(self.messageService.sendMessage(senderId,recieverId,message))
    def recieveMessage(self,id):
        return(self.messageService.recieveMessage(id))
        
class Service:
    def __init__(self,url):
        self.url=url
        self.database={}

class UserService(Service):
    def __init__(self,url,sessionService):
        super().__init__(url)
        self.sessionService=sessionService
    def createAccount(self,id,password):
        if(id not in self.database):
            self.database[id]=password
            self.sessionService.addEntry(id)
            return(True)
        else:
            raise Exception('Account Already exists')
            return(False)
    def deleteAccount(self,id):
        if(id in self.database):
            del self.database[id]
            self.sessionService.removeEntry(id)
            return(True)
        else:
            raise Exception('Account Already exists')
            return(False)
    def login(self,id,password):
        if(id in self.database):
            if(self.database[id]==password):
                return(self.sessionService.login(id))
            else:
                raise Exception('Incorrect Password')
        else:
            raise Exception('Account does not exists.')
    def logout(self,id):
        return(self.sessionService.logout(id))

class SessionService(Service):
    def addEntry(self,id):
        self.database[id]=False
        return(True)
    def removeEntry(self,id,password):
        del self.database[id]
        return(True)
    def login(self,id):
        if(self.database[id]):
            raise Exception('Already logged in.')
        else:
            self.database[id]=True
            return(True)
    def logout(self,id):
        if(self.database[id]):
            self.database[id]=False
            return(True)
        else:
            raise Excpetion('Already logged out.')
    def getStatus(self,id):
        return(self.database[id])

class MessageService(Service):
    def __init__(self,url,sessionService):
        super().__init__(url)
        self.sessionService=sessionService
    def sendMessage(self,senderId,recieverId,message):
        if(self.sessionService.getStatus(senderId)):
            self.database[(senderId,recieverId)]=message
            return(True)
        else:
            raise Exception('Please login to send message.')
    def recieveMessage(self,id):
        listOfMessages=[]
        for messageDirection in self.database:
            if(messageDirection[1]==id):
                listOfMessages.append((messageDirection[0],self.database[messageDirection]))
        return(listOfMessages)
        
    
class User:
    def __init__(self,id,password,contactList,chatApplication):
        self.id=id
        self.password=password
        self.contactList=contactList
        self.chatApplication=chatApplication
    def createAccount(self):
        return(self.chatApplication.createAccount(self.id,self.password))
    def deleteAccount(self):
        return(self.chatApplication.deleteAccount(self.id))
    def login(self,id,password):
        return(self.chatApplication.login(id,password))
    def logout(self):
        return(self.chatApplication.logout(id))
    def sendMessage(self,recieverId,message):
        return(self.chatApplication.sendMessage(self.id,recieverId,message))
    def recieveMessage(self):
        return(self.chatApplication.recieveMessage(self.id))

sessionService=SessionService('sessionservice.com')
userService=UserService('userservice.com',sessionService)
messageService=MessageService('messageservice.com',sessionService)
server=Server('serverurl.com',userService,messageService)
chatApplication=ChatApplication('Whatsapp','www.whatsapp.com',server)
user1=User(0,'password',[],chatApplication)
user2=User(1,'password',[],chatApplication)
user1.createAccount()
user2.createAccount()
user1.login(0,'password')
user2.login(1,'password')
user1.sendMessage(1,'hi')
print(user2.recieveMessage())
