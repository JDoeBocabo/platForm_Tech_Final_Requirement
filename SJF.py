# get the number of processes from the user
num_processes = int(input("Enter the number of processes: "))

# define the lists for storing the burst time, arrival time, waiting time, turn around time, and completion time
burst_time = []
arrival_time = []
waiting_time = [0] * num_processes
turn_around_time = [0] * num_processes
completion_time = [0] * num_processes

# get the burst time and arrival time for each process from the user
for i in range(num_processes):
    bt = int(input(f"Enter the burst time for process {i}: "))
    at = int(input(f"Enter the arrival time for process {i}: "))
    burst_time.append(bt)
    arrival_time.append(at)

# sort the processes by their burst time
processes = sorted(zip(burst_time, arrival_time, range(num_processes)))

# initialize the current time to 0
current_time = 0

# initialize the sum of waiting time and turn around time to 0
waiting_time_sum = 0
turn_around_time_sum = 0

# calculate the waiting time and turn around time for each process
for i in range(num_processes):
    # get the burst time and arrival time of the current process
    bt, at, _ = processes[i]

    # calculate the completion time of the current process
    completion_time[i] = current_time + bt

    # calculate the waiting time of the current process
    waiting_time[i] = current_time - at

    # calculate the turn around time of the current process
    turn_around_time[i] = waiting_time[i] + bt

    # update the sum of waiting time and turn around time
    waiting_time_sum += waiting_time[i]
    turn_around_time_sum += turn_around_time[i]

    # update the current time
    current_time += bt

# calculate the average waiting time and average turn around time
average_waiting_time = waiting_time_sum / num_processes
average_turn_around_time = turn_around_time_sum / num_processes

# print the results in a table form
print("Process |\tBurst Time |\tArrival Time |\tCompletion Time |\tWaiting Time |\tTurn Around Time")
for i in range(num_processes):
    print(f"{i}\t\t\t\t{burst_time[i]}\t\t\t\t{arrival_time[i]}\t\t\t\t\t{completion_time[i]}\t\t\t\t{waiting_time[i]}\t\t\t\t{turn_around_time[i]}")

# print the average waiting time and average turn around time
print(f"Average Waiting Time: {average_waiting_time:.2f}")
print(f"Average Turn Around Time: {average_turn_around_time:.2f}")
