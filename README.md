# PanClassif: A machine learning classifier pipeline for [TCGA](https://www.cancer.gov/about-nci/organization/ccg/research/structural-genomics/tcga) pancancer classification

This is a complete machine learning pipeline package to work with TCGA cancer RNA-seq gene count data.

[PanClassif PyPi](https://pypi.org/project/panclassif/)



## Data prerequisition

* TCGA cancer & normal samples downloaded using TCGA2STAT 
* smoothed version of the above collected data using knn-smoothing ([Wagner et al., 2017](https://www.biorxiv.org/content/early/2018/04/09/217737)) 
* [Dataset Direct Download Click Here](https://data.mendeley.com/datasets/pr9j7x7nmh/1) 


## Functions
### featSelect(homepath, cancerpath, normalpath, k)
Params
* homepath : (str) 
    Path where you want to save all the generated files 
    and folders. 
* cancerpath : (str)  
    Path where all the cancer's cancer gene expression
    matrix are located.
* normalpath : (str)  
    Path where all the cancer's normal gene expression
    matrix are located.
* k : (int) 
    The number of top genes you want to choose per
    cancer. (default: k=5) you can not put k less than 5
----------
   
### dataProcess(homepath,names,cancerpath,smoothed_cancer,smoothed_normal,scale_mode)
Params
* homepath : (str)
	  Path where you want to save all the generated files 
	  and folders. 
* cancerpath : (str) 
	  Path where all the cancer's cancer gene expression
	  matrix are located.
* names : (list) 
	  List of the cancer names found from `featSelect`
	  function.
* smoothed_cancer : (str) 
	  Path where all the cancer's smoothed cancer gene expression
	  matrix are located.
* smoothed_normal : (str) 
	  Path where all the cancer's smoothed normal gene expression
	  matrix are located.
* scale_mode (int):
        Here (0 is for Standardization and 1 for normalization) for data scalling
----------


### upsampled(names, homepath)
### binary_merge(names, homepath)
### multi_merge(names, homepath)
Params
* names : (list) 
	  List of the cancer names found from `featSelect`
	  function.
* homepath : (str)  
	  Path where you want to save all the generated files 
	  and folders.
----------

### classification(homepath, classifier, mode, save_model)
Params
* homepath : (str)
      Path where you want to save all the generated files 
      and folders 
* classifer : (sklearn's classification model) 
      Provide the classification model's instance you want 
      to use. For example: RandomForestClassifier(n_estimators=100).
* Or, classifer : (str) 
      If you want to use "Neural Network" then just type 
      "NN". For example: classifier = "NN"
* mode : (str) 
      There is two mode 1) binary 2) multi. Use "binary" 
      for binary classification &  "multi" for multiclass 
      classification. (default: mode = "binary")
* save_model : (str) 
      Optional parameter. Use it only if you want to save 
      the model. For example: save_model = "your_model_name"
----------

### gsea(homepath)
* homepath : (str)
      Path where you want to save all the generated files 
      and folders 
----------
  
## Example
----------
```txt
homepath = '/home'
cancerpath = '/home/cancer/'
normalpath = '/home/normal/'

smoothed_cancer = '/home/smoothed_cancer'
smoothed_normal = '/home/smoothed_normal'

```



### Data Load and Process Phase
```python
import panclassif as pc 
#You have to follow below order to work the code properly 
names = pc.featSelect(homepath,cancerpath,normalpath, k=5)
pc.dataProcess(homepath,names,cancerpath,smoothed_cancer,smoothed_normal)
pc.upsampled(names, homepath)
pc.binary_merge(names, homepath)
pc.multi_merge(names, homepath)
```

### Classification Phase

```python
from sklearn.ensemble import RandomForestClassifier
pc.classification(homepath, RandomForestClassifier(n_estimators=100), mode="multi", save_model="RF")
```

### Gene enrichment check

```python
pc.gsea(homepath)
```
    

