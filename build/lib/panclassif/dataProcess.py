from .stepone import step1
from .steptwo import step2
from .stepthree import step3
from .stepfour import step4
from .stepfive import step5
from .test_train_split import splitCancer, splitNormal

def dataProcess(homepath,names,cancerpath,smoothed_cancer,smoothed_normal):
	'''
	Parameters
	----------
	`homepath` (str): 
	  Path where you want to save all the generated files 
	  and folders. 
	`cancerpath` (str): 
	  Path where all the cancer's cancer gene expression
	  matrix are located.
	`names` (list): 
	  List of the cancer names found from `featSelect`
	  function.
	`smoothed_cancer` (str): 
	  Path where all the cancer's smoothed cancer gene expression
	  matrix are located.
	`smoothed_normal` (str): 
	  Path where all the cancer's smoothed normal gene expression
	  matrix are located.

	Return:
	-------
	None

	Outputs:
	--------
	Split the treated data into train and test. train datas
	are saved in "~/pre_upsample_train_data" and test datas
	are save in "~/test_data". Unique genes name are saved
	in "~/std_npy" folder as "unique_genes_with_frequency.csv" 
	with their respective frequency.
	'''

	print("Data process is running")
	step1(homepath,names)
	step2(homepath)
	step3(homepath)
	step4(homepath,cancerpath,smoothed_cancer)
	step5(homepath,names,smoothed_cancer,smoothed_normal)
	splitCancer(homepath,names)
	splitNormal(homepath,names)
	print("Data process has ended")
	print()


