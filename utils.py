
class Individual:

    def __init__(self):
        self.name = ""
        self.emissions = 0

    def name_individual(self, name):
        person = name
        return person

    def diet_emissions(self, choice):
        diet = choice
        if diet == 0:  # Meat lover
            diet_emissions_totals = 3.3
        elif diet == 1:  # average
            diet_emissions_totals = 2.5
        elif diet == 2:  # No beef
            diet_emissions_totals = 1.9
        elif diet == 3:  # Vegetarian
            diet_emissions_totals = 1.7
        elif diet == 4:  # Vegan
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





#if __name__ == "__main__":
