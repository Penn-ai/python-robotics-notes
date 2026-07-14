# Day 5: If statements and for loops

battery = 50
target_points = ["A", "B", "C"]

if battery < 20:
    print("Battery low. Go charging.")
else:
    for point in target_points:
        print(f"Robot is moving to point {point}.")