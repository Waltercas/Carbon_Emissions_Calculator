import pandas as pd
import numpy as np


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

    def flight_emissions(self, long_distance_flights, medium_distance_flights, short_distance_flights):
        flight_emissions_totals = long_distance_flights * 0.51
        flight_emissions_totals += medium_distance_flights * 0.196
        flight_emissions_totals += short_distance_flights * 0.0375
        return flight_emissions_totals

    def hotel_emmissions(self, nights):
        hotel_emissions_totals = nights * 0.0383
        return hotel_emissions_totals

    def transportation_emissions(self, rail, bus, car, bike_walk):

        if rail == 0:
            rail_emissions_totals = 0
        elif rail == 1:
            rail_emissions_totals = 0.0007
        elif rail == 2:
            rail_emissions_totals = 0.0014
        elif rail == 3:
            rail_emissions_totals = 0.0021
        elif rail == 4:
            rail_emissions_totals = 0.0028
        elif rail == 5:
            rail_emissions_totals = 0.0042
        elif rail == 6:
            rail_emissions_totals = 0.0056

        if bus == 0:
            bus_emissions_totals = 0
        elif bus == 1:
            bus_emissions_totals = 0.0006
        elif bus == 2:
            bus_emissions_totals = 0.0012
        elif bus == 3:
            bus_emissions_totals = 0.0018
        elif bus == 4:
            bus_emissions_totals = 0.0024
        elif bus == 5:
            bus_emissions_totals = 0.0036
        elif bus == 6:
            bus_emissions_totals = 0.0048


if __name__ == "__main__":
    choice = 1
    nameList = []
    emissionList = []

    while choice != 0:
        d = Individual()
        d.name = d.name_individual(input("Enter name:"))
        d.emissions = d.diet_emissions(
            float(input("Choose your diet: \n Meat Lover = 0 \n Average = 1 \n No Beef = 2 " +
                        "\n Vegetarian = 3 \n Vegan = 4\n")))
        long_flights = float(input("Enter number of long round-trip flight"
                                   "(2,300+ miles) you made this year"))
        medium_flights = float(input("Enter number of medium round-trip flight"
                                     "(300-2299 miles) you made this year"))
        short_flights = float(input("Enter number of long round-trip flight"
                                    "(under 300 miles) you made this year"))
        d.emissions += d.flight_emissions(long_flights, medium_flights, short_flights)
        nights_in_hotel = int(input("Enter how many nights you have spent in a hotel per year"))
        d.emissions += d.hotel_emmissions(nights_in_hotel)
        nameList.append(d.name)
        emissionList.append(d.emissions)
        choice = int(input("Enter 0 to end Enter 1 to add another person"))
        if choice == 0:
            df = pd.DataFrame({"Names": nameList, "Emissions": emissionList})
            print(df)
