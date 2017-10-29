import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd


csv_name='26_nodesreached'
csv_path=csv_name+'.csv'

name1="K"
name2="Number of Nodes Reached"

ds=pd.read_csv(csv_path,header=None,names=[name1,name2])

sns.lmplot(x=name1,y=name2,data=ds,fit_reg=False)
plt.title("Hi")
plt.savefig(csv_name+'.png',bbox_inches='tight')
plt.show()
