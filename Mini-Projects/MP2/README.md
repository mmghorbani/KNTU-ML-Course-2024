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
