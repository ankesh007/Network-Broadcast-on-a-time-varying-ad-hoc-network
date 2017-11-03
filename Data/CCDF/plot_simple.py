import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
import sys

csv_name=sys.argv[1]
name1=sys.argv[2]
name2=sys.argv[3]
title=sys.argv[4]
csv_path=csv_name+'.csv'

ds=pd.read_csv(csv_path,header=None,names=[name1,name2])

sns.lmplot(x=name1,y=name2,data=ds,fit_reg=False)
plt.title(title)
plt.savefig("Plots/"+csv_name+'.png',bbox_inches='tight')
# plt.show()
