import utils
import psycopg2
from flask import Flask, request, render_template, redirect, url_for
person = utils.Individual()

app = Flask(__name__, template_folder="templates")
formData={}

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/index2")
def index2():
    return render_template('index2.html')
@app.route("/", methods=['POST','GET'])
def test_flsk():
    if request.method == 'POST':
        name = request.form["name"]
        diet = request.form["diet"]
        lflight = request.form["lflights"]
        mflight = request.form["mflights"]
        sflight = request.form["sflights"]
        hotel = request.form["hnights"]
        train = request.form["train"]
        bus = request.form["bus"]
        miles = request.form["miles"]
        mpg = request.form["mpg"]


        n = name
        d = person.diet_emissions(float(diet))

        l = person.long_flight_emissions(float(lflight))
        m = person.medium_flight_emissions(float(mflight))
        s = person.short_flight_emissions(float(sflight))
        h = person.hotel_emmissions(float(hotel))
        r = person.rail_emissions(float(train))
        b = person.bus_emissions(float(bus))
        c = person.car_emissions(float(miles),float(mpg))
        t = c + b + r
        e = d + l + m + s +h + r + b + c

        insert_query(n, e, d, l, m, s, h, r, b, c,t )

        return render_template("index2.html")
#<input type="submit" value="Submit">
    else:
        print(123)
        return render_template("index2.html")


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
    cursor.execute("INSERT INTO test (name, emissions,diet_emissions, long_flights, medium_flights, short_flights, hotel_emissions, rail_emissions, bus_emissions, car_emissions, transportation_total ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                (name, emissions, diet, long, medium, short, hotel, rail, bus, car, transportation,))

    conn.commit()


if __name__ == '__main__':
    app.run(debug=True)

