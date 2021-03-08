from .featSelect import featSelect
from .dataProcess import dataProcess
from .binarymerge import btrain, btest
from .multimerge import mtrain, mtest
from .upsampling_train_data import upsampled
from .models import classification
from .gseapy import gsea

def __init__(self):
	'''
	Functions:
	----------
	`featSelect`: 
	  Use for feature selection from data. 
	`dataProcess`: 
	  Use for processing the data.
	`upsampled`: 
	  Use for upsampling train data.
	`binarymerger`: 
	  Merging data for binary classification.
	`multimerger`: 
	  Merging data for multiclass classification.
	`classification`: 
	  Use for performing classification.
	'''
	print("panclassif succesfully imported")

def binary_merge(names,homepath):
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
	Merge all the cancer and normal samples 
	and generate one bin_cancer file for train 
	data and one for test data. Similarly one 
	bin_normal for train data and one for test 
	data
	'''
	print("Merging for binary has started")
	btrain(names,homepath)
	btest(names,homepath)
	print("Merging for binary has ended")
	print()


def multi_merge(names,homepath):
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
	Merge all the cancer and normal samples 
	and generate one mul_cancer file for train 
	data and one for test data. Similarly one 
	mul_normal for train data and one for test 
	data
	'''
	print("Merging for multiclass has started")
	mtrain(names,homepath)
	mtest(names,homepath)
	print("Merging for multiclass has ended")
	print()
