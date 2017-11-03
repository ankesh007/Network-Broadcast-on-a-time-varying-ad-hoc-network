import subprocess
import random
import csv
import numpy as np


# For starting device as 26, running for s = 0.5, l = 70 , x = 1 to 99

file_percent = open("part2/26_percent.csv",'w')
file_time = open("part2/26_time.csv",'w')
file_trans = open("part2/26_trans.csv",'w')
file_ginny = open("part2/26_ginny.csv",'w')

for x in range(0,101):		# set range(0,101)
	z = subprocess.check_output(["python", "algo2a.py", str(0.5), str(70), str(x), str(100-x), str(26) ])
	# print x
	y = z.split()
	# print y
	if int(y[0])==1 :
		file_time.write(str(x) + ',' + y[1] + '\n')
	else:
		file_percent.write(str(x) + ',' + y[1] + '\n')

	file_trans.write(str(x) + ',' + y[2] + ',' + y[3] + ',' + y[4] + '\n')
	file_ginny.write(str(x) + ',' + y[5] + '\n')

file_percent.close()
file_time.close()
file_trans.close()
file_ginny.close()
# done 2a

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

file_percent = open("part2/avg_percent.csv",'w')
file_time = open("part2/avg_time.csv",'w')
file_trans = open("part2/avg_trans.csv",'w')
file_ginny = open("part2/avg_ginny.csv",'w')

start_nodes = []

for j in range(100):
	x = random.randint(0,total-1)
	start_nodes.append(device_list[x])

for x in range(1,100):		# set range(1,100)

	# count_percent = 0
	# count_time = 0
	# total_percent = 0
	# total_time = 0

	times = []
	percents = []
	trans_super = []
	trans_ord = []
	trans_weak = []
	ginny = []

	for j in range(100):		# set range(100)
		z = subprocess.check_output(["python", "algo2a.py", str(0.5), str(70), str(x), str(100-x), str(start_nodes[j]) ])
		y = z.split()
		if int(y[0])==1 :
			times.append(float(y[1]))
		else:
			percents.append(float(y[1]))
		trans_super.append(float(y[2]))
		trans_ord.append(float(y[3]))
		trans_weak.append(float(y[4]))
		ginny.append(float(y[5]))

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
	file_trans.write(str(x) + ',' + str(np.mean(trans_super)) + ',' + str(np.std(trans_super)) + ',' + str(np.mean(trans_ord)) + ',' + str(np.std(trans_ord)) + ',' + str(np.mean(trans_weak)) + ',' + str(np.std(trans_weak)) + '\n')
	file_ginny.write(str(x) + ',' + str(np.mean(ginny)) + ',' + str(np.std(ginny)) + '\n')


file_percent.close()
file_time.close()	
file_trans.close()
file_ginny.close()
# done 2b
"""
# varying s
file_percent = open("part2/s_percent.csv",'w')
file_time = open("part2/s_time.csv",'w')
file_trans = open("part2/s_trans.csv",'w')

z = subprocess.check_output(["python", "algo2a.py", str(1), str(70), str(50), str(50), str(26) ])
y = z.split()
if int(y[0])==1 :
	file_time.write(str(1) + ',' + y[1] + '\n')
else:
	file_percent.write(str(1) + ',' + y[1] + '\n')

file_trans.write(str(1) + ',' + y[2] + ',' + y[3] + ',' + y[4] + '\n')


for s in range(5,30,5):		# set range(100)
	z = subprocess.check_output(["python", "algo2a.py", str(s), str(70), str(50), str(50), str(26) ])
	y = z.split()
	if int(y[0])==1 :
		file_time.write(str(s) + ',' + y[1] + '\n')
	else:
		file_percent.write(str(s) + ',' + y[1] + '\n')

	file_trans.write(str(s) + ',' + y[2] + ',' + y[3] + ',' + y[4] + '\n')

file_percent.close()
file_time.close()
file_trans.close()
# done 2c

# varying l
file_percent = open("part2/l_percent.csv",'w')
file_time = open("part2/l_time.csv",'w')
file_trans = open("part2/l_trans.csv",'w')

for l in range(10,100,10):		# set range(100)
	z = subprocess.check_output(["python", "algo2a.py", str(0.5), str(l), str(50), str(50), str(26) ])
	y = z.split()
	if int(y[0])==1 :
		file_time.write(str(l) + ',' + y[1] + '\n')
	else:
		file_percent.write(str(l) + ',' + y[1] + '\n')

	file_trans.write(str(l) + ',' + y[2] + ',' + y[3] + ',' + y[4] + '\n')

file_percent.close()
file_time.close()
file_trans.close()
# done 2d
"""