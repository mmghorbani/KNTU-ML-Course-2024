# -*- coding: utf-8 -*-

"""ML_MP3_Q1(1-3)_Ghorbani.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1LF3GotCipD0iiKcuDwvnR43c1ZyMtVdb
"""

# Q1 (1-3)
# This notebook provides a comprehensive analysis of the Iris dataset, starting with data loading, exploration, and visualization using various techniques like pair plots, heatmaps, and t-SNE. It then proceeds to feature scaling and dimensionality reduction using StandardScaler, PCA, and LDA. The notebook includes the implementation of a Support Vector Machine (SVM) for classification, with performance evaluation using metrics such as accuracy and F1-score. Visualizations of decision boundaries and confusion matrices are also included to illustrate model performance.

# Part I


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sb
import imageio.v2 as iio
from cvxopt import matrix, solvers
from itertools import combinations

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.manifold import TSNE
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
from sklearn import svm
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score, f1_score
from sklearn.inspection import DecisionBoundaryDisplay

# Import dataset
iris = load_iris()
X = pd.DataFrame(data=iris.data, columns=iris.feature_names)
y = pd.DataFrame(data=iris.target, columns=['target'])
y['species'] = iris.target_names[iris.target]

iris = pd.concat([X,y['species']], axis=1)
iris

# Find missing values
X.isnull().sum()

# Statistical description
X.describe()

plt.rcParams['figure.figsize'] = (8, 5)
plt.rcParams['figure.dpi'] = 120

sb.pairplot(iris, palette='Blues', hue='species')

sb.heatmap(X.corr(), annot=True, cmap='Blues', linewidth=1);
plt.title('Correlation heatmap of Iris dataset');

sb.countplot(x="species", data=y, palette="Blues");
plt.title('Countplot of Iris dataset for each classes');

tsne = TSNE(n_components=2, random_state=24, verbose=0)
X_tsne = tsne.fit_transform(X)

sb.scatterplot(x=X_tsne[:, 0], y=X_tsne[:, 1], hue=y['species'], palette='Blues', edgecolor='k')
plt.title('t-SNE analyse of Iris dataset')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')

"""# Part II"""

x_train, x_test, y_train, y_test = train_test_split(X,y['target'], test_size=0.3, random_state=24, shuffle=True)
print(x_train.shape, x_test.shape, y_train.shape, y_test.shape)

scaler = StandardScaler()
scaler.fit(x_train)

x_train_standardized = scaler.transform(x_train)
x_test_standardized = scaler.transform(x_test)

print(np.mean(x_train_standardized), np.mean(x_test_standardized))
print(np.std(x_train_standardized), np.std(x_test_standardized))

pca = PCA(n_components=2, random_state=24)
pca.fit(x_train_standardized)
x_train_pca = pca.transform(x_train_standardized)
x_test_pca = pca.transform(x_test_standardized)
print(x_train_pca.shape, x_test_pca.shape)

sb.scatterplot(x=x_train_pca[:, 0], y=x_train_pca[:, 1], hue=y_train, palette='Blues', edgecolor='k')
plt.title('PCA analyse of Iris dataset')

lda = LDA(n_components=2)
lda.fit(x_train_standardized, y_train)
x_train_lda = lda.transform(x_train_standardized)
x_test_lda = lda.transform(x_test_standardized)
print(x_train_lda.shape, x_test_lda.shape)

sb.scatterplot(x=x_train_lda[:, 0], y=x_train_lda[:, 1], hue=y_train, palette='Blues', edgecolor='k')
plt.title('LDA analyse of Iris dataset')

# Define model
clf_linear_pca = svm.SVC(C=1, kernel='linear', random_state=24)

# Train model
clf_linear_pca.fit(x_train_pca, y_train)

# Prediction
y_pred_linear_pca = clf_linear_pca.predict(x_test_pca)

# Accuracy score
clf_linear_pca.score(x_test_pca, y_test)

ax = plt.gca()

DecisionBoundaryDisplay.from_estimator(
        clf_linear_pca,
        x_test_pca,
        response_method="predict",
        grid_resolution=1000,
        plot_method="pcolormesh",
        cmap='Blues',
        ax=ax,
)

plt.scatter(x=x_train_pca[:, 0], y=x_train_pca[:, 1], c=y_train, edgecolors='k', cmap='Blues')

ax.scatter(
    clf_linear_pca.support_vectors_[:, 0],
    clf_linear_pca.support_vectors_[:, 1],
    s=100,
    linewidth=1,
    facecolors="none",
    edgecolors="red",
)

plt.title('SVC(kernel = linear), PCA')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')

cm_pca = confusion_matrix(y_test, y_pred_linear_pca)
disp = ConfusionMatrixDisplay(confusion_matrix=cm_pca)
disp.plot(cmap='Blues')
plt.title('SVC(kernel = linear), PCA')

print('SVC(kernel = linear), PCA')
print(classification_report(y_test, y_pred_linear_pca))

# Define model
clf_linear_lda = svm.SVC(kernel='linear', random_state=24)

# Train model
clf_linear_lda.fit(x_train_lda, y_train)

# Prediction
y_pred_lda = clf_linear_lda.predict(x_test_lda)

# Accuracy score
clf_linear_lda.score(x_test_lda, y_test)

cm_lda = confusion_matrix(y_test, y_pred_lda)
disp = ConfusionMatrixDisplay(confusion_matrix=cm_lda)
disp.plot(cmap='Blues')
plt.title('SVC(kernel = linear), LDA')

print('SVC(kernel = linear), LDA')
print(classification_report(y_test, y_pred_lda))

ax = plt.gca()

DecisionBoundaryDisplay.from_estimator(
        clf_linear_lda,
        x_test_lda,
        response_method="predict",
        grid_resolution=1000,
        plot_method="pcolormesh",
        cmap='Blues',
        ax=ax,
        eps=4
)

plt.scatter(x=x_train_lda[:, 0], y=x_train_lda[:, 1], c=y_train, edgecolors='k', cmap='Blues')

ax.scatter(
    clf_linear_lda.support_vectors_[:, 0],
    clf_linear_lda.support_vectors_[:, 1],
    s=100,
    linewidth=1,
    facecolors="none",
    edgecolors="red",
)

plt.title('SVC(kernel = linear), LDA')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')

"""# Part III"""

images = []

for i in range(1,11):
  # Define the model
  clf_poly_lda = svm.SVC(kernel='poly', degree=i, C=0.5, random_state=24)

  # Train model
  clf_poly_lda.fit(x_train_lda, y_train)

  # Prediction
  y_pred_poly_lda = clf_poly_lda.predict(x_test_lda)

  # Print accuracy and f1-score
  print(f'Degree = {i}, accuracy = {accuracy_score(y_test,  y_pred_poly_lda)* 100:.2f}, f1-score = {f1_score(y_test,  y_pred_poly_lda, average="macro"):.2f}')

  # Plot decision boundary
  fig, ax = plt.figure() , plt.gca()

  DecisionBoundaryDisplay.from_estimator(
        clf_poly_lda,
        x_test_lda,
        response_method="auto",
        grid_resolution=1000,
        plot_method="pcolormesh",
        cmap='Blues',
        ax=ax,
        eps=4
  )

  plt.scatter(x=x_train_lda[:, 0], y=x_train_lda[:, 1], c=y_train, edgecolors='k', cmap='Blues')

  ax.scatter(
    clf_poly_lda.support_vectors_[:, 0],
    clf_poly_lda.support_vectors_[:, 1],
    s=100,
    linewidth=1,
    facecolors="none",
    edgecolors="red",
  )

  plt.title(f'SVC(kernel = poly, degree = {i}), LDA')
  plt.xlabel('Feature 1')
  plt.ylabel('Feature 2')

  plt.savefig(f'sklearn_poly_degree_{i}.png')
  images.append(iio.imread((f'sklearn_poly_degree_{i}.png')))
  plt.close('all')


iio.mimsave('sklearn_decision_boundries.gif', images, duration=1000, loop=0)
