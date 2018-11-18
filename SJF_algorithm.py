#Code...SJF Algorithm.....
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
#SJF
for i in range(0, len(burst_time) - 1):  # applying bubble sort to sort process according to their burst time
    for j in range(0, len(burst_time) - i - 1):  # and arrival time
        if arrival_time[j] == arrival_time[j+1]:
            if burst_time[j] > burst_time[j + 1]:
                temp_burst = burst_time[j]
                temp_name = process_name[j]
                burst_time[j] = burst_time[j + 1]
                process_name[j] = process_name[j + 1]
                burst_time[j + 1] = temp_burst
                process_name[j + 1] = temp_name
mylist = [[0 for x in range(3)] for x in range(len(process_name))]
for row in range(len(process_name)):
    mylist[row][0] = process_name[row]
    mylist[row][1] = int(arrival_time[row])
    mylist[row][2] = int(burst_time[row])
count = 0
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
print("\nTotal Waiting Time : ", sum(waiting_time)/len(process_name))
print("Total Turnaround Time : ", sum(turnaround_time)/len(process_name))