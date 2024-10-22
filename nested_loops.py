#Nested Loops
import random

mood = ["happy", "sad", "angry", "excited"]
week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
time = ["morning", "afternoon", "evening",]

for w in range(len(week)):
    for t in range(len(time)):
        print(f"On " + week[w] +" "+ time[t] + " you were feeling " + (random.choice(mood)))