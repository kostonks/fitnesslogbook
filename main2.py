from prettytable import PrettyTable
from datetime import datetime

# Exercise Class 
class Exercise:
    def __init__(self, name, intensity, weight, reps=None, date=None):
        self.name = name
        self.intensity = intensity
        self.weight = weight
        self.reps = reps
        self.date = date or datetime.now().strftime("%Y/%m/%d")

# User Class
class User:
    def __init__(self, username):
        self.username = username
        self.exercises = []

    def log_exercise(self, exercise):
        self.exercises.append(exercise)

    def print_exercises(self):
        table = PrettyTable()
        table.field_names = ["Date", "Exercise", "Intensity", "Weight", "Reps"]
        for exercise in self.exercises:
            table.add_row([exercise.date, exercise.name, exercise.intensity, exercise.weight, exercise.reps or "N/A"])
        print(table)

    def print_exercises_by_date(self, date):
        table = PrettyTable()
        table.field_names = ["Date", "Exercise", "Intensity", "Weight", "Reps"]
        for exercise in self.exercises:
            if exercise.date == date:
                table.add_row([exercise.date, exercise.name, exercise.intensity, exercise.weight, exercise.reps or "N/A"])
        if table.get_string():
            print(table)
        else:
            print("No exercises logged for this date.")

# Function to log exercise 
def log_exercise(user):
    name = input("Enter exercise name: ")
    intensity = int(input("Enter intensity RPE(1-10): "))
    weight = input("Enter weight used (lbs or kg): ")
    reps = input("Enter repetitions: ")
    date = input("Enter date (YYYY/MM/DD): ")
    reps = int(reps) if reps.isdigit() else None
    exercise = Exercise(name, intensity, weight, reps, date)
    user.log_exercise(exercise)
    print("Exercise logged successfully")

# Main function for user 
def main():
    username = input("Enter your username: ")
    user = User(username)

    while True:
        print("\n--- Fitness Tracking ---")
        print("1. Log Exercise")
        print("2. Show All Exercises")
        print("3. Show Exercises by Date")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")
        if choice == "1":
            log_exercise(user)
        elif choice == "2":
            user.print_exercises()
        elif choice == "3":
            date = input("Enter date to search (YYYY/MM/DD): ")
            user.print_exercises_by_date(date)
        elif choice == "4":
            print("Exiting")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
