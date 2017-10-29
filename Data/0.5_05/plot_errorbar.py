import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd

csv_path='avg_percent.csv'

ds=pd.read_csv(csv_path)
np_arr=ds.values

print np_arr.shape

plt.figure()
plt.errorbar(np_arr[:,0],np_arr[:,1],yerr=np_arr[:,2],ecolor='red')
plt.title("Average")
plt.xlabel("Transmission Probability to SuperNodes(X) in %")
plt.ylabel("Average % of Nodes Reached")
plt.savefig('avg_percent'+'.png')
# plt.show()
