import subprocess
import random
import csv
import numpy as np


# For starting device as 26, varying x

file_percent = open("part3/26_percent.csv",'w')
file_time = open("part3/26_time.csv",'w')
file_ginny = open("part3/26_ginny.csv",'w')

for x in range(0,101):		# set range(1,100)
	z = subprocess.check_output(["python", "algo3a.py",str(x), str(100-x), str(26) ])
	# print x
	y = z.split()
	# print y
	if int(y[0])==1 :
		file_time.write(str(x) + ',' + y[1] + '\n')
	else:
		file_percent.write(str(x) + ',' + y[1] + '\n')

	file_ginny.write(str(x) + ',' + y[2] + '\n')

file_percent.close()
file_time.close()
file_ginny.close()
# done 3a

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

file_percent = open("part3/avg_percent.csv",'w')
file_time = open("part3/avg_time.csv",'w')
file_ginny = open("part3/avg_ginny.csv",'w')

start_nodes = []

for j in range(100):
	x = random.randint(0,total-1)
	start_nodes.append(device_list[x])

for x in range(1,100,10):		# set range(1,100)

	# count_percent = 0
	# count_time = 0
	# total_percent = 0
	# total_time = 0

	times = []
	percents = []
	ginny = []

	for j in range(10):		# set range(100)
		z = subprocess.check_output(["python", "algo3a.py", str(x), str(100-x), str(start_nodes[j]) ])
		y = z.split()
		if int(y[0])==1 :
			times.append(float(y[1]))
		else:
			percents.append(float(y[1]))
		ginny.append(float(y[2]))

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

	file_percent.write(str(x) + ',' + str(mnp) + ',' + str(stdp) + '\n')
	file_time.write(str(x) + ',' + str(mnt) + ',' + str(stdt) + '\n')
	file_ginny.write(str(x) + ',' + str(np.mean(ginny)) + ',' + str(np.std(ginny)) + '\n')


file_percent.close()
file_time.close()	
file_ginny.close()
# done 3b
