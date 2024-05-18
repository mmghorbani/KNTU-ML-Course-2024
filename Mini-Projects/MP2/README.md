## Question 1
Implements a simple Multi-layer Perceptron (MLP) for a multi-class classification problem. The MLP consists of two layers of McCulloch-Pitts neurons with different activation functions. The code explores the use of step, sign, and ReLU activation functions and visualizes the decision boundaries for each combination.

## Question 2
This Python notebook investigates the effectiveness of a multilayer perceptron (MLP) network for classifying faults in bearings. The system leverages features extracted from vibration data acquired from the CWRU-bearing dataset. The notebook compares the performance of the MLP network using different optimization algorithms and loss functions.

_ The data is preprocessed by extracting features like mean, standard deviation, and root mean square (RMS) from the vibration time series.
_ Two MLP models are trained and evaluated:
  _ Model 1: Uses Adam optimizer and sparse categorical cross-entropy loss.
  _ Model 2: Uses SGD optimizer and Kullback-Leibler divergence loss.
_ K-Fold cross-validation is employed to assess the generalizability of the models.
