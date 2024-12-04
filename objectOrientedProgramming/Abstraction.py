

from abc import ABC,abstractmethod

class Bike(ABC):
    
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def accelarate(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Hunter(Bike):

    def start(self):

        print("hunter start method")

    def accelarate(self):
        print("hunter accelarate method")

    def stop(self):
        print("hunte stop method")

hunder_instance=Hunter()
hunder_instance.start()
hunder_instance.accelarate()
hunder_instance.stop()
    
    