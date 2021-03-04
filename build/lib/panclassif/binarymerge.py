def btrain(names,homepath):
	import numpy as np
	import pandas as pd
	import warnings
	warnings.filterwarnings("ignore")

	#reading data and doing work
	cresult=pd.DataFrame()
	nresult=pd.DataFrame()
	for index in range(len(names)):
	  Cancer = pd.read_csv(homepath+"/train_data/cancer/"+
	                       names[index]+".txt.bz2",header=None, delimiter = "\t")
	  Normal = pd.read_csv(homepath+"/train_data/normal/"+
	                       names[index]+".txt.bz2",header=None, delimiter = "\t")
	  
	  Cancer= Cancer.T
	  Normal=Normal.T
	  
	  frames1 = [Cancer, cresult]
	  cresult = pd.concat(frames1)
	  
	  frames2 = [Normal, nresult]
	  nresult = pd.concat(frames2)
	  
	# merging all the cancer and normal data together and saving them  
	cresult.to_csv(r''+homepath+'/train_data/bin_Cancer.txt.bz2',
	               compression="bz2", sep='\t',header=None,index=None,index_label=None)

	nresult.to_csv(r''+homepath+'/train_data/bin_Normal.txt.bz2',
	               compression="bz2", sep='\t',header=None,index=None,index_label=None)


def btest(names,homepath):
	import numpy as np
	import pandas as pd
	import warnings
	warnings.filterwarnings("ignore")

	#reading data and doing work
	cresult=pd.DataFrame()
	nresult=pd.DataFrame()
	for index in range(len(names)):
	  Cancer = pd.read_csv(homepath+"/test_data/cancer/"+
	                       names[index]+".txt.bz2",header=None, delimiter = "\t")
	  Normal = pd.read_csv(homepath+"/test_data/normal/"+
	                       names[index]+".txt.bz2",header=None, delimiter = "\t")
	  
	  Cancer= Cancer.T
	  Normal=Normal.T
	  
	  frames1 = [Cancer, cresult]
	  cresult = pd.concat(frames1)
	  
	  frames2 = [Normal, nresult]
	  nresult = pd.concat(frames2)
	  
	# merging all the cancer and normal data together and saving them  
	cresult.to_csv(r''+homepath+'/test_data/bin_Cancer.txt.bz2',
	               compression="bz2", sep='\t',header=None,index=None,index_label=None)

	nresult.to_csv(r''+homepath+'/test_data/bin_Normal.txt.bz2',
	               compression="bz2", sep='\t',header=None,index=None,index_label=None)