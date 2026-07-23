import sqlite3

connection = sqlite3.connect("aircraft.db")


cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS aircraft (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        image1 TEXT,
        image2 TEXT,
        country TEXT NOT NULL,
        country_code TEXT,
        flag TEXT,
        category TEXT,
        type TEXT,
        status TEXT,
        first_flight INTEGER,
        max_speed_kmh INTEGER,
        range_km INTEGER,
        service_ceiling_ft INTEGER,
        length_m REAL,
        wingspan_m REAL,
        height_m REAL,
        empty_weight_kg INTEGER,
        max_takeoff_weight_kg INTEGER


);
""")

connection.commit()
connection.close()

# print("Database created successfully!")