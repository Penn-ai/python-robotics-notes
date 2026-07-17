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

# robot_name = "TurtleBot3"

# # Initial battery level
# battery = 100

# # Each target point has a different battery consumption
# # 运用到新知识点：dictionary 字典
# tasks = {
#     "A": 10,
#     "B": 15,
#     "C": 20,
#     "D": 25
# }


# def check_battery(battery_level, required_battery):
#     """
#     Check whether the robot has enough battery for the next task.
#     """
#     if battery_level >= required_battery:
#         return True
#     else:
#         return False


# def move_to_point(point, battery_cost):
#     """
#     Simulate the robot moving to a target point.
#     """
#     print(f"{robot_name} is moving to point {point}.")
#     print(f"This task will consume {battery_cost}% battery.")


# print("Robot Task Manager Started")
# print(f"Robot name: {robot_name}")
# print(f"Initial battery: {battery}%")
# print("------------------------------")

# for point, battery_cost in tasks.items():  #task是一个字典
#     print(f"Next target point: {point}")

#     if check_battery(battery, battery_cost):
#         move_to_point(point, battery_cost)
#         battery = battery - battery_cost
#         print(f"Task at point {point} completed.")
#         print(f"Battery left: {battery}%")
#     else:
#         print(f"Battery is not enough for point {point}.")
#         print("Robot stops the task.")
#         break                #break指的立即结束当前for循环

#     print("------------------------------")

# print("Robot Task Manager Finished")
# print(f"Final battery: {battery}%")

# #整体任务逻辑
# 机器人状态：电量
# 任务数据：目标点与耗电量
# 判断条件:电量是否足够
# 执行动作：移动到目标点
# 状态更新：扣除电量
# 停止条件：电量不足
# 过程输出：打印任务日志

# Robot Task Manager - Version 3
# This program simulates a robot completing tasks and calculates task statistics.

robot_name = "TurtleBot3"

# Initial battery level
battery = 60

# Each target point has a different battery consumption
tasks = {
    "A": 10,
    "B": 15,
    "C": 20,
    "D": 25
}

# Task statistics
total_tasks = len(tasks)
completed_tasks = 0


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
print(f"Total tasks: {total_tasks}")
print("------------------------------")

for point, battery_cost in tasks.items():
    print(f"Next target point: {point}")

    if check_battery(battery, battery_cost):
        move_to_point(point, battery_cost)

        battery = battery - battery_cost
        completed_tasks = completed_tasks + 1       # 执行一个后，此变量+1

        print(f"Task at point {point} completed.")
        print(f"Battery left: {battery}%")
    else:
        print(f"Battery is not enough for point {point}.")
        print("Robot stops the task.")
        break

    print("------------------------------")

# Calculate final statistics
unfinished_tasks = total_tasks - completed_tasks
completion_rate = completed_tasks / total_tasks * 100

print("------------------------------")
print("Task Summary")
print(f"Total tasks: {total_tasks}")
print(f"Completed tasks: {completed_tasks}")
print(f"Unfinished tasks: {unfinished_tasks}")
print(f"Final battery: {battery}%")
print(f"Task completion rate: {completion_rate}%")
print("Robot Task Manager Finished")

#数据统计逻辑： 执行任务——记录状态——输出统计结果