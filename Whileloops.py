#slide 30 in M2L4, While loops hands on.
#1. Countdown Timer:
import time

timer = 10  # seconds

while timer > 0:
    print(timer)
    timer -= 1
    print("Time's up!")

#2. Patient Queue:
patient_queue = ["John", "Jane", "Alice", "Bob"]

while patient_queue > 0:
    current_patient +=  1 patient_queue
    print(f"Now serving: {current_patient}")
    
#3. Battery Charger with Efficiency Check:
battery_level = 20  # initial battery level
efficiency_threshold = 90  # percentage

while battery_level < 100:
    print(f"Charging... Battery level: {battery_level}%")
    battery_level += 10

    if battery_level >= efficiency_threshold:
        print("Efficiency check passed. Battery fully charged!")
        break

#4. Smart Coffee Machine:
coffee_types = ["Espresso", "Latte", "Cappuccino"]
coffee_reservoir = 3  # number of coffees available

while coffee_reservoir > 0:
    print("Available coffee types:")
    for i, coffee in enumerate(coffee_types, start=1):
        print("{i}. {coffee}")

    choice = int(input("Choose your coffee (1-3): "))
    if 1 <= choice <= len(coffee_types):
        print("Dispensing {coffee_types[choice - 1]}...")
        coffee_reservoir -= 1
    else:
        print("Invalid choice. Try again.")

print("Coffee reservoir empty. Please refill.")

#5. Intelligent Elevator System:
floors = [1, 2, 3, 4, 5]
elevator_requests = [3, 1, 5, 2, 4]  # Example list of floor requests

while elevator_requests:
    current_floor = elevator_requests.pop(0)

    if current_floor in floors:
        print(f"Elevator stopping at Floor {current_floor}")
    else:
        print(f"Ignoring invalid request for Floor {current_floor}")

print("Elevator simulation completed.")

#6. Smart Traffic Light System:
traffic_light_states = ["Red", "Green", "Yellow"]
requests = ["Stop", "Go", "Stop", "Go", "Stop", "Go"]  # Example list of traffic light requests

while True:
    request_count = requests.count("Go")

    if request_count == 0:
        print("No requests to go. Exiting...")
        break

    print("Traffic light is green. All vehicles can go!")
    requests.remove("Go")

#7. Skipping Rope Challenge:

rope_length = 10
skip_count = 0

while rope_length > 0:
    print(f"Skipping... Rope length: {rope_length}")
    skip_count += 1

    if skip_count % 3 == 0:
        cut_length = int(input("Enter the length to cut: "))
        rope_length -= cut_length
    else:
        continue

print("Skipping rope challenge completed.")
