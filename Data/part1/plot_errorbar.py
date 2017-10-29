import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
import sys

csv_name=sys.argv[1]
csv_path=csv_name+'.csv'

ds=pd.read_csv(csv_path)
np_arr=ds.values

print np_arr.shape
np_arr=np_arr[int(sys.argv[5]):int(sys.argv[6]),:]

plt.figure()
plt.errorbar(np_arr[:,0],np_arr[:,1],yerr=np_arr[:,2],ecolor='red')
plt.title(sys.argv[4])
plt.xlabel(sys.argv[2])
plt.ylabel(sys.argv[3])
plt.savefig("Plots/"+csv_name+'.png',bbox_inches='tight')
# plt.show()
