from .featSelect import featSelect
from .dataProcess import dataProcess
from .binarymerge import btrain, btest
from .multimerge import mtrain, mtest
from .upsampling_train_data import upsampled
from .models import classification

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
	Merge all the cancer samples as cancer `bin_cancer` and 
	normal samples as normal `bin_normal` for binary 
	classification without adding labels.
	"~/train_data"
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
	Merge all the cancer samples as cancer `bin_cancer` and 
	normal samples as normal `bin_normal` for binary 
	classification with labels added.
	"~/train_data"
	'''
	print("Merging for multiclass has started")
	mtrain(names,homepath)
	mtest(names,homepath)
	print("Merging for multiclass has ended")
	print()
