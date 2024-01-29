#1 For Loop Festival Planner:
days = ["Day 1", "Day 2", "Day 3"]
events = ["Concert", "Workshop", "Exhibition"]

for day in days:
    for event in events:
        print(f"{day}: {event}")

#2 Classroom Seat Assignment:
students = ["Alice", "Bob", "Charlie", "David"]
seats = range(1, len(students) + 1)

for student, seat in zip(students, seats):
    print(f"Seat {seat}: {student}")

#3 Shopping Cart Total Calculator:
items = {"item1": 20, "item2": 30, "item3": 15}
total_cost = 0

for item, cost in items.items():
    total_cost += cost

print(f"Total Cost: ${total_cost}")

#4 Multiplication Table Generator:
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i} * {j} = {i * j}"
        
#5 Inventory Management:
inventory = {"item1": 10, "item2": 5, "item3": 8}

for item, quantity in inventory.items():
    if quantity < 5:
        print(f"Low stock for {item}")

#6 Treasure Hunt:
treasure_location = (5, 7)
searched_locations = [(3, 4), (5, 7), (2, 9), (8, 1)]

for location in searched_locations:
    if location == treasure_location:
        print("Treasure found!")
        break

#7 Email Cleanup:
emails = ["john@example.com", "spam@example.com", "alice@example.com"]

for email in emails:
    if "spam" in email:
        continue
    print(f"Cleaned email: {email}")

