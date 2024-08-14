from pymongo import MongoClient

# Connect to MongoDB client on your local machine
client = MongoClient('mongodb://localhost:27017/')

# Access the database
db = client['attendance_system']

# Access the collection (similar to a table in relational databases)
students_collection = db['students']

# Data to be inserted
data = {
    "125": {
        "name": "Titus",
        "major": "Robotics",
        "starting_year": 2017,
        "total_attendance": 7,
        "standing": "G",
        "year": 4,
        "last_attendance_time": "2022-12-11 00:54:34"
    },
    "127": {
        "name": "Justin",
        "major": "Economics",
        "starting_year": 2021,
        "total_attendance": 12,
        "standing": "B",
        "year": 1,
        "last_attendance_time": "2022-12-11 00:54:34"
    },
    "128": {
        "name": "Sanoop",
        "major": "Physics",
        "starting_year": 2020,
        "total_attendance": 7,
        "standing": "G",
        "year": 2,
        "last_attendance_time": "2022-12-11 00:54:34"
    }
}

# Insert data into MongoDB
for key, value in data.items():
    students_collection.update_one({'_id': key}, {'$set': value}, upsert=True)
