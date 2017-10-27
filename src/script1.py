import subprocess
import random
import csv
import numpy as np


# For starting device as 26, running for k = 0 to 100

file_percent = open("26_percent.csv",'w')
file_time = open("26_time.csv",'w')

for j in range(1,100):		# set range(1,100)
	x = subprocess.check_output(["python", "algo1a.py", str(j), str(26) ])
	# print x
	y = x.split()
	# print y
	if int(y[0])==1 :
		file_time.write(str(j) + ',' + y[1] + '\n')
	else:
		file_percent.write(str(j) + ',' + y[1] + '\n')

file_percent.close()
file_time.close()
# done 1a

# For random sarting points

devices = set()
filename="../proximityedgestimestamps.csv"

with open(filename,'rb') as csvfile:
	trace=csv.reader(csvfile,delimiter=';')

	for row in trace:
		if(len(row)<3):
			continue

		device_id1=int(row[1])
		device_id2=int(row[2])
		devices.add(device_id1)
		devices.add(device_id2)

total = len(devices)
device_list = list(devices)

file_percent = open("avg_percent.csv",'w')
file_time = open("avg_time.csv",'w')

start_nodes = []

for j in range(100):	# set range(100)
	x = random.randint(0,total-1)
	start_nodes.append(device_list[x])

for k in range(1,100):	# set range(1,100)

	# count_percent = 0
	# count_time = 0
	# total_percent = 0
	# total_time = 0

	times = []
	percents = []

	for j in range(100):		# set range(100)
		x = subprocess.check_output(["python", "algo1a.py", str(k), str(start_nodes[j]) ])
		# print x
		y = x.split()
		# print y
		if int(y[0])==1 :
			# count_time+=1
			# total_time+=float(y[1])
			times.append(float(y[1]))
		else:
			percents.append(float(y[1]))

	print k,len(times),len(percents)
	mnp = 0
	stdp = 0
	if len(percents)==0:
		mnp = 0
	else:
		mnp = np.mean(percents)
		stdp = np.std(percents)
	mnt = 0
	stdt = 0
	if len(times)==0:
		mnt = 0
	else:
		mnt = np.mean(times)
		stdt = np.std(times)

	file_percent.write(str(k) + ',' + str(mnp) + ',' + str(stdp) + '\n')
	file_time.write(str(k) + ',' + str(mnt) + ',' + str(stdt) + '\n')


file_percent.close()
file_time.close()	

# Find mean using sum/count