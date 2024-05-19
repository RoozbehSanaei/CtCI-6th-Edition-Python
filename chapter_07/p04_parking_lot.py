import unittest
from random import randrange

import pytest


'''
    Setting Up the Vehicle System:
        Create a basic structure for vehicles called the Vehicle class. 
        This class represents general characteristics of a vehicle, including its model, size, and a unique number. 
        Additionally, it keeps track of whether a vehicle is parked or not.

    Initializing Vehicles:
        When a new vehicle is created, its model, size, and unique number are defined. 
        Initially, the vehicle is marked as not parked.

    Checking Vehicle's Parking Status:
        Include a method in the Vehicle class to check if the vehicle is parked. 
        This method prints and returns the parking status of the vehicle.

    Creating Specific Types of Vehicles:
        Define subclasses for different types of vehicles like Bike, Scooter, Car, and Bus.
        These classes inherit properties and behaviors from the Vehicle class but are used to represent specific vehicle types.

    Designing the Parking Zone:
        Develop a ParkZone class to manage a parking area. The parking zone starts with a predefined amount of space available for parking vehicles.

    Parking a Vehicle:
        Implement a method to park a vehicle. This method checks if there is enough space in the parking zone for the vehicle based on its size.
        If there is sufficient space, the vehicle is registered in the parking zone, its parked status is updated to True,
        the available space in the parking zone is reduced accordingly, and a parking token is generated and returned.
        If there isn't enough space, the method indicates that no space is available.

    Checking for Available Space:
        Include a method in the ParkZone class to check if there is enough space to accommodate a vehicle of a certain size.

    Registering the Vehicle:
        Add a method to register a vehicle in the park zone. 
        This method generates a unique token for the vehicle and ensures no duplicate tokens are issued.

    Generating Parking Token:
        Create a method to generate a random token used for parking vehicles. 
        This token is used to identify the vehicle when it needs to be deparked.

    Deparking a Vehicle:
        Implement a method to remove a vehicle from the park zone using its parking token. 
        This method checks if the provided token is valid and corresponds to a parked vehicle.
        If the token is valid, the vehicle is removed from the parking list, its parked status is set to False, and the available space in the parking zone is increased accordingly.
        If the token is invalid, the method raises an error.

    Listing Parked Vehicles:
        Add a method to list all vehicles currently parked in the park zone. 
        This method displays details like the model, size, and number of each parked vehicle.

'''


class Vehicle:
    types = []

    def __init__(self, model, size, number):
        self.model = model
        self.size = size
        self.number = number
        self.parked = False

    def is_parked(self):
        if self.parked:
            print("Vehicle is parked")
            return True

        print("Vehicle is not parked")
        return False


class Bike(Vehicle):
    pass


class Scooter(Vehicle):
    pass


class Car(Vehicle):
    pass


class Bus(Vehicle):
    pass


class ParkZone:
    def __init__(self):
        self.space_available = 10
        self.parked = {}

    def park(self, vehicle):
        if self.is_space_available(vehicle.size):
            token = self.register(vehicle)
            self.space_available -= vehicle.size
            vehicle.parked = True
            print(vehicle.model, " has been parked.")
            print("Token: ", token, ", Space available ", self.space_available)
            return token
        print("No space available")
        return None

    def is_space_available(self, size):
        return (self.space_available - size) >= 0

    def register(self, vehicle):
        token = self.generate_token()
        while token in self.parked:
            token = self.generate_token()
        self.parked[token] = vehicle
        return token

    def generate_token(self):
        return randrange(1111, 9999)

    def depark(self, token):
        if token in self.parked:
            parked_vehicle = self.parked[token]
            parked_vehicle.parked = False
            self.space_available += parked_vehicle.size
            print(parked_vehicle.model, "has been deparked")
            print("Space Available: ", self.space_available)
            return self.parked.pop(token)
        raise ValueError("Invalid token or vehicle not found")

    def list_parked_vehicles(self):
        print("------Parked Vehicles------")
        for vehicle in self.parked.values():
            print(vehicle.model, vehicle.size, vehicle.number)


def test_parking_lot():
    bike = Bike("Suzuki Access", 1, "MH14AB1234")
    assert not bike.is_parked()
    park_zone = ParkZone()
    token = park_zone.park(bike)
    assert bike.is_parked()
    assert park_zone.depark(token) == bike
    assert not bike.is_parked()

    car = Car("Honda Jazz", 5, "MU268A")
    assert not car.is_parked()
    car_token = park_zone.park(car)
    assert car.is_parked()
    with pytest.raises(ValueError, match="Invalid token or vehicle not found"):
        park_zone.depark(token)

    assert park_zone.depark(car_token) == car
    assert not car.is_parked()

    bus = Bus("Volvo", 5, "AN657")
    park_zone.park(bus)

    scooter = Scooter("Honda Activa", 1, "GI653")
    park_zone.park(scooter)
    park_zone.list_parked_vehicles()


if __name__ == "__main__":
    unittest.main()
