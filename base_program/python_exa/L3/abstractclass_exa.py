from abc import ABC, abstractmethod

class Vechile_abc(ABC):
    @abstractmethod
    def move(self):
        pass

    def stop(self):
        pass

class Car(Vechile_abc):
    def move(self):
        print("Car move")
    
    # def stop(self):
    #     print("Car stop")

class Plane(Vechile_abc):
    def move(self):
        print("Plane move")
    
    def stop(self):
        print("Plane stop")

class Ship(Vechile_abc):
    def move(self):
        print("Ship move")
    
    def stop(self):
        print("Ship stop")

class VechileFactory:   
    def create(self, vechile_type):
        if vechile_type == "car":
            return Car()
        elif vechile_type == "plane":
            return Plane()
        elif vechile_type == "ship":
            return Ship()
        else:
            raise Exception("Unknown vechile type")

if __name__ == "__main__":
    vechile_factory = VechileFactory()
    vechile = vechile_factory.create("car")
    vechile.move()
    vechile.stop()

    vechile = vechile_factory.create("plane")
    vechile.move()
    vechile.stop()

    vechile = vechile_factory.create("ship")
    vechile.move()
    vechile.stop()