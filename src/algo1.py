from __future__ import division
import csv
import sys

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

	if(len(sys.argv)<3):
		print("Use: <script_name> <Parameter_K> <Source_node>")
		exit(0)

	devices={}
	brodcasted_to=0

	K=int(sys.argv[1])
	data_generated_at=int(sys.argv[2])
	percent_check=0.9
	start_time=0

	device_count=1
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

			if(device_id2 in devices):
				pass
			else:
				devices[device_id2]=DEVICE(device_id2)
				device_count=device_count+1
	

	data_id=str(data_generated_at)+"_0" 
	#convention that data_id for generated data is <device_id>_<brodcast_count>
	data=DATA(data_id)
	device_with_data=DEVICE(data_generated_at)
	device_with_data.to_forward[data_id]=(data,0)
	devices[data_generated_at]=device_with_data
	devices[data_generated_at].update_forwarding(K)
	flag=False


	with open(filename,'rb') as csvfile:
		trace=csv.reader(csvfile,delimiter=';')

		for row in trace:
			if(len(row)<3):
				continue
			
			time_stamp=int(row[0])
			device_id1=int(row[1])
			device_id2=int(row[2])
			for chunk in devices[device_id1].to_forward:
				chunks=devices[device_id1].to_forward[chunk]

				if(devices[device_id2].has_data(chunks[0])==False):
					devices[device_id2].receive_data(chunks[0],devices[device_id1])
					brodcasted_to=brodcasted_to+1
					devices[device_id1].to_forward[chunks[0].id]=(chunks[0],chunks[1]+1)
					# print brodcasted_to," ",device_id1," ",device_id2 
					if(brodcasted_to>=device_count*percent_check):
						print K,",""Time:",time_stamp
						flag=True
						break

			if(flag==True):
				break
			devices[device_id1].update_forwarding(K)

			for chunk in devices[device_id2].to_forward:
				chunks=devices[device_id2].to_forward[chunk]

				if(devices[device_id1].has_data(chunks[0])==False):
					devices[device_id1].receive_data(chunks[0],devices[device_id2])
					brodcasted_to=brodcasted_to+1
					devices[device_id2].to_forward[chunks[0].id]=(chunks[0],chunks[1]+1)
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



if __name__=="__main__":
	main()



