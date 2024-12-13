import csv

location_ids_1 = []
location_ids_2 = []

with open("day01_part1_data.txt") as csvfile:
    reader = csv.reader(csvfile, delimiter=" ")
    for row in reader:
        location_ids_1.append(int(row[0]))
        location_ids_2.append(int(row[3]))

location_ids_1.sort()
location_ids_2.sort()

distance_between_ids = []

for i in range(len(location_ids_1)):
    id1 = location_ids_1[i]
    id2 = location_ids_2[i]
    distance: int = id1 - id2
    distance_between_ids.append(abs(distance))


print(sum(distance_between_ids))
