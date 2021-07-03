from sklearn.metrics import confusion_matrix, classification_report
from matplotlib.colors import LinearSegmentedColormap
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.pyplot import figure
import os
import warnings
warnings.filterwarnings("ignore")
def heatconmat(y_true, y_pred, homepath, mode="binary"):
  cmap_reds = plt.get_cmap("Reds")
  num_colors = 50
  colors = ["white", "grey"] + [cmap_reds(i / num_colors) for i in range(2, num_colors)]
  cmap2 = LinearSegmentedColormap.from_list('', colors, num_colors)
  sns.set_context('talk')
  df = pd.Series(y_true)
  if(mode == "binary"):
    plt.figure(figsize=(4,4))
  else:  
    plt.figure(figsize=(18,12))
  data = confusion_matrix(df,y_pred)
  sns.heatmap(data,
              annot=True,
              fmt='d',
              vmin=0, vmax=num_colors,
              cbar=False,
              # mask = data <= 0,
              #cmap='gist_earth_r',
              cmap=cmap2,
              yticklabels=sorted(df.unique()))
  plt.show()

  # plt.imshow(data, interpolation='none')
  # plt.colorbar()
  # plt.xticks(sorted(df.unique()),fontsize=12)
  # plt.yticks(sorted(df.unique()),fontsize=12)
  # plt.grid(True)
  # plt.show()
  print(classification_report(df,y_pred))
  # Directory 
  directory = "plots"
  # Parent Directory path 
  parent_dir = homepath
  # Path 
  path = os.path.join(parent_dir, directory) 
  if not os.path.exists(path):
    os.mkdir(path)
  plt.savefig(homepath+"/plots/plot.png")
  


def classification(homepath, classifier, mode="binary", save_model=""):

  '''
  Parameters
  ----------
    `homepath` (str): 
      Path where you want to save all the generated files 
      and folders 
    `classifer` (sklearn's classification model): 
      Provide the classification model's instance you want 
      to use. For example: RandomForestClassifier(n_estimators=100).
    `classifer` (str): 
      If you want to use "Neural Network" then just type 
      "NN". For example: classifier = "NN"
    `mode` (str): 
      There is two mode 1) binary 2) multi. Use "binary" 
      for binary classification &  "multi" for multiclass 
      classification. (default: mode = "binary")
    `save_model` (str): 
      Optional parameter. Use it only if you want to save 
      the model. For example: save_model = "your_model_name"

  Return:
  -------
    None

  Outputs:
  --------
    Classification report such as precision, recall, f1-score, mcc, accuracy. 
    Confusion matrix as plot saved in ~/plots/plot.png. Models saved in 
    ~/models/your_model_name.sav or ~/models/your_model_name.h5  
  '''

  if(mode == "binary"):
    import io
    import numpy as np
    import pandas as pd
    from sklearn.metrics import matthews_corrcoef
    import os
    import joblib
    import tensorflow as tf
    # from keras.models import Sequential
    # from keras.layers import Dense


    #train data load
    Cancer = pd.read_csv(homepath+"/train_data/bin_Cancer.txt.bz2",header=None, delimiter = "\t")
    Normal = pd.read_csv(homepath+"/train_data/bin_Normal.txt.bz2",header=None, delimiter = "\t")
    Cancer['Target'] = 1
    Normal['Target'] = 0
    #Normal = Normal.drop(Normal.index[0])
    frame = [Cancer,Normal]
    Data = pd.concat(frame,axis=0)
    X_train = Data.iloc[:,:len(Data.columns)-1]
    y_train = Data.iloc[:,len(Data.columns)-1]

    #test data load
    Cancer = pd.read_csv(homepath+"/test_data/bin_Cancer.txt.bz2",header=None, delimiter = "\t")
    Normal = pd.read_csv(homepath+"/test_data/bin_Normal.txt.bz2",header=None, delimiter = "\t")
    Cancer['Target'] = 1
    Normal['Target'] = 0
    #Normal = Normal.drop(Normal.index[0])
    frame = [Cancer,Normal]
    Data = pd.concat(frame,axis=0)
    Data = Data.drop(Data.index[0])
    X_test = Data.iloc[:,:len(Data.columns)-1]
    y_test = Data.iloc[:,len(Data.columns)-1]

    if(type(classifier) != str ):
      clf = classifier
      clf.fit(X_train, y_train)
      y_pred = clf.predict(X_test)

      heatconmat(y_test, y_pred, homepath, mode)
      print("MCC Score: ",matthews_corrcoef(y_test, y_pred))

      if(len(save_model) != 0):
        # Directory 
        directory = "model_save"
        # Parent Directory path 
        parent_dir = homepath
        # Path 
        path = os.path.join(parent_dir, directory) 
        if not os.path.exists(path):
          os.mkdir(path)
        joblib.dump(clf, homepath+"/model_save/"+save_model+"_"+mode+".sav")

    elif(type(classifier) == str and classifier == "NN"):
      # define the keras model
      model = tf.keras.Sequential()
      model.add(tf.keras.layers.Dense(1024, input_dim=len(Data.columns)-1, activation='relu'))
      model.add(tf.keras.layers.Dense(512, activation='relu'))
      model.add(tf.keras.layers.Dense(256, activation='relu'))
      model.add(tf.keras.layers.Dense(128, activation='relu'))
      model.add(tf.keras.layers.Dense(64, activation='relu'))
      model.add(tf.keras.layers.Dense(32, activation='relu'))
      model.add(tf.keras.layers.Dense(1, activation='sigmoid'))
      # compile the keras model
      model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
      # fit the keras model on the dataset
      model.fit(X_train, y_train, epochs=100, batch_size=100)
      y_pred = model.predict_classes(X_test)
      y_pred_seris = pd.Series(y_pred.flatten())

      heatconmat(y_test, y_pred_seris, homepath, mode)
      print("MCC Score: ",matthews_corrcoef(y_test, y_pred))

      if(len(save_model) != 0):
        # Directory 
        directory = "model_save"
        # Parent Directory path 
        parent_dir = homepath
        # Path 
        path = os.path.join(parent_dir, directory) 
        if not os.path.exists(path):
          os.mkdir(path)
        model.save(homepath+"/model_save/"+save_model+"_"+mode+".h5")

    else:
      print("classifier error. please check your 'classifier' parameter")
      return



  elif(mode == "multi"):
    import io
    import numpy as np
    import pandas as pd
    from sklearn.metrics import matthews_corrcoef
    import os
    import joblib
    from keras.models import Sequential
    from keras.layers import Dense
    from sklearn.preprocessing import LabelEncoder
    from keras.utils import np_utils
    import tensorflow as tf

    #train load
    Cancer = pd.read_csv(homepath+"/train_data/mul_Cancer.txt.bz2",header=None, delimiter = "\t")
    Normal = pd.read_csv(homepath+"/train_data/mul_Normal.txt.bz2",header=None, delimiter = "\t")
    Normal = Normal.drop(Normal.index[0])
    frame = [Cancer,Normal]
    Data = pd.concat(frame,axis=0)
    Data = Data.drop(Data.index[0])
    #print(Data)
    X_train = Data.iloc[:,:len(Data.columns)-1]
    y_train = Data.iloc[:,len(Data.columns)-1]
    # print(x)
    # print(Y)

    #test load
    Cancer = pd.read_csv(homepath+"/test_data/mul_Cancer.txt.bz2",header=None, delimiter = "\t")
    Normal = pd.read_csv(homepath+"/test_data/mul_Normal.txt.bz2",header=None, delimiter = "\t")
    Normal = Normal.drop(Normal.index[0])
    frame = [Cancer,Normal]
    Data = pd.concat(frame,axis=0)
    Data = Data.drop(Data.index[0])
    #print(Data)
    X_test = Data.iloc[:,:len(Data.columns)-1]
    y_test = Data.iloc[:,len(Data.columns)-1]
    # print(x)
    # print(Y)

    if(type(classifier) != str ):
      clf = classifier
      clf.fit(X_train, y_train)
      y_pred = clf.predict(X_test)

      heatconmat(y_test, y_pred, homepath, mode)
      print("MCC Score: ",matthews_corrcoef(y_test, y_pred))

      if(len(save_model) != 0):
        # Directory 
        directory = "model_save"
        # Parent Directory path 
        parent_dir = homepath
        # Path 
        path = os.path.join(parent_dir, directory) 
        if not os.path.exists(path):
          os.mkdir(path)
        joblib.dump(clf, homepath+"/model_save/"+save_model+"_"+mode+".sav")

    elif(type(classifier) == str and classifier == "NN"):
      # encode class values as integers
      encoder = LabelEncoder()
      encoder.fit(y_train)
      encoded_Y = encoder.transform(y_train)
      # convert integers to dummy variables (i.e. one hot encoded)
      y_train = np_utils.to_categorical(encoded_Y)

      encoder = LabelEncoder()
      encoder.fit(y_test)
      y_test = encoder.transform(y_test)

      # define baseline model
      model = tf.keras.Sequential()
      model.add(tf.keras.layers.Dense(1024, input_dim=len(Data.columns)-1, activation='relu'))
      model.add(tf.keras.layers.Dense(512, activation='relu'))
      model.add(tf.keras.layers.Dense(256, activation='relu'))
      model.add(tf.keras.layers.Dense(128, activation='relu'))
      model.add(tf.keras.layers.Dense(64, activation='relu'))
      model.add(tf.keras.layers.Dense(32, activation='relu'))
      model.add(tf.keras.layers.Dense(23, activation='softmax'))
      # compile the keras model
      model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
      # fit the keras model on the dataset
      model.fit(X_train, y_train, epochs=100, batch_size=100)
      y_pred = model.predict_classes(X_test)

      heatconmat(y_test, y_pred, homepath, mode)
      print("MCC Score: ",matthews_corrcoef(y_test, y_pred))

      if(len(save_model) != 0):
        # Directory 
        directory = "model_save"
        # Parent Directory path 
        parent_dir = homepath
        # Path 
        path = os.path.join(parent_dir, directory) 
        if not os.path.exists(path):
          os.mkdir(path)
        model.save(homepath+"/model_save/"+save_model+"_"+mode+".h5")
    
    else:
      print("classifier error. please check your 'classifier' parameter")
      return