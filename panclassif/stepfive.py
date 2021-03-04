def step5(homepath,names,smoothed_cancer,smoothed_normal):
	import os
	import numpy as np
	import pandas as pd
	import csv
	import random
	from sklearn.preprocessing import StandardScaler

	from os import listdir
	from os.path import isfile, join
	import warnings
	warnings.filterwarnings("ignore")
	
	cancerfiles = [f for f in listdir(smoothed_cancer) if isfile(join(smoothed_cancer, f))]
	normalfiles = [f for f in listdir(smoothed_normal) if isfile(join(smoothed_normal, f))]

	# Directory 
	directory = "data_after_genefilter"
	# Parent Directory path 
	parent_dir = homepath
	# Path 
	path = os.path.join(parent_dir, directory) 
	if not os.path.exists(path):
		os.mkdir(path) 

	directory = "cancer"
	# Parent Directory path 
	parent_dir = homepath+"/data_after_genefilter/"
	# Path 
	path = os.path.join(parent_dir, directory) 
	if not os.path.exists(path):
		os.mkdir(path)

	directory = "normal"
	# Parent Directory path 
	parent_dir = homepath+"/data_after_genefilter/"
	# Path 
	path = os.path.join(parent_dir, directory)
	if not os.path.exists(path):
		os.mkdir(path)

	# loading the genes that need to delete and saving the data again after removing the deleted genes
	selected_genes = np.load(homepath+"/std_npy/genes_to_del.npy")

	list.sort(cancerfiles)
	list.sort(normalfiles)

	for index in range(len(names)):
	  Cancer = pd.read_csv(smoothed_cancer+'/'+cancerfiles[index],header=None, delimiter = '\t')
	  Normal = pd.read_csv(smoothed_normal+'/'+normalfiles[index],header=None, delimiter = '\t')

	  Cancer = Cancer.T
	  Normal = Normal.T

	  cancer = Cancer.drop(columns = selected_genes)
	  normal = Normal.drop(columns = selected_genes)

	  print(names[index])
	  print(cancer.shape)
	  print(normal.shape)

	  cancer = cancer.T
	  normal = normal.T

	  std_scaler_can = StandardScaler()
	  std_scaler_norm = StandardScaler()

	  cancer = pd.DataFrame(std_scaler_can.fit_transform(cancer), columns=cancer.columns)
	  normal = pd.DataFrame(std_scaler_norm.fit_transform(normal), columns=normal.columns)

	  cancer.to_csv(r''+parent_dir+'/cancer/'+names[index]+'.txt.bz2',compression="bz2", sep='\t',header=None,index=None,index_label=None)
	  normal.to_csv(r''+parent_dir+'/normal/'+names[index]+'.txt.bz2',compression="bz2", sep='\t',header=None,index=None,index_label=None)
