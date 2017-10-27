from __future__ import division
import csv
import sys
import operator
import random
import numpy as np

filename="../proximityedgestimestamps.csv"
filename2="../modularityclass.csv"


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

	if(len(sys.argv)<4):
		print("Use: <script_name> <Transmission Prob.(X in %)> <Transmission Porb(Y in %)> <Source_Node>")
		exit(0)

	devices={}
	device_community={}
	device_broadcast_count={}
	brodcasted_to=0

	# K=int(sys.argv[1])
	X=float(sys.argv[1])
	Y=float(sys.argv[2])

	percent_check=0.9

	data_generated_at=int(sys.argv[3])
	start_time=0
	device_count=0

# *************Processing the trace file for classifying hosts according to degree******************

	with open(filename2,'rb') as csvfile:
		trace=csv.reader(csvfile,delimiter=';')

		for row in trace:
			if(len(row)<2):
				continue

			device_id1=int(row[0])
			class_device=int(row[1])

			if(device_id1 in device_community):
				pass
			else:
				device_community[device_id1]=class_device

	with open(filename,'rb') as csvfile:
		trace=csv.reader(csvfile,delimiter=';')

		for row in trace:
			if(len(row)<3):
				continue
			device_id1=int(row[1])
			device_id2=int(row[2])

			if(device_id1 in devices):
				pass
			else:
				devices[device_id1]=DEVICE(device_id1)
				device_count=device_count+1
				device_broadcast_count[device_id1]=0

				# print device_community[device_id1]

			if(device_id2 in devices):
				pass
			else:
				devices[device_id2]=DEVICE(device_id2)
				device_count=device_count+1
				device_broadcast_count[device_id2]=0

				# print device_community[device_id2]

	
	device_with_data=devices[data_generated_at]
	data_id=str(data_generated_at)+"_0" 
	data=DATA(data_id)
	device_with_data.to_forward[data_id]=(data,0)
	devices[data_generated_at]=device_with_data
	flag=False


	with open(filename,'rb') as csvfile:
		trace=csv.reader(csvfile,delimiter=';')

		for row in trace:
			if(len(row)<3):
				continue
			
			time_stamp=int(row[0])
			device_id1=int(row[1])
			device_id2=int(row[2])
			
# Device 1 transmission
			for chunk in devices[device_id1].to_forward:
				chunks=devices[device_id1].to_forward[chunk]

				rand_int=random.randint(0,101)

				if(device_community[device_id1]==device_community[device_id2] and rand_int>Y):
					continue
				if(device_community[device_id1]!=device_community[device_id2] and rand_int>X):
					continue				
				if(devices[device_id2].has_data(chunks[0])==False):
					devices[device_id2].receive_data(chunks[0],devices[device_id1])
					brodcasted_to=brodcasted_to+1
					devices[device_id1].to_forward[chunks[0].id]=(chunks[0],chunks[1]+1)
					device_broadcast_count[device_id1]=device_broadcast_count[device_id1]+1

					if(brodcasted_to>=device_count*percent_check):
						print "X:",X," Y:",Y," Time:",time_stamp
						flag=True
						break

			if(flag==True):
				break

#Device 2 transmission
			for chunk in devices[device_id2].to_forward:
				chunks=devices[device_id2].to_forward[chunk]
				rand_int=random.randint(0,101)

				if(device_community[device_id1]==device_community[device_id2] and rand_int>Y):
					continue
				if(device_community[device_id1]!=device_community[device_id2] and rand_int>X):
					continue				
				if(devices[device_id1].has_data(chunks[0])==False):
					devices[device_id1].receive_data(chunks[0],devices[device_id2])
					brodcasted_to=brodcasted_to+1
					devices[device_id2].to_forward[chunks[0].id]=(chunks[0],chunks[1]+1)
					device_broadcast_count[device_id2]=device_broadcast_count[device_id2]+1

					if(brodcasted_to>=device_count*percent_check):
						print "X:",X," Y:",Y," Time:",time_stamp
						flag=True
						break
			
			if(flag==True):
				break

		if(flag==False):
			print "X:",X," Y:",Y,",","Reached only(in %):",(brodcasted_to/device_count)*100

	device_broacast_list=[]

	for elements in device_broadcast_count:
		device_broacast_list.append(device_broadcast_count[elements])

	# print (device_broacast_list)

	np_arr=np.asarray(device_broacast_list)

	pair_wise_diff_sum=np.sum(np.abs(np_arr[:,np.newaxis]-np_arr))
	linear_sum=np.sum(np_arr)

	print (pair_wise_diff_sum/(2*device_count*(0.00000001+linear_sum)))


if __name__=="__main__":
	main()



