import sqlite3
conn = sqlite3.connect('gym_tracker.db')
cursor = conn.cursor()
cursor.execute("PRAGMA table_info(workouts);")
print(cursor.fetchall())