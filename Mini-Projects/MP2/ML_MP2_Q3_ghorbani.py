# -*- coding: utf-8 -*-
"""ML_MP2_Q3_Ghorbani.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ATP2DiY-0AwiAb0O7BaQXRfB7jmCTZv4

# Q3
Design [Decsion tree](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html) and [Random forest](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html) classifiers for [Drug dataset](https://www.kaggle.com/datasets/pablomgomez21/drugs-a-b-c-x-y-for-decision-trees). Apply pre-pruning and post-pruning techniques to prevent overfitting in decision trees. Additionally, use undersampling to balance the datase.

# Part 0

''' A) Import '''

# Import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn import tree
from sklearn.metrics import classification_report, accuracy_score
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from sklearn.ensemble import RandomForestClassifier

from imblearn.under_sampling import RandomUnderSampler

# Import datasets as .csv
!pip install --upgrade --no-cach-dir gdown
! gdown 1yVfZrzan3vuG7Gg37k7JQjkpkDdhV8AK

"""B) Preprocessing data"""

# Load dataset from files
dataset = pd.read_csv('/content/drug200.csv')
pd.DataFrame(dataset).head()

# Rename features and values for better understaning
dataset.rename(columns={'Na_to_K': 'Sodium_to_Potassium' , 'BP' : 'Blood_Pressure'}, inplace=True)
dataset['Sex'].replace({'M': 'Male', 'F': 'Female'}, inplace=True)
dataset['Drug'].replace({'drugA': 'A', 'drugB': 'B', 'drugC':'C', 'drugX':'X', 'drugY':'Y'}, inplace=True)
dataset['Sodium_to_Potassium'] = dataset['Sodium_to_Potassium'].round(0)
dataset['Sodium_to_Potassium'] = dataset['Sodium_to_Potassium'].astype('int')
dataset.head()

# Check missing values
dataset.info()

# Plot histplot and coutplot of features and targets
plt.rcParams["figure.figsize"] = (20, 18)

plt.subplot(3, 3, 1)
sns.countplot(x='Sex', data=dataset, palette='viridis', hue='Sex');
plt.title('Countplot of Sex')

plt.subplot(3, 3, 2)
sns.countplot(x='Blood_Pressure', data=dataset, palette='viridis', hue='Blood_Pressure');
plt.title('Countplot of Blood_Pressure')

plt.subplot(3, 3, 3)  # Corrected subplot position
sns.countplot(x='Cholesterol', data=dataset, palette='viridis', hue='Cholesterol');
plt.title('Countplot of Cholesterol')

plt.subplot(3,3,4)
sns.histplot(x='Age', data=dataset, palette='viridis', hue='Age', legend=False);
plt.title('Histplot of Age')

plt.subplot(3,3,5)
sns.histplot(x='Sodium_to_Potassium', data=dataset, palette='viridis', hue='Sodium_to_Potassium', legend=False);
plt.title('Histplot of Sodium_to_Potassium')

plt.subplot(3,3,6)
sns.countplot(x='Drug', data=dataset, palette='viridis', hue='Drug');
plt.title('Countplot of Drug(Targets)')
plt.show();

# Use label encoding to convert categorical features into numerical
cols = ['Sex', 'Blood_Pressure', 'Cholesterol']
dataset[cols] = dataset[cols].apply(LabelEncoder().fit_transform)
dataset.head()

# Understand assigned numbers to each value for all features
plt.rcParams["figure.figsize"] = (20, 18)

plt.subplot(3, 3, 1)
sns.countplot(x='Sex', data=dataset, palette='viridis', hue='Sex');
plt.title('Countplot of Sex')

plt.subplot(3, 3, 2)
sns.countplot(x='Blood_Pressure', data=dataset, palette='viridis', hue='Blood_Pressure');
plt.title('Countplot of Blood_Pressure')

plt.subplot(3, 3, 3)
sns.countplot(x='Cholesterol', data=dataset, palette='viridis', hue='Cholesterol');
plt.title('Countplot of Cholesterol')

plt.subplot(3,3,4)
sns.histplot(x='Age', data=dataset, palette='viridis', hue='Age', legend=False);
plt.title('Histplot of Age')

plt.subplot(3,3,5)
sns.histplot(x='Sodium_to_Potassium', data=dataset, palette='viridis', hue='Sodium_to_Potassium', legend=False);
plt.title('Histplot of Sodium_to_Potassium')

plt.subplot(3,3,6)
sns.countplot(x='Drug', data=dataset, palette='viridis', hue='Drug');
plt.title('Countplot of Drug(Targets)')

plt.show();

"""# Part I & II"""

""" A) Extract Train and Target data """


X = dataset.drop(["Drug"], axis = 1)
y = dataset["Drug"]
print(X.shape, y.shape)

"""B) Split data to Train and Test"""

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=24)
print(x_train.shape, y_train.shape, x_test.shape, y_test.shape)

# Under Sampling
sub = RandomUnderSampler(
    sampling_strategy='all',
    random_state=24,
    replacement=False
    )

x_sub, y_sub = sub.fit_resample(x_train, y_train)
print(x_sub.shape, y_sub.shape)

plt.figure(figsize=(8,4))
sns.countplot(data=y_sub, palette='viridis');
plt.title('Countplot of Drug(Targets) training set after Under-sampling')

# Cheack correlation of each data set
plt.rcParams["figure.figsize"] = (8, 4)
plt.subplot(1,2,1)
sns.histplot(x_train['Sodium_to_Potassium'])
plt.title('Distribution of training set')

plt.subplot(1,2,2)
sns.histplot(x_test['Sodium_to_Potassium'])
plt.title('Distribution of test set')

"""C) Design classifier"""

# Define classifier
clf = tree.DecisionTreeClassifier(
    criterion='gini',
    random_state=24,
    max_depth=None,
    max_leaf_nodes=None,
    ccp_alpha=0,
    )

# Train on original dataset
clf.fit(x_train, y_train)

# Plot decision tree
plt.figure(figsize=(15, 8))
tree.plot_tree(
    clf,
    class_names=np.unique(y_train),
    feature_names=x_train.columns,
    node_ids=True,
    rounded=True,
    filled=True
    );
plt.title('Decision tree structure trained by original dataset')


# Understand decision tree structure
n_nodes = clf.tree_.node_count
children_left = clf.tree_.children_left
children_right = clf.tree_.children_right
feature = clf.tree_.feature
threshold = clf.tree_.threshold
values = clf.tree_.value

node_depth = np.zeros(shape=n_nodes, dtype=np.int64)
is_leaves = np.zeros(shape=n_nodes, dtype=bool)
stack = [(0, 0)]  # start with the root node id (0) and its depth (0)
while len(stack) > 0:
    # `pop` ensures each node is only visited once
    node_id, depth = stack.pop()
    node_depth[node_id] = depth

    # If the left and right child of a node is not the same we have a split
    # node
    is_split_node = children_left[node_id] != children_right[node_id]
    # If a split node, append left and right children and depth to `stack`
    # so we can loop through them
    if is_split_node:
        stack.append((children_left[node_id], depth + 1))
        stack.append((children_right[node_id], depth + 1))
    else:
        is_leaves[node_id] = True

print(
    "Decision tree structure trained by original dataset \n"
    "The tree structure has {n} nodes and has "
    "the following tree structure:\n".format(n=n_nodes)
)
for i in range(n_nodes):
    if is_leaves[i]:
        print(
            "{space}node={node} is a leaf node with value={value}.".format(
                space=node_depth[i] * "\t", node=i, value=values[i]
            )
        )
    else:
        print(
            "{space}node={node} is a split node with value={value}: "
            "go to node {left} if X[:, {feature}] <= {threshold} "
            "else to node {right}.".format(
                space=node_depth[i] * "\t",
                node=i,
                left=children_left[i],
                feature=feature[i],
                threshold=threshold[i],
                right=children_right[i],
                value=values[i],
            )
        )

print('---------------------------------------------------')

# Make prediction
y_pred = clf.predict(x_test)

# Confusion matrix
cm = confusion_matrix(y_test, y_pred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels= np.unique(y_train))
disp.plot(cmap='Blues');
plt.title('Original dataset')

# Classification report
print('Classification report of Original dataset')
print(classification_report(y_test, y_pred))

print('---------------------------------------------------')

# Train on undersampled dataset
clf.fit(x_sub, y_sub)

# Plot decision tree
plt.figure(figsize=(15, 8))
tree.plot_tree(
    clf,
    class_names=np.unique(y_sub),
    feature_names=x_sub.columns,
    node_ids=True,
    rounded=True,
    filled=True
    );
plt.title('Decision tree structure trained by undersampled dataset')


# Understand decision tree structure
n_nodes = clf.tree_.node_count
children_left = clf.tree_.children_left
children_right = clf.tree_.children_right
feature = clf.tree_.feature
threshold = clf.tree_.threshold
values = clf.tree_.value

node_depth = np.zeros(shape=n_nodes, dtype=np.int64)
is_leaves = np.zeros(shape=n_nodes, dtype=bool)
stack = [(0, 0)]  # start with the root node id (0) and its depth (0)
while len(stack) > 0:
    # `pop` ensures each node is only visited once
    node_id, depth = stack.pop()
    node_depth[node_id] = depth

    # If the left and right child of a node is not the same we have a split
    # node
    is_split_node = children_left[node_id] != children_right[node_id]
    # If a split node, append left and right children and depth to `stack`
    # so we can loop through them
    if is_split_node:
        stack.append((children_left[node_id], depth + 1))
        stack.append((children_right[node_id], depth + 1))
    else:
        is_leaves[node_id] = True

print(
    "Decision tree structure trained by undersampled dataset \n"
    "The tree structure has {n} nodes and has "
    "the following tree structure:\n".format(n=n_nodes)
)
for i in range(n_nodes):
    if is_leaves[i]:
        print(
            "{space}node={node} is a leaf node with value={value}.".format(
                space=node_depth[i] * "\t", node=i, value=values[i]
            )
        )
    else:
        print(
            "{space}node={node} is a split node with value={value}: "
            "go to node {left} if X[:, {feature}] <= {threshold} "
            "else to node {right}.".format(
                space=node_depth[i] * "\t",
                node=i,
                left=children_left[i],
                feature=feature[i],
                threshold=threshold[i],
                right=children_right[i],
                value=values[i],
            )
        )

print('---------------------------------------------------')

# Make prediction
y_pred = clf.predict(x_test)

# Confusion matrix
cm = confusion_matrix(y_test, y_pred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels= np.unique(y_train))
disp.plot(cmap='Blues');
plt.title('Undersampled dataset')

# Classification report
print('Classification report of Undersampled dataset')
print(classification_report(y_test, y_pred))

print('---------------------------------------------------')

"""C) Pruning"""

# Pre-Pruning with max_deph
clf_2 = tree.DecisionTreeClassifier(
    criterion='gini',
    random_state=24,
    max_depth=3,
    max_leaf_nodes=None,
    ccp_alpha=0,
    )

# Train on original dataset
clf_2.fit(x_train, y_train)

# Plot decision tree
plt.figure(figsize=(15, 6))
tree.plot_tree(
    clf_2,
    class_names=np.unique(y_sub),
    feature_names=x_sub.columns,
    node_ids=True,
    rounded=True,
    filled=True
    );
plt.title('Decision tree structure trained by original dataset,  max_depth=3')

print('---------------------------------------------')

# Pediction
y_pred_2 = clf_2.predict(x_test)

# Classifiaction report
print('Classification report of original dataset, max_depth=3')
print(classification_report(y_test, y_pred_2))

# Train on undersampled dataset
clf_2.fit(x_sub, y_sub)

# Plot decision tree
plt.figure(figsize=(15,6))
tree.plot_tree(
    clf_2,
    class_names=np.unique(y_sub),
    feature_names=x_sub.columns,
    node_ids=True,
    rounded=True,
    filled=True
    );
plt.title('Decision tree structure trained by undersampled dataset,  max_depth=3')

print('---------------------------------------------')

# Pediction
y_pred_2 = clf_2.predict(x_test)

# Classifiaction report
print('Classification report of undersampled dataset, max_depth=3')
print(classification_report(y_test, y_pred_2))

# Pre-Pruning with max_leaf_nodes
clf_3 = tree.DecisionTreeClassifier(
    criterion='gini',
    random_state=24,
    max_depth=None,
    max_leaf_nodes=5,
    ccp_alpha=0,
    )

# Train on original dataset
clf_3.fit(x_train, y_train)

# Plot decision tree
plt.figure(figsize=(15, 8))
tree.plot_tree(
    clf_3,
    class_names=np.unique(y_train),
    feature_names=x_train.columns,
    node_ids=True,
    rounded=True,
    filled=True
    );
plt.title('Decision tree structure trained by original dataset,  max_leaf_node=5')

print('---------------------------------------------')

# Pediction
y_pred_3 = clf_3.predict(x_test)

# Classifiaction report
print('Classification report of original dataset, max_leaf_node=5')
print(classification_report(y_test, y_pred_3))

# Train on undersampled dataset
clf_3.fit(x_sub, y_sub)

# Plot decision tree
plt.figure(figsize=(15, 8))
tree.plot_tree(
    clf_3,
    class_names=np.unique(y_train),
    feature_names=x_train.columns,
    node_ids=True,
    rounded=True,
    filled=True
    );
plt.title('Decision tree structure trained by undersampled dataset,  max_leaf_node=5')

print('---------------------------------------------')

# Pediction
y_pred_3 = clf_3.predict(x_test)

# Classifiaction report
print('Classification report of undersampled dataset, max_leaf_node=5')
print(classification_report(y_test, y_pred_3))

# Post-Pruning with ccp_alpha
clf_4 = tree.DecisionTreeClassifier(
    criterion='gini',
    random_state=24,
    max_depth=None,
    max_leaf_nodes=None,
    ccp_alpha=0.1,
    )

# Train on original dataset
clf_4.fit(x_train, y_train)

# Plot decision tree
plt.figure(figsize=(8, 6))
tree.plot_tree(
    clf_4,
    class_names=np.unique(y_train),
    feature_names=x_train.columns,
    node_ids=True,
    rounded=True,
    filled=True
    );
plt.title('Decision tree structure trained by original dataset,  ccp_alpha=0.1')

print('---------------------------------------------')

# Pediction
y_pred_4 = clf_4.predict(x_test)

# Classifiaction report
print('Classification report of original dataset, ccp_alpha=0.1')
print(classification_report(y_test, y_pred_4))

# Train on undersampled dataset
clf_4.fit(x_sub, y_sub)

# Plot decision tree
plt.figure(figsize=(8, 6))
tree.plot_tree(
    clf_4,
    class_names=np.unique(y_train),
    feature_names=x_train.columns,
    node_ids=True,
    rounded=True,
    filled=True
    );
plt.title('Decision tree structure trained by undersampled dataset,  ccp_alpha=0.1')

print('---------------------------------------------')

# Pediction
y_pred_4 = clf_4.predict(x_test)

# Classifiaction report
print('Classification report of undersampled dataset, ccp_alpha=0.1')
print(classification_report(y_test, y_pred_4))

"""# Part III"""

# Define classifier
clf_RF = RandomForestClassifier(
    n_estimators=40,
    criterion='gini',
    max_depth=None,
    bootstrap=True,
    random_state=24,
    verbose=0,
    ccp_alpha=0,
    max_samples=30,
    )

# Train the model with original data
clf_RF.fit(x_train, y_train)

# Prediction
y_pred_RF = clf_RF.predict(x_test)

# Classifiaction report
print('Classification report of original dataset')
print(classification_report(y_test, y_pred_RF))