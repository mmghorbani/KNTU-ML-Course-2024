## Question 1
Implementation of a two-layer artificial neural network with McCulloch-Pitts neurons for multi-class classification. The network utilizes three distinct activation functions: sigmoid, ReLU (Rectified Linear Unit), and ELU (Exponential Linear Unit).

- The notebook defines mathematical functions for sigmoid, ReLU, and ELU activations, along with their derivatives.
- It implements the McCulloch-Pitts neuron class with functionalities for step, sign, and ReLU activation functions.
- Two multi-class classification models are built using the defined neurons:
  - Model 1: Uses a step function as the activation function in both layers.
  - Model 2: Employs a sign function in the first layer and ReLU in the second layer.
- The notebook visualizes the decision boundaries achieved by both models using randomly generated data points.

## Question 2
This Python notebook investigates the effectiveness of a multilayer perceptron (MLP) network for classifying faults in bearings. The system leverages features extracted from vibration data acquired from the CWRU-bearing dataset. The notebook compares the performance of the MLP network using different optimization algorithms and loss functions.

- The data is preprocessed by extracting features like mean, standard deviation, and root mean square (RMS) from the vibration time series.
- Two MLP models are trained and evaluated:
  - Model 1: Uses Adam optimizer and sparse categorical cross-entropy loss.
  - Model 2: Uses SGD optimizer and Kullback-Leibler divergence loss.
- K-Fold cross-validation is employed to assess the generalizability of the models.


## Question 2

This notebook investigates the application of decision trees and random forest classifiers for a drug classification task using the Drug dataset from Kaggle. The notebook provides insights into how pre-pruning, post-pruning, undersampling, and hyperparameter tuning can influence the performance and complexity of decision trees and random forests for drug classification.

- The notebook utilizes the Drug dataset from Kaggle for drug classification.
- Preprocessing includes data cleaning, feature engineering, and undersampling to handle class imbalance.
- Decision tree models are trained with different hyperparameters for pre-pruning, post-pruning, and default settings.
- Decision tree structures are visualized to understand their decision-making processes.
- The performance of decision trees is evaluated using classification reports.
- A random forest model is trained with default hyperparameters and evaluated on the test set.
- This investigation allows for comparing the impact of different approaches on the performance of decision trees and random forests in this drug classification task.



