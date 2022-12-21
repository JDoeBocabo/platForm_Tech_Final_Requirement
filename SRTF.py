# Get the number of processes from the user
num_processes = int(input("Enter the number of processes: "))

# Initialize the list to store the process information
processes = []

# Get the arrival times and burst times for each process from the user
for i in range(num_processes):
    arrival_time = int(input(f"Enter the arrival time for process {i+1}: "))
    burst_time = int(input(f"Enter the burst time for process {i+1}: "))
    processes.append([arrival_time, burst_time])

# Sort the process list in ascending order of arrival time
processes.sort(key=lambda x: x[0])

# Initialize the variables to store the waiting time and turn around time for each process
waiting_times = []
turn_around_times = []

# Set the initial time to the arrival time of the first process
time = processes[0][0]

# Iterate through the processes
for i, process in enumerate(processes):
    # Calculate the waiting time for the current process
    waiting_time = time - process[0]
    waiting_times.append(waiting_time)
    # Calculate the turn around time for the current process
    turn_around_time = waiting_time + process[1]
    turn_around_times.append(turn_around_time)
    # Set the time to the completion time of the current process
    time = turn_around_time

# Print the table with the process information, waiting time, and turn around time
print("Process |\tArrival Time |\tBurst Time |\tWaiting Time |\tTurn Around Time")
for i, process in enumerate(processes):
    print(f"\t{i+1}\t\t\t\t{process[0]}\t\t\t\t{process[1]}\t\t\t\t{waiting_times[i]}\t\t\t\t\t{turn_around_times[i]}")

# Calculate and print the average waiting time and turn around time
avg_waiting_time = sum(waiting_times) / len(waiting_times)
avg_turn_around_time = sum(turn_around_times) / len(turn_around_times)
print(f"\nAverage Waiting Time: {avg_waiting_time}")
print(f"Average Turn Around Time: {avg_turn_around_time}")
