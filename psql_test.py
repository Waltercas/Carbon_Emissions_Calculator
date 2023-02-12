from sqlalchemy import create_engine
import utils
import psycopg2
person = utils.Individual()


conn = psycopg2.connect(user="postgres",
                        password="postgres",
                        host="localhost",
                        port="2022",
                        database="CarbonTest")

cursor = conn.cursor()


def create_table():
    cursor.execute("""CREATE TABLE test(id serial PRIMARY KEY, name varchar, emissions float, diet_emissions float,
     long_flights float, medium_flights float, short_flights float, hotel_emissions float, rail_emissions float,
      bus_emissions float, car_emissions float, transportation_total float);""")


def insert_query(name, emissions, diet, long, medium, short, hotel, rail, bus, car, transportation):
    cursor.execute("""INSERT INTO test (name, emissions,diet_emissions, long_flights, medium_flights,
     short_flights, hotel_emissions, rail_emissions, bus_emissions, car_emissions, transportation)total ) VALUES (%s,%s)""",
                (name, emissions, diet, long, medium, short, hotel, rail, bus, car, transportation))

conn.commit()


