# Function to calculate waiting time
def calculate_waiting_time(processes, n, wt):
    wt[0] = 0
    for i in range(1, n):
        wt[i] = processes[i - 1]['burst_time'] + wt[i - 1]

# Function to calculate turn around time
def calculate_turn_around_time(processes, n, wt, tat):
    for i in range(n):
        tat[i] = processes[i]['burst_time'] + wt[i]

# Function to calculate average waiting and turn-around times
def calculate_avg_time(processes, n):
    wt = [0] * n
    tat = [0] * n

    # Function to find waiting time of all processes
    calculate_waiting_time(processes, n, wt)

    # Function to find turn around time for all processes
    calculate_turn_around_time(processes, n, wt, tat)

    # Display processes along with all details
    print("Processes | Arrival Time | Burst Time | Waiting",
          "Time | Turn-Around Time")
    total_wt = 0
    total_tat = 0
    for i in range(n):
        total_wt = total_wt + wt[i]
        total_tat = total_tat + tat[i]
        print(" ", processes[i]['name'], "\t\t",
              processes[i]['arrival_time'], "\t\t\t\t",
              processes[i]['burst_time'], "\t\t\t\t\t",
              wt[i], "\t\t\t\t ", tat[i])

    print("\nAverage waiting time = %.5f " %
          (total_wt / n))
    print("Average turn around time = %.5f " %
          (total_tat / n))

# Driver code
# Get the number of processes
n = int(input("Enter the number of processes: "))

# Initialize the list of processes
processes = []

# Get the details of each process
for i in range(n):
    name = input("Enter the name of the process: ")
    arrival_time = int(input("Enter the arrival time of the process: "))
    burst_time = int(input("Enter the burst time of the process: "))
    processes.append({'name': name, 'arrival_time': arrival_time, 'burst_time': burst_time})

# Function to find the waiting time, turn
# around time and average waiting time
# and turnaround time
calculate_avg_time(processes, n)
