#Dice roll
import random
for _ in range (10):
    dice_roll = random.randint (1,6)
    print ("you rolled a" + str (dice_roll) + "!")

#Playlist random song
import random 
playlist = ['song1', 'song2', 'song3', 'song4', 'song5']
random.shuffle(playlist) 

for song in playlist:
    print (song)

#Random snacks
import random
sancks = ['apple', 'banana', 'carrot stick', 'doughnut', 'chocolate bar']
picked_snack = ''

while picked_snack != 'chocolate bar':
    picked_snack = random.choice(snacks)
    print ("you got a" + picked_snack + ".")
    if picked_snack != 'chocolate bar': 
        print(" let's pick again!")
    else:
        print("yay! chocolate bar wins!")

#Lucky Draw Simulation:
import random

participants = ["Alice", "Bob", "Charlie", "David", "Eve"]
winner = random.choice(participants)

print(f"The lucky winner is: {winner}")

#Random Walk Simulation:
position = 0

for _ in range(10):
    step = random.choice([-1, 1])
    position += step

print(f"Final position after random walk: {position}")

#Dice Roll Synchronicity:
dice_rolls = []

for _ in range(5):
    dice_rolls.append(random.randint(1, 6))

print(f"Dice rolls: {dice_rolls}")

#Quiz Master Shuffle:
questions = ["Q1", "Q2", "Q3", "Q4", "Q5"]
random.shuffle(questions)

for index, question in enumerate(questions, start=1):
    print(f"Question {index}: {question}")

#Classroom Roll Call:
students = ["Alice", "Bob", "Charlie", "David", "Eve"]
random_sample = random.sample(students, k=2)

print(f"Randomly selected students: {random_sample}")

#Secure Password Creation:
import string

length = 8
password = ''.join(random.choices(string.ascii_letters + string.digits, k=length))

print(f"Generated password: {password}")

#Dynamic Color Generation:
def generate_random_color():
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))

print(f"Random color: {generate_random_color()}")
