import enum
import datetime
class ParkingLot:
    def __init__(self,numberOfEntryGates,numberOfExitGates,numberOfFloors,server):
        self.numberOfEntryGates=numberOfEntryGates
        self.numberOfExitGates=numberOfExitGates
        self.floors=[None]*numberOfFloors
        self.initialize()
        self.entryGuard=Employee(1,EmployeeType.ENTRYGUARD)
        self.exitGuard=Employee(1,EmployeeType.EXITGUARD)
        self.server=server
    def addCar(self,car):
        for floor in self.floors:
            if(floor.addCar(car)):
                self.server.addEntry(car.__getattribute('registrationNumber'),self.entryGuard.noteTime())
                return(True)
        return(False)
    def removeCar(self,registrationNumber):
        for floor in self.floors:
            if(floor.removeCar(registrationNumber)):
                print('Car removed')
                self.server.removeEntry(self,registrationNumber)
                return(bill)
        print('Car could not be removed')
        return(False)
    def getBill(self):
        bill=self.server.getBill(registrationNumber)
        return(bill)
    def initialize(self):
        for n in range(len(self.floors)):
            self.Floors[n]=Floor(n,10,10,10)
        
class Floor:
    def __init__(self,floorNumber,numberOfSmallSpots,numberOfMediumSpots,numberOfLargeSpots):
        self.floorNumber=floorNumber
        self.small=[None]*numberOfSmallSpots
        self.medium=[None]*numberOfMediumSpots
        self.large=[None]*numberOfLargeSpot
        self.initalize()
    def addCar(self,car):
        if(car.__getattribute__('carType')==SpotType.SMALL):
            for n in range(len(self.small)):
                if(self.small[n].addCar(car)):
                    return(True)
            return(False)
    def removeCar(self,registrationNumber):
        for n in range(self.small):
            if(self.small[n].removeCar(regitrationNumber)):
                return(True)
        return(False)
    def initialize(self):
        for n in range(len(self.small)):
            self.small[n]=Spot(n,SpotType.SMALL,True)
        for n in range(len(self.medium)):
            self.medium[n]=Spot(n,SpotType.MEDIUM,True)
        for n in range(len(self.large)):
            self.large[n]=Spot(n,SpotType.LARGE,True)
            
class Spot:
    def __init__(self,id,spotType,status):
        self.id=id
        self.spotType=spotType
        self.status=status
        self.spot=None
    def addCar(self,car):
        if(self.status==True):
            if(car.__getattribute__('carType')==self.spotType):
                self.status=False
                self.spot=car
                return(True)
            else:
                print('Please park at the correct spot type')
                return(False)
        else:
            raise Exception('Spot full')
    def removeCar(self,registrationNumber):
        if(self.status==False):
            if(self.spot.__getattribute__('regitrationNumber')==registrationNumber):
                self.status=True
                self.spot=None
                return(True)
            else:
                print('Different Car present here.')
                return(False)
        else:
            print('Spot already vacant')
            return(False)
    
class Car:
    def __init__(self,registrationNumber,carType):
        self.registraionNumber=registrationNumber
        self.carType=carType
        
class Employee:
    def __init__(self,id,employeeType):
        self.id=id
        self.employeeType=employeeType
    def noteTime(self):
        return(datetime.datetime.now())
        
class Server:
    def __init__(self):
        self.logs={}
        self.rate=10
    def addEntry(self,registrationNumber,time):
        self.logs[regitrationNumber]+=[time]
    def removeEntry(self,registrationNumber):
        del self.logs[regitrationNumber]
    def getBill(self,registrationNumber):
        bill= (self.logs[registrationNumber][1]- self.logs[regitrationNumber][0])*rate
        self.removeEntry(registrationNumber)
        return(bill)
        
class SpotType:
    SMALL=1
    MEDIUM=2
    LARGE=3

class CarType:
    SMALL=1
    MEDIUM=2
    LARGE=3
    
class EmployeeType(enum.Enum):
    ENTRYGUARD=1
    EXITGUARD=2
