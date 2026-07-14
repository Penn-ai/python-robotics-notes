# Simple Robot Task Manager

target_points = ["A", "B", "C", "D"]
battery = 45

def move_to_point(point):
    print(f"Robot is moving to point {point}.")

def check_battery(battery_level):
    if battery_level < 20:
        return False
    else:
        return True

for point in target_points:
    if check_battery(battery):
        move_to_point(point)
        battery = battery - 10
        print(f"Battery left: {battery}%")
    else:
        print("Battery low. Stop task.")
        break