import pandas as pd
from sqlalchemy import create_engine

class Individual:

    def __init__(self):
        self.name = ""
        self.emissions = 0

    def name_individual(self, name):
        person = name
        return person

    def diet_emissions(self, choice):
        diet = choice
        if choice == 0:  # Meat lover
            diet_emissions_totals = 3.3
        elif choice == 1:  # average
            diet_emissions_totals = 2.5
        elif choice == 2:  # No beef
            diet_emissions_totals = 1.9
        elif choice == 3:  # Vegetarian
            diet_emissions_totals = 1.7
        elif choice == 4:  # Vegan
            diet_emissions_totals = 1.5
        return diet_emissions_totals

    def long_flight_emissions(self,short_distance_flights):
        short_flight_total= short_distance_flights * 0.0375
        return short_flight_total

    def medium_flight_emissions(self, medium_distance_flights):
        medium_flight_total = medium_distance_flights * 0.196
        return medium_flight_total

    def short_flight_emissions(self, short_distance_flights):
        short_flight_total = short_distance_flights * 0.0375
        return short_flight_total

    def hotel_emmissions(self, nights):
        hotel_emissions_totals = nights * 0.0383
        return hotel_emissions_totals

    def rail_emissions(self, rail):
        if rail == 0:
            rail_emissions_totals = 0
        elif rail == 1:
            rail_emissions_totals = 0.0007 * 52
        elif rail == 2:
            rail_emissions_totals = 0.0014 * 52
        elif rail == 3:
            rail_emissions_totals = 0.0021 * 52
        elif rail == 4:
            rail_emissions_totals = 0.0028 * 52
        elif rail == 5:
            rail_emissions_totals = 0.0042 * 52
        elif rail == 6:
            rail_emissions_totals = 0.0056 * 52
        return rail_emissions_totals

    def bus_emissions(self, bus):
        if bus == 0:
            bus_emissions_totals = 0
        elif bus == 1:
            bus_emissions_totals = 0.0006 * 52
        elif bus == 2:
            bus_emissions_totals = 0.0012 * 52
        elif bus == 3:
            bus_emissions_totals = 0.0018 * 52
        elif bus == 4:
            bus_emissions_totals = 0.0024 * 52
        elif bus == 5:
            bus_emissions_totals = 0.0036 * 52
        elif bus == 6:
            bus_emissions_totals = 0.0048 * 52
        return bus_emissions_totals

    def car_emissions(self, miles, mpg):
        car_emissions_total = (miles /mpg) * 0.0089
        return car_emissions_total





if __name__ == "__main__":
    choice = 1
    nameList = []
    emissionList = []
    dietList = []
    longFlightList = []
    mediumFlightList = []
    shortFlightList = []
    railEmissionsList = []
    carEmissionsList = []
    busEmissionsList = []
    transportationEmissionsList = []

    while choice != 0:
        d = Individual()
        d.name = d.name_individual(input("Enter name: "))
        diet = d.diet_emissions(
            float(input("Choose your diet: \n Meat Lover = 0 \n Average = 1 \n No Beef = 2 " +
                        "\n Vegetarian = 3 \n Vegan = 4\n")))
        d.emissions = diet
        dietList.append(diet)
        long_flights = d.long_flight_emissions(float(input("Enter number of long round-trip flight"
                                   "(2,300+ miles) you made this year\n")))
        medium_flights = d.medium_flight_emissions(float(input("Enter number of medium round-trip flight"
                                     "(300-2299 miles) you made this year\n")))
        short_flights = d.short_flight_emissions(float(input("Enter number of long round-trip flight"
                                    "(under 300 miles) you made this year\n")))
        longFlightList.append(long_flights)
        mediumFlightList.append(medium_flights)
        shortFlightList.append(short_flights)

        d.emissions += short_flights + medium_flights + long_flights
        nights_in_hotel = int(input("Enter how many nights you have spent in a hotel per year\n"))
        d.emissions += d.hotel_emmissions(nights_in_hotel)

        rail = d.rail_emissions(int(input("How many miles do you travel by train weekly: \n 0 miles = 0 \n 1-5 miles = 1 \n 6-10 miles = 2 " +
                        "\n 11-20 miles = 3 \n 20-30 miles = 4\n 30+ miles = 5\n")))
        bus = d.bus_emissions(int(input("How many miles do you travel by bus weekly: \n 0 miles = 0 \n 1-5 miles = 1 \n 6-10 miles = 2 " +
                         "\n 11-20 miles = 3 \n 20-30 miles = 4\n 30+ miles = 5\n")))
        miles = int(input("How many miles do you drive yearly on average. \n"))
        mpg = int(input("What is your vehicles average mpg \n"))
        car = d.car_emissions(miles, mpg)

        transportation_emissions_total = rail + bus + car
        railEmissionsList.append(rail)
        busEmissionsList.append(bus)
        carEmissionsList.append(car)
        transportationEmissionsList.append(transportation_emissions_total)


        d.emissions += transportation_emissions_total
        nameList.append(d.name)
        emissionList.append(d.emissions)

        choice = int(input("Enter 0 to end Enter 1 to add another person \n"))
        if choice == 0:
            df = pd.DataFrame({"Names": nameList, "Emissions": emissionList, "Long FLights":longFlightList,
                               "Medium Flights": mediumFlightList, "Short Flights": shortFlightList,
                               "Rail": railEmissionsList, "Bus": busEmissionsList, "Car": carEmissionsList,
                               "Transportation Total": transportationEmissionsList})
            print(df)


