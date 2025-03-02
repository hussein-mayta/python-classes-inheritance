class Vehicle:
    def __init__(self, brand, model, year, rental_price_per_day):
        self.brand = brand  
        self.model = model  
        self.year = year  
        self.__rental_price_per_day = rental_price_per_day  # Private attribute

    def display_info(self):
        print(f"{self.brand} {self.model}, Year: {self.year}, Rental Price: ${self.__rental_price_per_day}/day")
