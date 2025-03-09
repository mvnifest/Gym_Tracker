from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# Функция для извлечения тренировок из базы данных по выбранному дню
def get_workouts(day):
    conn = sqlite3.connect('gym_tracker.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM workouts WHERE day = ?", (day,))
    workouts = cursor.fetchall()
    conn.close()
    return workouts

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/day/<day>')
def day(day):
    workouts = get_workouts(day)
    return render_template('day.html', day=day, workouts=workouts)

if __name__ == '__main__':
    app.run(debug=True)