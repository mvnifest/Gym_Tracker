import sqlite3

# Открытие базы данных
conn = sqlite3.connect('gym_tracker.db')
cursor = conn.cursor()

# Обновляем данные для Day 1
cursor.execute("UPDATE workouts SET exercise = 'Barbell Bench Press' WHERE day = 'Day 1' AND exercise = 'жим лежа'")
cursor.execute("UPDATE workouts SET exercise = 'Pullover' WHERE day = 'Day 1' AND exercise = 'пуловер'")
cursor.execute("UPDATE workouts SET exercise = 'Barbell Incline Press' WHERE day = 'Day 1' AND exercise = 'жим штанги наклонной на трицепс'")
cursor.execute("UPDATE workouts SET exercise = 'Seated Tricep Extensions' WHERE day = 'Day 1' AND exercise = 'г образные сгибания сидя'")
cursor.execute("UPDATE workouts SET exercise = 'Dips' WHERE day = 'Day 1' AND exercise = 'брусья'")

# Обновляем данные для Day 2
cursor.execute("UPDATE workouts SET exercise = 'Weighted Pull-ups' WHERE day = 'Day 2' AND exercise = 'Подтянивания с весом'")
cursor.execute("UPDATE workouts SET exercise = 'Seated Cable Rows' WHERE day = 'Day 2' AND exercise = 'Стягивания блока сидя двумя руками'")
cursor.execute("UPDATE workouts SET exercise = 'Wide-grip Lat Pulldown' WHERE day = 'Day 2' AND exercise = 'Стягивание широкого блока сверху'")
cursor.execute("UPDATE workouts SET exercise = 'Dumbbell Rows' WHERE day = 'Day 2' AND exercise = 'на скамье гантеля'")
cursor.execute("UPDATE workouts SET exercise = 'Bicep Curls on Bench' WHERE day = 'Day 2' AND exercise = 'бицепс на скамье'")

# Обновляем данные для Day 3
cursor.execute("UPDATE workouts SET exercise = 'Incline Dumbbell Press' WHERE day = 'Day 3' AND exercise = 'жим гантелей на наклонной скамье'")
cursor.execute("UPDATE workouts SET exercise = 'Overhead Dumbbell Press' WHERE day = 'Day 3' AND exercise = 'Жим гантелей вверх на плечи'")
cursor.execute("UPDATE workouts SET exercise = 'Cable Chest Fly' WHERE day = 'Day 3' AND exercise = 'Свод блоков на грудь на станции'")
cursor.execute("UPDATE workouts SET exercise = 'Dumbbell Shrugs' WHERE day = 'Day 3' AND exercise = 'шраги на плечи'")
cursor.execute("UPDATE workouts SET exercise = 'Dumbbell Chest Fly' WHERE day = 'Day 3' AND exercise = 'Свод гантелей на плоской/упражнение сверху'")
cursor.execute("UPDATE workouts SET exercise = 'Dumbbell Lateral Raises' WHERE day = 'Day 3' AND exercise = 'Развод гантелей стоя'")

# Сохраняем изменения в базе данных
conn.commit()

# Закрываем соединение
conn.close()
