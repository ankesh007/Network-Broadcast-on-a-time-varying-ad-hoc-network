import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd


csv_name='avg_time'
csv_path=csv_name+'.csv'

ds=pd.read_csv(csv_path)
np_arr=ds.values

print np_arr.shape
np_arr=np_arr[0:67,:]

plt.figure()
plt.errorbar(np_arr[:,0],np_arr[:,1],yerr=np_arr[:,2],ecolor='red')
plt.title("Average Percentage of Nodes Reached v/s\n Transmission Probability to SuperNodes for S = 0.5% and L = 5%")
plt.xlabel("Transmission Probability to SuperNodes(X) in %")
plt.ylabel("Average % of Nodes Reached")
plt.savefig(csv_name+'.png',bbox_inches='tight')
# plt.show()
