class Vehicle:
    def __init__(self,name,with_engine):
        self.name = name
        self.__with_engine = with_engine
    
    types = "parent of All Vehicle"
    private = ''
    def identify_myself(self):
        return f"Hi I'm {self.types}{self.private}, My Name is {self.name}, My Engine Status is '{self.__with_engine}' "
    
class Bikes(Vehicle):
    def __init__(self,name,with_engine,wheel_count):
        super().__init__(name,with_engine)
        self.wheel_count = wheel_count
    
    types = 'Bike'
    private = ''
    def identify_myself(self):
        return super().identify_myself() + f'I have {self.wheel_count} Wheel(s)' 

class Cars(Vehicle):
    def __init__(self,name,with_engine,wheel_count,engine_type):
        super().__init__(name,with_engine)
        self.wheel_count = wheel_count
        self.__engine_type = engine_type

    types = 'Car'
    private = ''

    def identify_myself(self):
        return super().identify_myself() + f'I have {self.wheel_count} Wheel(s), My Engine Type {self.__engine_type}'


class Buses(Vehicle):
    def __init__(self,name,with_engine,wheel_count,private_bus):
        super().__init__(name,with_engine)
        self.wheel_count = wheel_count
        self.private = " ["+private_bus+"] "

    types = 'Bus'
    def identify_myself(self):
        return super().identify_myself() + f'I have {self.wheel_count} Wheel(s)'

pedal_bikes = Bikes('Pedal Bikes','no engine',2)
gerobak = Vehicle('Gerobak','no engine')
sports_cars = Cars('Sports Cars','with engine',4,'V8')
public_bus = Buses('Trans jakarta','with engine',4,'Public Bus')

print(gerobak.identify_myself())
print(pedal_bikes.identify_myself())
print(sports_cars.identify_myself())
print(public_bus.identify_myself())