class Vehicle:
    def __init__(self, brand, model, year, rental_price_per_day):
        self.brand = brand  
        self.model = model  
        self.year = year  
        self.__rental_price_per_day = rental_price_per_day  # Private attribute

    def display_info(self):
        print(f"{self.brand} {self.model}, Year: {self.year}, Rental Price: ${self.__rental_price_per_day}/day")

    def calculate_rental_cost(self, days):
        return self.__rental_price_per_day * days
    
    def get_rental_price_per_day(self):
        return self.__rental_price_per_day
    
    def set_rental_price_per_day(self, new_price):
        if new_price > 0:
            self.__rental_price_per_day = new_price
        else:
            print("Rental price must be positive.")

class Car(Vehicle):
    def __init__(self, brand, model, year, rental_price_per_day, seating_capacity):
        super().__init__(brand, model, year, rental_price_per_day)
        self.seating_capacity = seating_capacity

    def display_info(self):
        print(f"\nCar: {self.brand} {self.model}, Year: {self.year}, Seats: {self.seating_capacity}, Rental Price: ${self.get_rental_price_per_day()}/day")

class Bike(Vehicle):
    def __init__(self, brand, model, year, rental_price_per_day, engine_capacity):
        super().__init__(brand, model, year, rental_price_per_day)
        self.engine_capacity = engine_capacity 
    
    def display_info(self):
        print(f"\nBike: {self.brand} {self.model}, Year: {self.year}, Engine: {self.engine_capacity}cc, Rental Price: ${self.get_rental_price_per_day()}/day")

def show_vehicle_info(vehicle):
    vehicle.display_info()

print("\n==== Welcome to Mayta Vehicles ====")
print(" \t**Menu** ")
print(" 1 : Rent a Car ")
print(" 2 : Rent a Bike ")
print(" 3 : EXIT ")

option=int(input("Enter your option :"))

while option!=3:

    if option==1:
        carBrand=input("Enter car brand: ")
        carModel=input("Enter car model: ")
        carYear=int(input("Enter car year: "))
        carPrice=float(input("Enter car rental price per day: "))
        carSeats=int(input("Enter car seating capacity: "))

        car = Car(carBrand, carModel, carYear, carPrice, carSeats)

        show_vehicle_info(car)

        carDays=int(input("Enter number of days to rent the car: "))

