#Code...SRJF Algorithm.....
file = open("file.txt", "r")
process_name = []
arrival_time = []
burst_time = []
file_data = []
waiting_tim = []
turnaround_tim = []
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
#SRJF
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

loop = sum(arrival_time)
waiting_time = [[0 for x in range(2)] for x in range(len(process_name))]
turnaround_time = [[0 for x in range(2)] for x in range(len(process_name))]
count = 0
start_time = 0
spend_time = 0
for i in range(len(mylist)):
    if count < len(mylist):
        if mylist[count][1] == i:
            waiting_time[count][0] = mylist[count][0]
            spend_time = 0
            while spend_time < mylist[count][2]:
                spend_time += 1
            waiting_time[count][1] = abs(total_waiting_time)
            total_waiting_time = total_waiting_time + mylist[count][2]
            total_waiting_time = i + mylist[count][2]
            turnaround_time[count][0] = mylist[count][0]
            turnaround_time[count][1] = total_waiting_time - mylist[count][1]
            print("|---", process_name[count], '(', total_waiting_time, ')', end=" ")
            count += 1
        else:
            start_time += 1
            total_waiting_time += 1


print("\n",waiting_time)
print(turnaround_time)
time = 0
print("\nTotal Waiting Time : ", sum(waiting_tim)/len(process_name))
print("Total Turnaround Time : ", sum(turnaround_tim)/len(process_name))

