import random
import csv
# 1wy8S2OI7GWtbV9ULP53HkdNYGhDI9b9sILN_ZtfyI2s
meals = [[],[]]
weekdays = ["Monday:", "Tuesday:", "Wednesday:", "Thursday:", "Friday:", "Saturday:", "Sunday:"]
chosen = set()
i = len(chosen)

with open('MealList.csv', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    for row in csvreader:
        meals[0].append(row[0])
        meals[1].append(int(row[1]))

while i < 7:
    a = random.choices(meals[0], weights = meals[1], k = 1)
    chosen.add(a[0])
    i = len(chosen)

chosenlist = list(chosen)

for day in weekdays:
    print(day, chosenlist[i-1])
    i -= 1