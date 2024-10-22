#Riddle Range
import random

mood = ["happy", "sad", "angry", "excited"]
week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

for i in range(len(week)):
    print(f"On " + week[i] + " you were feeling " + (random.choice(mood)))