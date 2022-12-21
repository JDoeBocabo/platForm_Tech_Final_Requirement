# number of processes
num_processes = int(input("Enter the number of processes: "))

# quantum time for each process
quantum = int(input("Enter the quantum time: "))

# burst time for each process
burst_times = []
for i in range(num_processes):
    burst_time = int(input(f"Enter burst time for process {i+1}: "))
    burst_times.append(burst_time)

# waiting time for each process
waiting_times = [0] * num_processes

# turn around time for each process
turn_around_times = [0] * num_processes

# remaining burst time for each process
remaining_burst_times = burst_times[:]

# time elapsed
time_elapsed = 0

# boolean to check if all processes are completed
all_processes_completed = False

while not all_processes_completed:
    all_processes_completed = True
    for i in range(num_processes):
        if remaining_burst_times[i] > 0:
            all_processes_completed = False
            if remaining_burst_times[i] > quantum:
                time_elapsed += quantum
                remaining_burst_times[i] -= quantum
            else:
                time_elapsed += remaining_burst_times[i]
                waiting_times[i] = time_elapsed - burst_times[i]
                remaining_burst_times[i] = 0

# compute turn around time for each process
for i in range(num_processes):
    turn_around_times[i] = waiting_times[i] + burst_times[i]

# print results in a table form
print("Process\t\tBurst Time\tWaiting Time\tTurn Around Time")
for i in range(num_processes):
    print(f"{i+1}\t\t\t\t{burst_times[i]}\t\t\t\t{waiting_times[i]}\t\t\t{turn_around_times[i]}")

# sum of waiting times
sum_waiting_times = sum(waiting_times)

# sum of turn around times
sum_turn_around_times = sum(turn_around_times)

# average waiting time
avg_waiting_time = sum_waiting_times / num_processes

# average turn around time
avg_turn_around_time = sum_turn_around_times / num_processes

print(f"Average Waiting Time: {avg_waiting_time}")
print(f"Average Turn Around Time: {avg_turn_around_time}")
