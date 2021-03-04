def step4(homepath,cancerpath,smoothed):
	import numpy as np
	import pandas as pd
	import csv
	import random

	import os
	from os import listdir
	from os.path import isfile, join
	import warnings
	warnings.filterwarnings("ignore")

	cancerfiles = [f for f in listdir(cancerpath) if isfile(join(cancerpath, f))]
	smoothedfiles = [f for f in listdir(smoothed) if isfile(join(smoothed, f))]

	selected_genes = np.load(homepath+"/std_npy/selected_genes.npy")
	data = pd.read_csv(cancerpath+'/'+cancerfiles[0],header=None)
	header_gene_names =  data.iloc[:,0:1]
	header_gene_names = header_gene_names.drop(header_gene_names.index[0])
	header_gene_names.reset_index(drop=True, inplace=True)
	data_read = pd.read_csv(smoothed+'/'+smoothedfiles[0],header=None, delimiter = '\t')
	frame0 = [data_read,header_gene_names]
	data_cancer_early = pd.concat(frame0, axis = 1)
	data_cancer_early = data_cancer_early.T
	data_cancer_early.reset_index(drop=True, inplace=True)


	cols_exist = []
	cols_to_del = []

	# selecting the genes that we need from "selected genes"
	for i in range(20501):
		for j in range(len(selected_genes)):
			if(data_cancer_early[i][len(data_read.columns)] == selected_genes[j]):
				cols_exist.append(i)

	# selecting the genes that we need to drop from "cols_to_exist"
	for i in range(20501):
		if(i not in cols_exist):
			cols_to_del.append(i)
	# saving the genes that we need to drop
	np.save(homepath+"/std_npy/genes_to_del",cols_to_del)