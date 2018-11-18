totalwaitingtime=0
totalturnarroundtime=0
n= int(input("Enter number of processes :"))
bursttime=[0]*n
userp=[0]*n
waitingtime=[0]*n
turnarroundtime=[0]*n
temp=0
p=[0]*n
i=0
while i<n:
      p[i]=i
      i+=1
for i in range(n):
    bursttime[i]=int(input("Enter burst time :"))
    userp[i]=int(input("Enter user process:"))
for index in range(n):
    for k in range(n):
         if userp[i]>userp[k]:
            temp=p[i]
            p[i]=p[k]
            p[k]=bursttime[i]
            bursttime[i]=temp
            temp=userp[i]
            userp[i]=userp[k]
            userp[k]=temp
turnarroundtime[0]=bursttime[0]
for i in range(n-1):
     j=1
     j+=i
     waitingtime[j]=waitingtime[i] + bursttime[i];
for i in range(n):
    turnarroundtime[i]=waitingtime[i]+bursttime[i]; 

print ("Process    UserProcess   Bursttime    Waitingtime    Turnarroundtime")
for i in range(n):
     print("p[",i,"]","\t\t",(userp[k]),"\t\t",(bursttime[i]),"\t\t",(waitingtime[i]),"\t\t",(turnarroundtime[i]))
for i in range(n):
    totalwaitingtime=totalwaitingtime+waitingtime[i];
    totalturnarroundtime=totalturnarroundtime+turnarroundtime[i];
print("Average Waiting Time" ,totalwaitingtime/n)
print("Average Turn Arround Time", totalturnarroundtime/n)


    
