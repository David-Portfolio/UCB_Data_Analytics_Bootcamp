The purpose of this project is to use machine learning techniques to support future funding decisions from Alphabet Soup. The provided csv file aggregating over 34,000 organizations that have previously received funding is the data source for our deep learning model. After pre-processing the data, optimizing and running the model, we have achieved target performance of 75% accuracy. To increase model performance, we reduced the noise from the dataset by dropping uneeded columns, binning and subset filtering identified useful variables, then applying one-hot encoding. Subsequently, the numerical variables were split into features/target arrays, training/testing datasets, and standardized/scaled prior to defining the Keras model. The selected layer details and accuracy graph for reference:

* Layer 1: 20 neurons
* Layer 2: 15 neurons
* Layer 3: 10 neurons
* Layer 4: 5 neurons
* Layer 5: 1 neurons

<img width="222" alt="Model Accuracy" src="https://user-images.githubusercontent.com/65242270/93688318-ca492700-fa79-11ea-84f8-63b102f8ebac.PNG">

*Note: it is assumed that for column "IS_SUCCESSFUL" that "0" = "N" and "1" = "Y", and for column "STATUS" that "0" = "Not Active" and "1" = "Active".
