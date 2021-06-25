def featSelect(homepath,cancerpath,normalpath,k=5):

  '''
  Parameters
  ----------
    `homepath` (str): 
      Path where you want to save all the generated files 
      and folders. 
    `cancerpath` (str): 
      Path where all the cancer's cancer gene expression
      matrix are located.
    `normalpath` (str): 
      Path where all the cancer's normal gene expression
      matrix are located.
    `k` (int): 
      The number of top genes you want to choose per
      cancer. (default: k=5) you can not put k less than 5

  Return:
  -------
    `names` (list):
      Name of cancers found in `cancerpath`.

  Outputs:
  --------
    Creates a folder named "~/std_npy" and all the top `k`
    genes from each cancer type is saved as npy file. 
  '''

  import numpy as np
  import pandas as pd
  from sklearn.feature_selection import SelectKBest, chi2 , f_classif,f_regression,mutual_info_classif,mutual_info_regression
  from sklearn.svm import SVR
  import os
  from os import listdir
  from os.path import isfile, join
  import warnings
  if(k<5):
    k=5
  warnings.filterwarnings("ignore")
  cancerfiles = [f for f in listdir(cancerpath) if isfile(join(cancerpath, f))]
  normalfiles = [f for f in listdir(normalpath) if isfile(join(normalpath, f))]
  names = []

  for f in cancerfiles:
    s = f.split('.')
    names.append(s[0])

  list.sort(cancerfiles)
  list.sort(normalfiles)
  list.sort(names)

  # Directory 
  directory = "std_npy"
  # Parent Directory path 
  parent_dir = homepath
  # Path 
  path = os.path.join(parent_dir, directory) 
  if not os.path.exists(path):
    os.mkdir(path)

  print("Feature selection process is running...")
  #reading data and doing work
  for index in range(len(cancerfiles)):
    Cancer = pd.read_csv(cancerpath+'/'+cancerfiles[index], header=None, index_col=None)
    Normal = pd.read_csv(normalpath+'/'+normalfiles[index], header=None, index_col=None) 

    #droping sample headers
    Cancer = Cancer.drop(Cancer.index[0])
    Cancer = Cancer.drop(columns=[0])
    Normal = Normal.drop(Normal.index[0])
    Normal = Normal.drop(columns=[0])
    #transpose
    Cancer_T = Cancer.T
    Normal_T = Normal.T

    #setting target
    Cancer_T["20501"] = 1.0
    Normal_T["20501"] = 0.0

    Cancer_T = Cancer_T.T
    Normal_T = Normal_T.T

    Cancer_T = Cancer_T.reset_index(drop=True)
    Normal_T = Normal_T.reset_index(drop=True)

    Cancer_T = Cancer_T.T
    Normal_T = Normal_T.T
    #dropping row
    Normal_T = Normal_T.drop(Normal_T.index[0])

    #concating
    X = pd.concat((Cancer_T,Normal_T),axis=0)
    x = X.iloc[:,:20501]
    y = X.iloc[:,20501]

    print(f'Doing feature selection for {names[index]}')
    #Anova test
    selector = SelectKBest(f_classif, k=k)
    selector.fit(x, y)
    cols_anova = selector.get_support(indices=True)
    np.save(homepath+"/std_npy/"+names[index],cols_anova)
  print("Feature selection process has ended")
  print()
  return names