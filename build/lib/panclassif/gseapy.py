import pandas as pd
import gseapy as gs
import os
import warnings





def gsea(homepath):


	'''
		Parameters
		----------
			`homepath` (str): 
			  Path where you want to save all the generated files 
			  and folders. 

		Return:
		-------
			None

		Outputs:
		--------
			Generate a directory names enrichr 
			within home directory and two plot 
			of gene enrichement analysis using 
			the selected genes from panclassif 
	'''
	warnings.filterwarnings("ignore")
	# Directory 
	directory = "enrichr"
	# Parent Directory path 
	parent_dir = homepath
	# Path 
	path = os.path.join(parent_dir, directory)
	if not os.path.exists(path):
		os.mkdir(path)
	gene = pd.read_csv(homepath+"/std_npy/unique_genes_with_frequency.csv",header=None)
	gl = []
	for g in range(len(gene)):
	  gl.append(gene[0][g])

	enr = gs.enrichr(gene_list=gl, description='Disease', 
		gene_sets='DisGeNET', outdir=homepath+'/enrichr')
	# simple plotting function
	from gseapy.plot import barplot, dotplot

	# to save your figure, make sure that ``ofname`` is not None
	barplot(enr.res2d,title='DisGeNET',cutoff=0.2,ofname=homepath+'/enrichr/DisGeNET_barplot.png')
	dotplot(enr.res2d, title='DisGeNET',cmap='viridis_r',cutoff=0.2,ofname=homepath+'/enrichr/DisGeNET_dotplot.png')