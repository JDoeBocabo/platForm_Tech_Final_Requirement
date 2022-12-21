# ask the user to enter the number of processes
num_processes = int(input("Enter the number of processes: "))

# create an empty list to store the processes
processes = []

# ask the user to enter the details of each process
for i in range(num_processes):
    print(f"Enter the details of process {i + 1}:")
    arrival_time = int(input("Arrival time: "))
    burst_time = int(input("Burst time: "))
    priority = int(input("Priority: "))
    processes.append([arrival_time, burst_time, priority])

# sort the processes by arrival time
processes.sort(key=lambda x: x[0])

# define the variables to store the results
waiting_times = []
turn_around_times = []

# initialize the current time
current_time = 0

# iterate through the processes
for i, p in enumerate(processes):
    arrival_time, burst_time, priority = p

    # calculate the waiting time
    waiting_time = current_time - arrival_time
    waiting_times.append(waiting_time)

    # update the current time
    current_time += burst_time

    # calculate the turn around time
    turn_around_time = burst_time + waiting_time
    turn_around_times.append(turn_around_time)

# calculate the average waiting time and turn around time
average_waiting_time = sum(waiting_times) / len(waiting_times)
average_turn_around_time = sum(turn_around_times) / len(turn_around_times)

# print the results in a table form
print("Process  \tArrival Time\tBurst Time\tPriority\tWaiting Time\tTurn Around Time")
for i, p in enumerate(processes):
    arrival_time, burst_time, priority = p
    waiting_time = waiting_times[i]
    turn_around_time = turn_around_times[i]
    print(f"{i + 1}   \t\t\t{arrival_time} \t\t\t\t  {burst_time}   \t\t{priority}   \t\t{waiting_time}   \t\t\t\t{turn_around_time}")

# print the average waiting time and turn around time
print(f"Average waiting time: {average_waiting_time}")
print(f"Average turn around time: {average_turn_around_time}")
