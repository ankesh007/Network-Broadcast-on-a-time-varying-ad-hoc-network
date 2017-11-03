from __future__ import division
import csv
import sys
import operator
import random
import numpy as np
from math import log

filename="../proximityedgestimestamps.csv"


class DATA:
	def __init__(self,id):
		self.id=id

class DEVICE:

	def __init__(self,id):
		self.id=id
		self.to_forward={}
		self.received={}

	def has_data(self,data):
		if(data.id in self.received):
			return True
		if(data.id in self.to_forward):
			return True
		return False

	def receive_data(self,data,device):
		self.received[data.id]=(data,device)
		self.to_forward[data.id]=(data,0)

	def update_forwarding(self,K):
		temp_list=[]
		for chunk in self.to_forward:
			chunks=self.to_forward[chunk]
			if(chunks[1]==K):
				temp_list.append(chunk)
		for chunk_id in temp_list:
			del self.to_forward[chunk_id]


def main():

	devices={}
	device_neighbour_set={}
	device_broadcast_count={}
	brodcasted_to=0
	percent_check=0.9

	start_time=0
	device_count=0

# *************Processing the trace file for classifying hosts according to degree******************

	with open(filename,'rb') as csvfile:
		trace=csv.reader(csvfile,delimiter=';')

		for row in trace:
			if(len(row)<3):
				continue
			device_id1=int(row[1])
			device_id2=int(row[2])

			if(device_id1 in devices):
				device_neighbour_set[device_id1].add(device_id2)
				pass
			else:
				devices[device_id1]=DEVICE(device_id1)
				device_count=device_count+1
				device_broadcast_count[device_id1]=0
				device_neighbour_set[device_id1]=set()
				device_neighbour_set[device_id1].add(device_id2)

			if(device_id2 in devices):
				device_neighbour_set[device_id2].add(device_id1)
				pass
			else:
				devices[device_id2]=DEVICE(device_id2)
				device_count=device_count+1
				device_broadcast_count[device_id2]=0
				device_neighbour_set[device_id2]=set()
				device_neighbour_set[device_id2].add(device_id1)

# ***************File Reading Ended**************************
	
	device_degree_count={}

# ****************Extracting length of neighbour set************************
	for elements in device_neighbour_set:
		device_degree_count[elements]=len(device_neighbour_set[elements])

# ****************Sorting dictionary according to number of unique neighbours and storing in list***********
	sorted_device_degree = sorted(device_degree_count.items(), key=operator.itemgetter(1))

	# print sorted_device_degree
	device_category={}

# *********************************************************************

	CDF=[]
	last=0
	count=0
	# CDF=np.concatenate()	

	for elements in sorted_device_degree:
		if(last!=elements[1]):
			CDF.append([last,count])
			last=elements[1]
			count=1
		else:
			count=count+1
	CDF.append([last,count])

	x= len(CDF)
	for i in range(1,x,1):
		CDF[i][1]=CDF[i][1]+CDF[i-1][1]

	CCDF=[]
	for i in range(x):
		CCDF.append([CDF[i][0],device_count-CDF[i][1]])
	# print len(CCDF)
	del CDF[0]
	del CCDF[len(CCDF)-1]

	CCDF[0][0]=0.5

	for i in range(x-1):
		CDF[i]=[log(CDF[i][0]),log(CDF[i][1])]
		CCDF[i]=[log(CCDF[i][0]),log(CCDF[i][1])]

	# print CDF
	# print CCDF

	# print CDF
	# print len(CCDF)

	file1=open('CDF.csv','w')
	file2=open('CCDF.csv','w')

	for elements in CDF:
		print>>file1,elements[0],",",elements[1]

	for elements in CCDF:
		print>>file2,elements[0],",",elements[1]



if __name__=="__main__":
	main()



