def upsampled(names,homepath):
	'''
	Parameters
	----------
	`names` (list): 
	  List of the cancer names found from `featSelect`
	  function.
	`homepath` (str): 
	  Path where you want to save all the generated files 
	  and folders. 

	Return:
	-------
	None

	Outputs:
	--------
	Upsample the train data into 3:1 ratio and save it in
	"~/train_data"
	'''

	import numpy as np
	import pandas as pd
	from sklearn.preprocessing import StandardScaler
	from imblearn.over_sampling import SMOTE
	from collections import Counter
	import os
	import warnings
	warnings.filterwarnings("ignore")

	# Directory 
	directory = "train_data"
	# Parent Directory path 
	parent_dir = homepath
	# Path 
	path = os.path.join(parent_dir, directory)
	if not os.path.exists(path):
		os.mkdir(path)

	# Directory 
	directory = "train_data/cancer"
	# Parent Directory path 
	parent_dir = homepath
	# Path 
	path = os.path.join(parent_dir, directory)
	if not os.path.exists(path):
		os.mkdir(path) 

	# Directory 
	directory = "train_data/normal"
	# Parent Directory path 
	parent_dir = homepath
	# Path 
	path = os.path.join(parent_dir, directory)
	if not os.path.exists(path):
		os.mkdir(path) 
	#len(names)
	print("Upsampling on train data is running")
	for index in range(len(names)):
	  Cancer = pd.read_csv(homepath+"/pre_upsample_train_data/cancer/"+
	                        names[index]+".txt.bz2",header=None, delimiter = '\t')
	  Normal = pd.read_csv(homepath+"/pre_upsample_train_data/normal/"+
	                        names[index]+".txt.bz2",header=None, delimiter = '\t')

	  can_sample = len(Cancer.columns)
	  norm_sample = len(Normal.columns)
	  Cancer = Cancer.T
	  Normal = Normal.T

	  if( norm_sample <= round(can_sample/3) ):
	    ## adding target in the last col
	    Cancer[str(len(Cancer.columns))] = 1
	    Normal[str(len(Normal.columns))] = 0
	    
	    #print(len(Cancer.columns))

	    frame = [Cancer,Normal]
	    Data = pd.concat(frame,axis=0)

	    #print(Data)

	    x = Data.iloc[:,:len(Cancer.columns)-1]
	    y = Data.iloc[:,len(Cancer.columns)-1]
	    # print(x)
	    # print(y)

	    # summarize class distribution
	    counter = Counter(y)
	    #print(counter)
	    # transform the dataset
	    oversample = SMOTE(k_neighbors=1, sampling_strategy=0.3333)
	    X, y = oversample.fit_resample(x, y)
	    # summarize the new class distribution
	    counter = Counter(y)
	    #print(counter)
	    X = pd.DataFrame(data=X)
	    y = pd.DataFrame(data=y)

	    data = pd.concat([X,y], axis = 1)
	    data = data.reset_index(drop=True)
	    data = data.T
	    data = data.reset_index(drop=True)
	    can = []
	    norm = []
	    for x in range(len(data.columns)):
	      if(data[x][len(data)-1]==0):
	        norm.append(x)
	      elif(data[x][len(data)-1]==1):
	        can.append(x)

	    drops_for_can = []

	    for x in range(len(data.columns)):
	      if(x not in can):
	        drops_for_can.append(x)
	    Cancer = data.drop(columns=drops_for_can)

	    drops_for_norm = []

	    for x in range(len(data.columns)):
	      if(x not in norm):
	        drops_for_norm.append(x)
	    Normal = data.drop(columns=drops_for_norm)

	    Cancer = Cancer.drop(Cancer.index[len(Cancer)-1])
	    Normal = Normal.drop(Normal.index[len(Normal)-1])

	    Cancer.to_csv(r''+homepath+'/train_data/cancer/'+names[index]+'.txt.bz2',compression="bz2", sep='\t',header=None,index=None,index_label=None)
	    Normal.to_csv(r''+homepath+'/train_data/normal/'+names[index]+'.txt.bz2',compression="bz2", sep='\t',header=None,index=None,index_label=None)
	print("Upsampling on train data has ended")
	print()