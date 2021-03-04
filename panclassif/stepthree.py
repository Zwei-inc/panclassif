def step3(homepath):
  import numpy as np
  import pandas as pd
  import csv
  import random
  import warnings
  warnings.filterwarnings("ignore")

  # importing the unique m genes name
  unique_genes = np.load(homepath+"/std_npy/genes_that_willbe_filtered.npy")

  # reading and making a dictonary of counted numbers of genes based on their frequency
  with open(homepath+'/std_npy/unique_genes_with_frequency.csv', mode='r') as infile:
      reader = csv.reader(infile)
      gene_freq_dict = {rows[0]:rows[1] for rows in reader}

  selected_genes = []
  for gene in unique_genes:
    selected_genes.append(gene)
  np.save(homepath+"/std_npy/selected_genes", selected_genes)
