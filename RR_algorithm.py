#RR_algorithm.....

count_time = 0;
count_array = 0;

i = 0;
process_name = []
arrival_time = []
burst_time = []
file_data = []
waiting_time = []
turnaround_time = []
total_waiting_time = 0
file = open("file.txt","r")
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
slice_time = 0
print("Data read from file\nSlice Time : ")
slice_time = input()
print(slice_time)
#sort
for i in range(0, len(burst_time) - 1):  # applying bubble sort to sort process according to their burst time
    for j in range(0, len(burst_time) - i - 1):  # and arrival time
        if arrival_time[j] == arrival_time[j + 1]:
            if burst_time[j] > burst_time[j + 1]:
                temp_burst = burst_time[j]
                temp_name = process_name[j]
                burst_time[j] = burst_time[j + 1]
                process_name[j] = process_name[j + 1]
                burst_time[j + 1] = temp_burst
                process_name[j + 1] = temp_name
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