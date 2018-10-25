import pandas as pd
import matplotlib.pyplot as plt
import sys
from datetime import datetime
#from pathlib import Path

def getSysArg():
    try:
        ARG_FILENAME = sys.argv[1]
    except:
        ARG_FILENAME = 'output_20180808_152731.csv'
    
    return ARG_FILENAME

if __name__ == '__main__':
    ReadFileName = getSysArg()
    data = pd.read_csv(ReadFileName,names=['gen_id','v_string','max_fitness'])  #,index_col='gen_id'
    df_tmp_maxfitness = data.iloc[:,[0,2]]
    df_tmp_maxfitness.plot()
    plt.savefig("genid_maxfitness"+ReadFileName+"_"+datetime.now().strftime('%Y%m%d_%H%M%S')+".png")
    plt.show()
