try:
    results = {
        "Ankit": 80,
        "Jatin": 90,
        "Rahul": 70,
        "Amit": 60,
        "Alice": 50,
    }

    name = input("Enter the student's name: ")
    print(f"{name}'s marks: {results[name]}")
except:
    print("Student not found.")

