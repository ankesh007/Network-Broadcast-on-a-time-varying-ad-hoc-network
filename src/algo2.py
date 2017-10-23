from __future__ import division
import csv
import sys
import operator
import random

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

	if(len(sys.argv)<5):
		print("Use: <script_name> <Top_S%> <Bottom_L%> <Transmission_Prob_to_super_nodes(%)> <Transmission_Prob_to_Oridinary_nodes(%)> <Source_Node>")
		exit(0)

	devices={}
	device_neighbour_set={}
	brodcasted_to=0

	# K=int(sys.argv[1])
	K=20000
	S=float(sys.argv[1])/100
	L=float(sys.argv[2])/100
	TP=float(sys.argv[3])
	TPO=float(sys.argv[4])

	percent_check=0.9

	data_generated_at=int(sys.argv[5])
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
				device_neighbour_set[device_id1]=set()
				device_neighbour_set[device_id1].add(device_id2)

			if(device_id2 in devices):
				device_neighbour_set[device_id2].add(device_id1)
				pass
			else:
				devices[device_id2]=DEVICE(device_id2)
				device_count=device_count+1
				device_neighbour_set[device_id2]=set()
				device_neighbour_set[device_id2].add(device_id1)

# ***************File Reading Ended**************************
	
	device_degree_count={}

# ****************Extracting length of neighbour set************************
	for elements in device_neighbour_set:
		device_degree_count[elements]=len(device_neighbour_set[elements])

# ****************Sorting dictionary according to number of unique neighbours and storing in list***********
	sorted_device_degree = sorted(device_degree_count.items(), key=operator.itemgetter(1))
	device_category={}

	super_node_count=int(S*device_count)
	weakly_connected_node_count=int(L*device_count)

# Assigning Super nodes Category 1 in a dictionary

	temp_var=device_count-1
	while True:
		device_category[sorted_device_degree[temp_var][0]]=1
		temp_var=temp_var-1
		if(temp_var<device_count-super_node_count):
			break

# Assigning Weak nodes Category 3 in a dictionary

	temp_var=0
	while True:
		device_category[sorted_device_degree[temp_var][0]]=3
		temp_var=temp_var+1
		if(temp_var>weakly_connected_node_count):
			break

# Assigning Middle Class Ordinary nodes category 2 in a dictionary

	for elements in sorted_device_degree:
		if(elements[0] in device_category):
			pass
		else:
			device_category[elements[0]]=2

# *********************************************************************

	#convention that data_id for generated data is <device_id>_<brodcast_count>
	device_with_data=devices[data_generated_at]
	data_id=str(data_generated_at)+"_0" 
	data=DATA(data_id)
	device_with_data.to_forward[data_id]=(data,0)
	devices[data_generated_at]=device_with_data
	flag=False

	transmission_list=[0,0,0]

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

				if(device_category[device_id2]==1 and rand_int>TP):
					continue
				if(device_category[device_id2]==2 and rand_int>TPO):
					continue
				if(devices[device_id2].has_data(chunks[0])==False):
					devices[device_id2].receive_data(chunks[0],devices[device_id1])
					brodcasted_to=brodcasted_to+1
					devices[device_id1].to_forward[chunks[0].id]=(chunks[0],chunks[1]+1)
					transmission_list[device_category[device_id1]-1]=transmission_list[device_category[device_id1]-1]+1
					# print brodcasted_to," ",device_id1," ",device_id2 
					if(brodcasted_to>=device_count*percent_check):
						print K,",""Time:",time_stamp
						flag=True
						break

			if(flag==True):
				break
			devices[device_id1].update_forwarding(K)

#Device 2 transmission
			for chunk in devices[device_id2].to_forward:
				chunks=devices[device_id2].to_forward[chunk]
				if(device_category[device_id1]==1 and rand_int>TP):
					continue
				if(device_category[device_id1]==2 and rand_int>TPO):
					continue				

				if(devices[device_id1].has_data(chunks[0])==False):
					devices[device_id1].receive_data(chunks[0],devices[device_id2])
					brodcasted_to=brodcasted_to+1
					devices[device_id2].to_forward[chunks[0].id]=(chunks[0],chunks[1]+1)
					transmission_list[device_category[device_id2]-1]=transmission_list[device_category[device_id2]-1]+1
				# print brodcasted_to," ",device_id2," ",device_id1
					if(brodcasted_to>=device_count*percent_check):
						print K,",""Time:",time_stamp
						flag=True
						break
			
			if(flag==True):
				break
			devices[device_id2].update_forwarding(K)

		if(flag==False):
			print K,",","Reached only(in %):",(brodcasted_to/device_count)*100

		print "TransmissionsCount by [Super,Ordinary,Weak]:",transmission_list



if __name__=="__main__":
	main()



