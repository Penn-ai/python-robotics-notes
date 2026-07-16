# # Simple Robot Task Manager

# target_points = ["A", "B", "C", "D"]
# battery = 45

# def move_to_point(point):
#     print(f"Robot is moving to point {point}.")

# def check_battery(battery_level):
#     if battery_level < 20:
#         return False
#     else:
#         return True

# for point in target_points:
#     if check_battery(battery):
#         move_to_point(point)
#         battery = battery - 10
#         print(f"Battery left: {battery}%")
#     else:
#         print("Battery low. Stop task.")
#         break
    

    
# Robot Task Manager - Version 2
# This program simulates a robot completing tasks at different target points.

robot_name = "TurtleBot3"

# Initial battery level
battery = 100

# Each target point has a different battery consumption
# 运用到新知识点：directionary 字典
tasks = {
    "A": 10,
    "B": 15,
    "C": 20,
    "D": 25
}


def check_battery(battery_level, required_battery):
    """
    Check whether the robot has enough battery for the next task.
    """
    if battery_level >= required_battery:
        return True
    else:
        return False


def move_to_point(point, battery_cost):
    """
    Simulate the robot moving to a target point.
    """
    print(f"{robot_name} is moving to point {point}.")
    print(f"This task will consume {battery_cost}% battery.")


print("Robot Task Manager Started")
print(f"Robot name: {robot_name}")
print(f"Initial battery: {battery}%")
print("------------------------------")

for point, battery_cost in tasks.items():  #task是一个字典
    print(f"Next target point: {point}")

    if check_battery(battery, battery_cost):
        move_to_point(point, battery_cost)
        battery = battery - battery_cost
        print(f"Task at point {point} completed.")
        print(f"Battery left: {battery}%")
    else:
        print(f"Battery is not enough for point {point}.")
        print("Robot stops the task.")
        break                #break指的立即结束当前for循环

    print("------------------------------")

print("Robot Task Manager Finished")
print(f"Final battery: {battery}%")