import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
import sys

csv_name=sys.argv[1]
name1=sys.argv[2]
name2="Average Transmissions by SuperNode"
name3="Average Transmissions by OrdinaryNode"
name4="Average Transmissions by WeakNode"

# title=sys.argv[4]
csv_path=csv_name+'.csv'

ds=pd.read_csv(csv_path,header=None,names=[name1,name2,name3,name4])
#print ds.shape

sns.lmplot(x=name1,y=name2,data=ds,fit_reg=True)
plt.title("Average Transmissions by super node starting from node 26 vs Transmissions Probability(to Super Node)")
plt.savefig("Plots/"+csv_name+'Super.png',bbox_inches='tight')
# plt.show()
sns.lmplot(x=name1,y=name3,data=ds,fit_reg=True)
plt.title("Average Transmissions by ordinary node starting from node 26 vs Transmissions Probability(to Super Node)")
plt.savefig("Plots/"+csv_name+'Ordinary.png',bbox_inches='tight')
sns.lmplot(x=name1,y=name4,data=ds,fit_reg=True)
plt.title("Average Transmissions by weak node starting from node 26 vs Transmissions Probability(to Super Node)")
plt.savefig("Plots/"+csv_name+'Weak.png',bbox_inches='tight')
