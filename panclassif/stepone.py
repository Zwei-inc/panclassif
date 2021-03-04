def step1(homepath,names):
	import numpy as np
	import pandas as pd
	from sklearn.feature_selection import SelectKBest, chi2 , f_classif,f_regression,mutual_info_classif,mutual_info_regression
	from sklearn.svm import SVR
	import warnings

	warnings.filterwarnings("ignore")

	"""# Frequency Check"""
	data = pd.read_csv(homepath+"/cancer/CHOL.csv.gz",header=None)
	one_col = data.iloc[:,0:1]
	one_col = one_col.drop(one_col.index[0])

	gene_frequency = []
	#reading data and doing work
	for index in range(len(names)):
	  DATA = np.load(homepath+"/std_npy/"+names[index]+".npy")
	  # print(DATA)
	  # print(DATA[0])
	  #print(len(DATA))
	  for i in range(len(DATA)):
	    if (DATA[i] != 0):
	      gene_frequency.append(one_col[0][DATA[i]])
	np.save(homepath+"/std_npy/gene_frequency",gene_frequency)