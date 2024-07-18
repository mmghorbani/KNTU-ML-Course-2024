# Mini-Project 2

![ML-MP2-Ghorbani](https://github.com/mmghorbani/KNTU-ML-Course-2024/assets/162275285/73eaf7a8-2424-481e-af4d-fd9857d6024c)



## Question 1
- `ML_MP2_Q1_Ghorbani.py` [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1W3V4FlpTqhgof4tHiL3nXUJyjlDR2ykU?usp=drive_link)

Implementation of a two-layer artificial neural network with McCulloch-Pitts neurons for multi-class classification. The network utilizes three distinct activation functions: sigmoid, ReLU (Rectified Linear Unit), and ELU (Exponential Linear Unit).

- The notebook defines mathematical functions for sigmoid, ReLU, and ELU activations, along with their derivatives.
- It implements the McCulloch-Pitts neuron class with functionalities for step, sign, and ReLU activation functions.
- Two multi-class classification models are built using the defined neurons:
  - Model 1: Uses a step function as the activation function in both layers.
  - Model 2: Employs a sign function in the first layer and ReLU in the second layer.
- The notebook visualizes the decision boundaries achieved by both models using randomly generated data points.

#### Plots
![q1-3-4](https://github.com/mmghorbani/KNTU-ML-Course-2024/assets/162275285/f9ca6cc1-0f8b-4765-8d6b-a25dc9993622)
![q1-3-3](https://github.com/mmghorbani/KNTU-ML-Course-2024/assets/162275285/3bdbad1f-b6ba-4c04-9618-61f59a048215)


## Question 2
- `ML_MP2_Q2_Ghorbani.py` [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1sBepl3-NRet544HM2toOAl3yAZi1rJ5c?usp=drive_link)

This Python notebook investigates the effectiveness of a multilayer perceptron (MLP) network for classifying faults in bearings. The system leverages features extracted from vibration data acquired from the CWRU-bearing dataset. The notebook compares the performance of the MLP network using different optimization algorithms and loss functions.

- The data is preprocessed by extracting features like mean, standard deviation, and root mean square (RMS) from the vibration time series.
- Two MLP models are trained and evaluated:
  - Model 1: Uses Adam optimizer and sparse categorical cross-entropy loss.
  - Model 2: Uses SGD optimizer and Kullback-Leibler divergence loss.
- K-Fold cross-validation is employed to assess the generalizability of the models.

#### Plots
![q2-2-2](https://github.com/mmghorbani/KNTU-ML-Course-2024/assets/162275285/0e742886-22d1-4cfd-a3ff-1cb3e30f0a7f)
![q2-2-1](https://github.com/mmghorbani/KNTU-ML-Course-2024/assets/162275285/1a007056-126b-4235-84dc-fe6b43132576)

## Question 3
- `ML_MP2_Q3_Ghorbani.py` [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1ATP2DiY-0AwiAb0O7BaQXRfB7jmCTZv4?usp=drive_link)

This notebook investigates the application of decision trees and random forest classifiers for a drug classification task using the Drug dataset from Kaggle. The notebook provides insights into how pre-pruning, post-pruning, undersampling, and hyperparameter tuning can influence the performance and complexity of decision trees and random forests for drug classification.

- The notebook utilizes the Drug dataset from Kaggle for drug classification.
- Preprocessing includes data cleaning, feature engineering, and undersampling to handle class imbalance.
- Decision tree models are trained with different hyperparameters for pre-pruning, post-pruning, and default settings.
- Decision tree structures are visualized to understand their decision-making processes.
- The performance of decision trees is evaluated using classification reports.
- A random forest model is trained with default hyperparameters and evaluated on the test set.
- This investigation allows for comparing the impact of different approaches on the performance of decision trees and random forests in this drug classification task.

#### Plot
![q3-2-5](https://github.com/mmghorbani/KNTU-ML-Course-2024/assets/162275285/b8f4cfa8-887f-45e4-ab14-16c61316e3b2)

## Question 4
- `ML_MP2_Q4_Ghorbani.py` [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1b_exw6kJZ943Tmcta3FEmUbO29lLrAYd?usp=drive_link)

This Jupyter Notebook implements a Naive Bayes classifier on the Heart Disease Dataset to predict the presence of heart disease in patients. It covers data loading, preprocessing (shuffling, splitting, normalization), model training with GaussianNB, evaluation (accuracy score, classification report, confusion matrix), and an example of random prediction.

#### Plot
![q4-6](https://github.com/mmghorbani/KNTU-ML-Course-2024/assets/162275285/03c944a5-d425-451a-b60d-680754e0307d)
