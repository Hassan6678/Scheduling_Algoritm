#Code ... FCFS algorithm
file = open("file.txt", "r")
process_name = []
arrival_time = []
burst_time = []
file_data = []
waiting_time = []
turnaround_time = []
total_waiting_time = 0
for line in file:
    for word in line.split():
        file_data.append(word)
for i in range(0, len(file_data), 3):
    process_name.append(file_data[i])
    i = i + 1
    arrival_time.append(int(file_data[i]))
    i = i + 1
    burst_time.append(int(file_data[i]))
    i = i + 1 
count = 0
for burs_time in burst_time:
    waiting_time.append(total_waiting_time - arrival_time[count])
    spend_time = 0
    while spend_time < burs_time:
        spend_time += 1
    total_waiting_time += spend_time
    print("|---", process_name[count],'(', total_waiting_time,')', end=" ")
    turnaround_time.append(total_waiting_time - arrival_time[count])
    count += 1
total_time = 0
for time in waiting_time:
    total_time += time
print("\nTotal Waiting Time : ", total_time/len(process_name))
total_time = 0
for time in turnaround_time:
    total_time += time
print("Total Turnaround Time : ", total_time/len(process_name))