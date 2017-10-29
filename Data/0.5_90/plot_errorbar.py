import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd


csv_name='avg_time'
csv_path=csv_name+'.csv'

ds=pd.read_csv(csv_path)
np_arr=ds.values

print np_arr.shape
np_arr=np_arr[:,:]

plt.figure()
plt.errorbar(np_arr[:,0],np_arr[:,1],yerr=np_arr[:,2],ecolor='red')
plt.title("Average Time to Reach 90% Nodes v/s\n Transmission Probability to SuperNodes\nfor S = 0.5% and L = 90%")
plt.xlabel("Transmission Probability to SuperNodes(X) in %")
plt.ylabel("Average Time to Reach 90% Nodes")
plt.savefig(csv_name+'.png',bbox_inches='tight')
# plt.show()


csv_name='avg_percent'
csv_path=csv_name+'.csv'

ds=pd.read_csv(csv_path)
np_arr=ds.values

print np_arr.shape
# np_arr=np_arr[0:67,:]

plt.figure()
plt.errorbar(np_arr[:,0],np_arr[:,1],yerr=np_arr[:,2],ecolor='red')
plt.title("Average Percentage of Nodes Reached v/s\n Transmission Probability to SuperNodes\nfor S = 0.5% and L = 90%")
plt.xlabel("Transmission Probability to SuperNodes(X) in %")
plt.ylabel("Average % of Nodes Reached")
plt.savefig(csv_name+'.png',bbox_inches='tight')
# plt.show()


csv_name='avg_ginny'
csv_path=csv_name+'.csv'

ds=pd.read_csv(csv_path)
np_arr=ds.values

print np_arr.shape
# np_arr=np_arr[0:67,:]

plt.figure()
plt.errorbar(np_arr[:,0],np_arr[:,1],yerr=np_arr[:,2],ecolor='red')
plt.title("Average Ginny Coefficient v/s\n Transmission Probability to SuperNodes\nfor S = 0.5% and L = 90%")
plt.xlabel("Transmission Probability to SuperNodes(X) in %")
plt.ylabel("Average Value of Ginny Coeff.")
plt.savefig(csv_name+'.png',bbox_inches='tight')
# plt.show()


csv_name='avg_trans'
csv_path=csv_name+'.csv'

ds=pd.read_csv(csv_path)
np_arr=ds.values

print np_arr.shape
# np_arr=np_arr[0:67,:]

plt.figure()
plt.errorbar(np_arr[:,0],np_arr[:,1],yerr=np_arr[:,2],ecolor='red')
plt.title("Average No. of Transmissions by SuperNodes v/s\n Transmission Probability to SuperNodes\nfor S = 0.5% and L = 90%")
plt.xlabel("Transmission Probability to SuperNodes(X) in %")
plt.ylabel("Average No. of Transmissions made by SuperNodes")
plt.savefig(csv_name+ '_super' +'.png',bbox_inches='tight')
# plt.show()

plt.figure()
plt.errorbar(np_arr[:,0],np_arr[:,3],yerr=np_arr[:,4],ecolor='red')
plt.title("Average No. of Transmissions by Ordinary Nodes v/s\n Transmission Probability to SuperNodes\nfor S = 0.5% and L = 90%")
plt.xlabel("Transmission Probability to SuperNodes(X) in %")
plt.ylabel("Average No. of Transmissions made by Ordinary Nodes")
plt.savefig(csv_name+ '_ordinary' +'.png',bbox_inches='tight')
# plt.show()

plt.figure()
plt.errorbar(np_arr[:,0],np_arr[:,5],yerr=np_arr[:,6],ecolor='red')
plt.title("Average No. of Transmissions by WeakNodes v/s\n Transmission Probability to SuperNodes\nfor S = 0.5% and L = 90%")
plt.xlabel("Transmission Probability to SuperNodes(X) in %")
plt.ylabel("Average No. of Transmissions made by WeakNodes")
plt.savefig(csv_name+ '_weak' +'.png',bbox_inches='tight')
# plt.show()

