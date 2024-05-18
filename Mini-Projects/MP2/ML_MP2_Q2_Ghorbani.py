# -*- coding: utf-8 -*-
"""ML_MP2_Q2_Ghorbani.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1sBepl3-NRet544HM2toOAl3yAZi1rJ5c

# Q2
Multi-class fault detection on [CWRU bearing dataset](https://engineering.case.edu/bearingdatacenter/download-data-file) with Multi-layer perceptron network.
"""

# Import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.io as sio
import seaborn as sb
import random

from sklearn.utils import shuffle
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, classification_report
from sklearn.model_selection import KFold

import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense

"""# Part I"""

# Import datasets as .mat
!pip install --upgrade --no-cach-dir gdown
! gdown 18r7azVBOL_beMqPlcWFAf90m-PEggHCB # Normal_0
! gdown 1KGB6D-5QS-PAXFYrba-JqkF5h4GHbRyR # IR007_0
! gdown 1BU3HEXI_-ejE0k-uBS1HnM76UMvQduRc # B007_0
! gdown 1qk-OCnOMfqS-ZlGlqD9lCBdL29IzJ2sI # OR007@6_0

# Extract deive-end accelerometer data (DE)
data_n = sio.loadmat('97(Normal_0).mat')
data_f_IR = sio.loadmat('105(IR007_0).mat')
data_f_B = sio.loadmat('118(B007_0).mat')
data_f_OR = sio.loadmat('130(OR007@6_0).mat')


data_normal = pd.DataFrame(data_n['X097_DE_time'])
data_fault_IR = pd.DataFrame(data_f_IR['X105_DE_time'])
data_fault_B = pd.DataFrame(data_f_B['X118_DE_time'])
data_fault_OR = pd.DataFrame(data_f_OR['X130_DE_time'])

print(data_normal.shape, data_fault_IR.shape, data_fault_OR.shape, data_fault_B.shape)

sampling_rate = 12000
duration = 10

time = np.arange(0, duration, 1/sampling_rate)

plt.rcParams["figure.figsize"] = (18, 12)
fig1, ax_array = plt.subplots(2, 2)

ax11, ax12 = ax_array[0]
ax21, ax22 = ax_array[1]

ax11.plot(time, data_normal[:len(time)])
ax11.set_title('Vibration data of normal bearing')
ax11.set_xlabel('Time(s)')
ax11.set_ylabel('Amplitude')
ax11.grid(True)

ax12.plot(time, data_fault_IR[:len(time)])
ax12.set_title('Vibration data of faulty bearing (Inner race)')
ax12.set_xlabel('Time(s)')
ax12.set_ylabel('Amplitude')
ax12.grid(True)

ax21.plot(time, data_fault_OR[:len(time)])
ax21.set_title('Vibration data of faulty bearing (Outer race)')
ax21.set_xlabel('Time(s)')
ax21.set_ylabel('Amplitude')
ax21.grid(True)


ax22.plot(time, data_fault_B[:len(time)])
ax22.set_title('Vibration data of faulty bearing (Ball)')
ax22.set_xlabel('Time(s)')
ax22.set_ylabel('Amplitude')
ax22.grid(True)

M = 400
N = 300

X = []
Y = []

# Normal class
for i in range(M):
  start_idx = i * N
  end_idx = start_idx + N
  x = data_normal[start_idx:end_idx]
  X.append(x)
  Y.append(0) # Normal class

# IR fault class
for i in range(M):
  start_idx = i * N
  end_idx = start_idx + N
  x = data_fault_IR[start_idx:end_idx]
  X.append(x)
  Y.append(1) # IR fault class

# B fault class
for i in range(M):
  start_idx = i * N
  end_idx = start_idx + N
  x = data_fault_B[start_idx:end_idx]
  X.append(x)
  Y.append(2) # B fault class

# OR fault class
for i in range(M):
  start_idx = i * N
  end_idx = start_idx + N
  x = data_fault_OR[start_idx:end_idx]
  X.append(x)
  Y.append(3) # OR fault class

X = np.array(X)
Y = np.array(Y)

X = np.reshape(X,(4*M,N))
Y = np.reshape(Y,(4*M,1))


print(X.shape, Y.shape)

# Square Mean Root
def smr(x):
  return np.mean(np.sqrt(abs(x)))**2

# Root Mean Square
def rms(x):
  return np.sqrt(np.mean((x**2)))

# Absolut Mean
def abs_mean(x):
  return np.mean(abs(x))

# Impact Factor 1
def IF1(x):
  return np.max(x) / (abs_mean(x))

def feature_extract(x):
  y = np.zeros((1,8))
  y[0,0] = np.mean(x)
  y[0,1] = np.std(x)
  y[0,2] = np.max(x)
  y[0,3] = np.max(x) - np.min(x)
  y[0,4] = smr(x)
  y[0,5] = rms(x)
  y[0,6] = abs_mean(x)
  y[0,7] = IF1(x)
  return y

Xnew = np.zeros(shape = (4*M,8))

for i in range(4*M):
  Xnew[[i],:] = feature_extract(X[[i],:])

print(Xnew.shape)

# Shuffle both X and Y with same order
X_shuffled, Y_shuffled = shuffle(Xnew,Y, random_state = 24)

train_ratio = 0.7
test_ratio = 0.15
validation_ratio = 0.15

x_train, x_temp, y_train, y_temp = train_test_split(
    X_shuffled, Y_shuffled,
    test_size = 1 - train_ratio,
    random_state=24
    )

x_val, x_test, y_val, y_test = train_test_split(
    x_temp, y_temp,
    test_size = test_ratio/(test_ratio + validation_ratio),
    random_state=24
    )

print(x_train.shape, x_test.shape, x_val.shape)
print(y_train.shape, y_test.shape, y_val.shape)

plt.rcParams["figure.figsize"] = (15, 5)

plt.subplot(1,3,1)
plt.hist(x_train[:,0])
plt.title('Histplot of mean values for Training set')

plt.subplot(1,3,2)
plt.hist(x_val[:,0])
plt.title('Histplot of mean values for Validation set')

plt.subplot(1,3,3)
plt.hist(x_test[:,0])
plt.title('Histplot of mean values for Test set')

scaler = MinMaxScaler()
scaler.fit(x_train)

x_train_normalized = scaler.transform(x_train)
x_test_normalized = scaler.transform(x_test)
x_val_normalized = scaler.transform(x_val)

print(np.min(x_train_normalized), np.min(x_test_normalized), np.min(x_val_normalized))
print(np.max(x_train_normalized), np.max(x_test_normalized), np.max(x_val_normalized))

"""# Part II"""

tf.random.set_seed(24)
random.seed(24)

model_1 = Sequential([
    Dense(units = 10, activation='relu'),
    Dense(units = 7, activation='relu'),
    Dense(units = 4, activation='softmax'),
])

model_1.compile(
    optimizer='Adam',
    loss='SparseCategoricalCrossentropy',
    metrics=['accuracy']
    )

hist_1 = model_1.fit(
    x=x_train_normalized,
    y=y_train,
    validation_data=(x_val_normalized,y_val),
    epochs=100,
    batch_size=10,
    verbose=2,
    )

# Plot the training and validation loss
plt.rcParams["figure.figsize"] = (12, 4)
plt.plot(hist_1.history['loss'], color='blue', linewidth=2)   # Training loss
plt.plot(hist_1.history['val_loss'], color='red', linewidth=2)  # Validation loss

plt.legend(['Training Loss', 'Validation Loss'])
plt.xlabel("Epochs")
plt.ylabel("Loss")
plt.title('Optimizer = Adam, Loss = Sparse Categorical Crossentropy')
plt.grid(True, linewidth = 1, linestyle=':')
plt.show()

# Plot the training and validation accuracy
plt.plot(hist_1.history['accuracy'], color='blue', linewidth=2)   # Training accuracy
plt.plot(hist_1.history['val_accuracy'], color='red', linewidth=2)  # Validation accuracy

plt.legend(['Training Accuracy', 'Validation Accuracy'])
plt.xlabel("Epochs")
plt.ylabel("Accuracy")
plt.title('Optimizer = Adam, Loss = Sparse Categorical Crossentropy')
plt.grid(True, linewidth = 1, linestyle=':')
plt.show()

y_probs_1 = model_1.predict(x_test_normalized)
y_pred_1 = y_probs_1.argmax(axis=1)

plt.rcParams["figure.figsize"] = (10, 6)
cm1 = confusion_matrix(y_test, y_pred_1)
disp1 = ConfusionMatrixDisplay(confusion_matrix=cm1)
disp1.plot(cmap='Blues')

print(classification_report(y_test, y_pred_1))

"""# Part III"""

tf.random.set_seed(24)
random.seed(24)

model_2 = Sequential([
    Dense(units = 10, activation='relu'),
    Dense(units = 5, activation='relu'),
    Dense(units = 4, activation='softmax'),
])

model_2.compile(
    optimizer='SGD',
    loss='KLDivergence',
    metrics=['accuracy']
    )

hist_2 = model_2.fit(
    x=x_train_normalized,
    y=y_train,
    validation_data=(x_val_normalized,y_val),
    epochs=100,
    batch_size=10,
    verbose=2,
    )

# Plot the training and validation loss
plt.rcParams["figure.figsize"] = (12, 4)
plt.plot(hist_2.history['loss'], color='blue', linewidth=2)
plt.plot(hist_2.history['val_loss'], color='red', linewidth=2)

plt.legend(['Training Loss', 'Validation Loss'])
plt.xlabel("Epochs")
plt.ylabel("Loss")
plt.title('Optimizer = SGD, Loss = Kullback Leibler Divergence')
plt.grid(True, linewidth = 1, linestyle=':')
plt.show()

# Plot the training and validation accuracy
plt.plot(hist_2.history['accuracy'], color='blue', linewidth=2)   # Training accuracy
plt.plot(hist_2.history['val_accuracy'], color='red', linewidth=2)  # Validation accuracy

plt.legend(['Training Accuracy', 'Validation Accuracy'])
plt.xlabel("Epochs")
plt.ylabel("Accuracy")
plt.title('Optimizer = SGD, Loss =  Kullback-Leibler Divergence')
plt.grid(True, linewidth = 1, linestyle=':')
plt.show()

y_probs_2 = model_2.predict(x_test_normalized)
y_pred_2 = y_probs_2.argmax(axis=1)

plt.rcParams["figure.figsize"] = (10, 6)
cm2 = confusion_matrix(y_test, y_pred_2)
disp2 = ConfusionMatrixDisplay(confusion_matrix=cm2)
disp2.plot(cmap='Blues')

print(classification_report(y_test, y_pred_2))

"""# Part IV"""

CV = KFold(n_splits=10, shuffle=True, random_state=24)

acc_per_fold_1 = []
loss_per_fold_1 = []
fold_no_1 = 1

for train_index, test_index in CV.split(x_train_normalized, y_train):
  tf.random.set_seed(24)
  random.seed(24)

  model_3 = Sequential([
    Dense(units = 10, activation='relu'),
    Dense(units = 7, activation='relu'),
    Dense(units = 4, activation='softmax'),
    ])

  model_3.compile(
    optimizer='Adam',
    loss='SparseCategoricalCrossentropy',
    metrics=['accuracy']
    )

  hist_3 = model_3.fit(
    x=x_train_normalized[train_index],
    y=y_train[train_index],
    epochs=100,
    batch_size=10,
    verbose=0,
    )

  scores_1 = model_3.evaluate(
      x_train_normalized[test_index],
      y_train[test_index],
      verbose=0
      )

  acc_per_fold_1.append(scores_1[1] * 100)
  loss_per_fold_1.append(scores_1[0])

  print('---------------------------------------------------------------------')
  print(f'Training for fold {fold_no_1}')
  print(f'Accuracy: {scores_1[1]}')
  print(f'Loss: {scores_1[0]}')
  fold_no_1 += 1

acc_per_fold_2 = []
loss_per_fold_2 = []
fold_no_2 = 1

for train_index, test_index in CV.split(x_train_normalized, y_train):
  tf.random.set_seed(24)
  random.seed(24)

  model_4 = Sequential([
    Dense(units = 10, activation='relu'),
    Dense(units = 7, activation='relu'),
    Dense(units = 4, activation='softmax'),
    ])

  model_4.compile(
    optimizer='sGD',
    loss='KLDivergence',
    metrics=['accuracy']
    )

  hist_4 = model_4.fit(
    x=x_train_normalized[train_index],
    y=y_train[train_index],
    epochs=100,
    batch_size=10,
    verbose=0,
    )

  scores_2 = model_4.evaluate(
      x_train_normalized[test_index],
      y_train[test_index],
      verbose=0
      )

  acc_per_fold_2.append(scores_2[1] * 100)
  loss_per_fold_2.append(scores_2[0])

  print('---------------------------------------------------------------------')
  print(f'Training for fold {fold_no_2}')
  print(f'Accuracy: {scores_2[1]}')
  print(f'Loss: {scores_2[0]}')
  fold_no_2 += 1

print(f'Avarage accuracy is {np.mean(acc_per_fold_1)} and avarage loss is {np.mean(loss_per_fold_1)} for Model 1.')
print(f'Avarage accuracy is {np.mean(acc_per_fold_2)} and avarage loss is {np.mean(loss_per_fold_2)} for Model 2.')