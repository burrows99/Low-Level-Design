import enum
class CallCenter:
    def __init__(self,numberOfRespondents,numberOfManagers,director):
        self.numberOfRespondents=numberOfRespondents
        self.numberOfManagers=numberOfManagers
        self.respondents=[]
        self.managers=[]
        self.initialize()
        self.director=director
    def dispatchCall(self):
        for employee in self.respondents:
            if(employee.availability):
                employee.availability=False
                return(employee)
        for employee in self.managers:
            if(employee.availability):
                employee.availability=False
                return(employee)
        if(director.availability):
            director.availability=False
            return(director)
        raise Exception('No one available')
    def initialize(self):
        for id in range(self.numberOfRespondents):
            self.respondents.append(EmployeeFactory(id,True,EmployeeType.RESPONDENT))
        for id in range(self.numberOfManagers):
            self.managers.append(EmployeeFactory(id,True,EmployeeType.MANAGER))
        
class Employee:
    def __init__(self,id,availability=True):
        self.id=id
        self.availability=availability
        
class Respondent(Employee):
    pass

class Manager(Employee):
    pass

class Director(Employee):
    pass

class EmployeeFactory(Employee):
    def __init__(self,id,availability,employeeType):
        super().__init__(id,availability)
        self.employeeType=employeeType
    def get(self):
        if(self.employeeType==EmployeeType.RESPONDENT):
            return(Respondent(self.id,self.name,self.availability))
        elif(self.employeeType==EmployeeType.MANAGER):
            return(Respondent(self.id,self.name,self.availability))
        elif(self.employeeType==EmployeeType.DIRECTOR):
            return(Respondent(self.id,self.name,self.availability))
        else:
            raise Exception('Incorrect employee type.')

class EmployeeType(enum.Enum):
    RESPONDENT=1
    MANAGER=2
    DIRECTOR=3
    
director=EmployeeFactory(1,True,EmployeeType.DIRECTOR)
callcenter=CallCenter(10,10,director)
while(True):
    print(callcenter.dispatchCall())
