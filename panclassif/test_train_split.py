def splitCancer(homepath,names):
	#for cancer
	import os
	import numpy as np
	import pandas as pd
	import csv
	import random
	from sklearn.preprocessing import StandardScaler
	import warnings
	warnings.filterwarnings("ignore")

	# Directory 
	directory = "test_data"
	# Parent Directory path 
	parent_dir = homepath
	# Path 
	path = os.path.join(parent_dir, directory)
	if not os.path.exists(path):
		os.mkdir(path) 

	# Directory 
	directory = "pre_upsample_train_data"
	# Parent Directory path 
	parent_dir = homepath
	# Path 
	path = os.path.join(parent_dir, directory)
	if not os.path.exists(path):
		os.mkdir(path) 

	# Directory 
	directory = "test_data/cancer"
	# Parent Directory path 
	parent_dir = homepath
	# Path 
	path = os.path.join(parent_dir, directory)
	if not os.path.exists(path):
		os.mkdir(path)

	# Directory 
	directory = "test_data/normal"
	# Parent Directory path 
	parent_dir = homepath
	# Path 
	path = os.path.join(parent_dir, directory)
	if not os.path.exists(path):
		os.mkdir(path)

	# Directory 
	directory = "pre_upsample_train_data/cancer"
	# Parent Directory path 
	parent_dir = homepath
	# Path 
	path = os.path.join(parent_dir, directory)
	if not os.path.exists(path):
		os.mkdir(path)

	# Directory 
	directory = "pre_upsample_train_data/normal"
	# Parent Directory path 
	parent_dir = homepath
	# Path 
	path = os.path.join(parent_dir, directory)
	if not os.path.exists(path):
		os.mkdir(path)

	#len(cancer_names)
	for index in range(len(names)):
	  Cancer = pd.read_csv(homepath+"/data_after_genefilter/cancer/"+names[index]+".txt.bz2",header=None, delimiter = '\t')
	  # print(cancer_names[index])
	  # print(len(Cancer.columns))
	  val_train = round((len(Cancer.columns) * 75) / 100) 
	  val_test = len(Cancer.columns) - val_train
	  # print(val_train)
	  # print(val_test)
	  # print()
	  i = 0

	  cols_for_test = []
	  cols_for_train = []

	  while i < val_test:
	    x = random.randint(0,(len(Cancer.columns)-1))
	    if x not in cols_for_test:
	      cols_for_test.append(x)
	      i += 1
	  i = 0
	  while i < val_train:
	    x = random.randint(0,(len(Cancer.columns)-1))
	    if x not in cols_for_test:
	      if x not in cols_for_train:
	        cols_for_train.append(x)
	        i += 1

	  test_cancer = Cancer.drop(columns = cols_for_train)
	  train_cancer = Cancer.drop(columns = cols_for_test)

	  test_cancer.to_csv(r''+homepath+"/test_data/cancer/"+names[index]+'.txt.bz2',compression="bz2", sep='\t',header=None,index=None,index_label=None)
	  train_cancer.to_csv(r''+homepath+"/pre_upsample_train_data/cancer/"+names[index]+'.txt.bz2',compression="bz2", sep='\t',header=None,index=None,index_label=None)


def splitNormal(homepath,names):
	#for normal
	import os
	import numpy as np
	import pandas as pd
	import csv
	import random
	from sklearn.preprocessing import StandardScaler

	#len(cancer_names)
	for index in range(len(names)):
	  Cancer = pd.read_csv(homepath+"/data_after_genefilter/normal/"+names[index]+".txt.bz2",header=None, delimiter = '\t')
	  # print(cancer_names[index])
	  # print(len(Cancer.columns))
	  if(len(Cancer.columns) != 2):
	    val_train = round((len(Cancer.columns) * 75) / 100) 
	    val_test = len(Cancer.columns) - val_train
	    # print(val_train)
	    # print(val_test)
	    # print()
	    i = 0

	    cols_for_test = []
	    cols_for_train = []

	    while i < val_test:
	      x = random.randint(0,(len(Cancer.columns)-1))
	      if x not in cols_for_test:
	        cols_for_test.append(x)
	        i += 1
	    i = 0
	    while i < val_train:
	      x = random.randint(0,(len(Cancer.columns)-1))
	      if x not in cols_for_test:
	        if x not in cols_for_train:
	          cols_for_train.append(x)
	          i += 1

	    test_cancer = Cancer.drop(columns = cols_for_train)
	    train_cancer = Cancer.drop(columns = cols_for_test)

	    test_cancer.to_csv(r''+homepath+"/test_data/normal/"+names[index]+'.txt.bz2',compression="bz2", sep='\t',header=None,index=None,index_label=None)
	    train_cancer.to_csv(r''+homepath+"/pre_upsample_train_data/normal/"+names[index]+'.txt.bz2',compression="bz2", sep='\t',header=None,index=None,index_label=None)

	  else:
	    val_train = 2
	    val_test = 1
	    # print(val_train)
	    # print(val_test)
	    # print()
	    cols_for_train = [1]
	    test_cancer = Cancer.drop(columns = cols_for_train)
	    train_cancer = Cancer

	    test_cancer.to_csv(r''+homepath+"/test_data/normal/"+names[index]+'.txt.bz2',compression="bz2", sep='\t',header=None,index=None,index_label=None)
	    train_cancer.to_csv(r''+homepath+"/pre_upsample_train_data/normal/"+names[index]+'.txt.bz2',compression="bz2", sep='\t',header=None,index=None,index_label=None)

