# -*-coding:utf-8-*-
# @Time    : 2019/11/25 0025 14:45
# @Author  :zhu
# @File    : method_3_LSTM.py
# @task description :
"""
用LSTM训练时序数据
"""
import math
import Example_matplotlib
import numpy as np
import pandas as pd
import seaborn as sns
import time

from datetime import date
from Example_matplotlib import pyplot as plt
from numpy.random import seed
from pylab import rcParams
from sklearn.metrics import mean_squared_error
from tqdm import tqdm_notebook
from sklearn.preprocessing import MinMaxScaler
from tensorflow import set_random_seed
from keras.models import Sequential
from keras.layers import Dense, Dropout, LSTM
from keras.utils import plot_model

#### Input params ##################
stk_path = "./data/VTI.csv"
test_size = 0.2                # proportion of dataset to be used as test set
cv_size = 0.2                  # proportion of dataset to be used as cross-validation set

N = 9                          # for feature at day t, we use lags from t-1, t-2, ..., t-N as features.
                               # initial value before tuning
lstm_units=50                  # lstm param. initial value before tuning.
dropout_prob=1                 # lstm param. initial value before tuning.
optimizer='adam'               # lstm param. initial value before tuning.
epochs=1                       # lstm param. initial value before tuning.
batch_size=1                   # lstm param. initial value before tuning.

model_seed = 100

fontsize = 14
ticklabelsize = 14
####################################

# Set seeds to ensure same output results
seed(101)
set_random_seed(model_seed)


def get_mape(y_true, y_pred):
    """
    Compute mean absolute percentage error (MAPE)
    """
    y_true, y_pred = np.array(y_true), np.array(y_pred)
    return np.mean(np.abs((y_true - y_pred) / y_true)) * 100


def get_x_y(data, N, offset):
    """
    Split data into x (features) and y (target)
    """
    x, y = [], []
    for i in range(offset, len(data)):
        x.append(data[i - N:i])
        y.append(data[i])
    x = np.array(x)
    y = np.array(y)

    return x, y


def train_pred_eval_model(x_train_scaled, y_train_scaled, x_cv_scaled, y_cv_scaled, scaler, lstm_units=50, dropout_prob=0.5, optimizer='adam', epochs=1, batch_size=1):
    '''
    Train model, do prediction, scale back to original range and do evaluation
    Use LSTM here.
    Returns rmse, mape and predicted values
    Inputs
        x_train_scaled  : e.g. x_train_scaled.shape=(451, 9, 1). Here we are using the past 9 values to predict the next value
        y_train_scaled  : e.g. y_train_scaled.shape=(451, 1)
        x_cv_scaled     : use this to do predictions
        y_cv_scaled     : actual value of the predictions (scaled)
        scaler          : scaler that is used to fit_transform train set
        lstm_units      : lstm param
        dropout_prob    : lstm param
        optimizer       : lstm param
        epochs          : lstm param
        batch_size      : lstm param
    Outputs
        rmse            : root mean square error
        mape            : mean absolute percentage error
        est             : predictions
    '''
    # Create the LSTM network
    model = Sequential()
    model.add(LSTM(units=lstm_units, return_sequences=True, input_shape=(x_train_scaled.shape[1], 1)))
    model.add(Dropout(dropout_prob))  # Add dropout with a probability of 0.5
    model.add(LSTM(units=lstm_units))
    model.add(Dropout(dropout_prob))  # Add dropout with a probability of 0.5
    model.add(Dense(1))

    # Compile and fit the LSTM network
    model.compile(loss='mean_squared_error', optimizer=optimizer)
    model.fit(x_train_scaled, y_train_scaled, epochs=epochs, batch_size=batch_size, verbose=0)

    # Do prediction
    est_scaled = model.predict(x_cv_scaled)
    est = scaler.inverse_transform(est_scaled)

    # Get correct scale of y_cv
    y_cv = scaler.inverse_transform(y_cv_scaled)

    # Calculate RMSE and MAPE
    rmse = math.sqrt(mean_squared_error(y_cv, est))
    mape = get_mape(y_cv, est)

    return rmse, mape, est


df = pd.read_csv(stk_path, sep=",")

# Convert Date column to datetime
df.loc[:, 'Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d')

# Change all column headings to be lower case, and remove spacing
df.columns = [str(x).lower().replace(' ', '_') for x in df.columns]

# Get month of each sample
df['month'] = df['date'].dt.month

# Sort by datetime
df.sort_values(by='date', inplace=True, ascending=True)

num_cv = int(cv_size*len(df))
num_test = int(test_size*len(df))
num_train = len(df) - num_cv - num_test
print("num_train = " + str(num_train))
print("num_cv = " + str(num_cv))
print("num_test = " + str(num_test))
print()

# 制作训练，验证，测试的数据，
train = df[:num_train][['date', 'adj_close']]
cv = df[num_train:num_train+num_cv][['date', 'adj_close']]
train_cv = df[:num_train+num_cv][['date', 'adj_close']]
test = df[num_train+num_cv:][['date', 'adj_close']]

print("train.shape = " + str(train.shape))
print("cv.shape = " + str(cv.shape))
print("train_cv.shape = " + str(train_cv.shape))
print("test.shape = " + str(test.shape))
print("*****以上是数据情况*****")

"""获取训练集，验证集，测试集"""
# 训练集
scaler = MinMaxScaler(feature_range=(0, 1))
train_scaled = scaler.fit_transform(np.array(train['adj_close']).reshape(-1, 1))
x_train, y_train = get_x_y(train_scaled, N, N)

# 验证集
train_cv_scaled = scaler.transform(np.array(train_cv['adj_close']).reshape(-1, 1))
x_cv, y_cv = get_x_y(train_cv_scaled, N, num_train)




# Here we scale the train_cv set, for the final model
scaler_final = MinMaxScaler(feature_range=(0, 1))
train_cv_scaled_final = scaler_final.fit_transform(np.array(train_cv['adj_close']).reshape(-1,1))
print("scaler_final.data_min_ = " + str(scaler_final.data_min_))
print("scaler_final.data_max_ = " + str(scaler_final.data_max_))

# Scale the test dataset according the min and max obtained from train_cv set
test_scaled  = scaler_final.transform(np.array(df['adj_close']).reshape(-1,1))

# Create the LSTM network
model = Sequential()
model.add(LSTM(units=lstm_units, return_sequences=True, input_shape=(x_train.shape[1], 1)))
model.add(Dropout(dropout_prob))    # Add dropout with a probability of 0.5
model.add(LSTM(units=lstm_units))
model.add(Dropout(dropout_prob))    # Add dropout with a probability of 0.5
model.add(Dense(1))
model.compile(loss='mean_squared_error', optimizer=optimizer)
model.fit(x_train, y_train, epochs=epochs, batch_size=batch_size, verbose=2)
model.summary()


"""做验证集的预测"""
est = model.predict(x_cv)
est_inv = scaler.inverse_transform(est)

# Get correct scale of y_cv
y_cv_inv = scaler.inverse_transform(y_cv)

# Calculate RMSE
rmse_bef_tuning = math.sqrt(mean_squared_error(y_cv_inv, est_inv))
print("RMSE = %0.3f" % rmse_bef_tuning)

# Calculate MAPE
mape_pct_bef_tuning = get_mape(y_cv_inv, est_inv)
print("MAPE = %0.3f%%" % mape_pct_bef_tuning)


"""可视化"""
rcParams['figure.figsize'] = 10, 8  # width 10, height 8
est_df = pd.DataFrame({'est_inv': est_inv.reshape(-1),
                       'y_cv_inv': y_cv_inv.reshape(-1),
                       'date': cv['date']})

ax = train.plot(x='date', y='adj_close', style='b-', grid=True)
ax = cv.plot(x='date', y='adj_close', style='y-', grid=True, ax=ax)
ax = test.plot(x='date', y='adj_close', style='g-', grid=True, ax=ax)
ax = est_df.plot(x='date', y='est_inv', style='r-', grid=True, ax=ax)
ax.legend(['train', 'dev', 'test', 'est'])
ax.set_xlabel("date")
ax.set_ylabel("USD")
plt.savefig("./data/result_1.png")
plt.show()

# exit("暂停")



# param_label = 'N'
# param_list = range(2, 60)
#
# error_rate = {param_label: [], 'rmse': [], 'mape_pct': []}
# tic = time.time()
# print(len(param_list))
# for param in param_list:
#     print(param)
#     # Split train into x and y
#     x_train_scaled, y_train_scaled = get_x_y(train_scaled, param, param)
#
#     # Split cv into x and y
#     x_cv_scaled, y_cv_scaled = get_x_y(train_cv_scaled, param, num_train)
#
#     # Train, predict and eval model
#     rmse, mape, _ = train_pred_eval_model(x_train_scaled,
#                                           y_train_scaled,
#                                           x_cv_scaled,
#                                           y_cv_scaled,
#                                           scaler,
#                                           lstm_units=lstm_units,
#                                           dropout_prob=dropout_prob,
#                                           optimizer='adam',
#                                           epochs=epochs,
#                                           batch_size=batch_size)
#
#     # Collect results
#     error_rate[param_label].append(param)
#     error_rate['rmse'].append(rmse)
#     error_rate['mape_pct'].append(mape)
#
# error_rate = pd.DataFrame(error_rate)
# error_rate.to_excel("./result.xlsx")
# toc = time.time()
# print("Minutes taken = " + str((toc - tic) / 60.0))
# # error_rate
#
# rcParams['figure.figsize'] = 10, 8  # width 10, height 8
#
# ax = error_rate.plot(x='N', y='rmse', style='bx-', grid=True)
# ax = error_rate.plot(x='N', y='mape_pct', style='rx-', grid=True, ax=ax)
# ax.set_xlabel("N")
# ax.set_ylabel("RMSE/MAPE(%)")
# plt.savefig("./data/result_2.png")
# plt.show()

# Split train_cv into x and y
N_opt = 5
x_train_cv_scaled, y_train_cv_scaled = get_x_y(train_cv_scaled_final, N_opt, N_opt)

# Split test into x and y
x_test_scaled, y_test_scaled = get_x_y(test_scaled, N_opt, num_train+num_cv)

# Train, predict and eval model
rmse, mape, est = train_pred_eval_model(x_train_cv_scaled,
                                        y_train_cv_scaled,
                                        x_test_scaled,
                                        y_test_scaled,
                                        scaler_final,
                                        lstm_units=60,
                                        dropout_prob=1,
                                        optimizer="adagrad",
                                        epochs=30,
                                        batch_size=30)

# Calculate RMSE
print("RMSE on test set = %0.3f" % rmse)

# Calculate MAPE
print("MAPE on test set = %0.3f%%" % mape)



# Plot adjusted close over time
rcParams['figure.figsize'] = 10, 8 # width 10, height 8

est_df = pd.DataFrame({'est': est.reshape(-1),
                       'date': df[num_train+num_cv:]['date']})

ax = train.plot(x='date', y='adj_close', style='b-', grid=True)
ax = cv.plot(x='date', y='adj_close', style='y-', grid=True, ax=ax)
ax = test.plot(x='date', y='adj_close', style='g-', grid=True, ax=ax)
ax = est_df.plot(x='date', y='est', style='r-', grid=True, ax=ax)
ax.legend(['train', 'dev', 'test', 'predictions'])
ax.set_xlabel("date")
ax.set_ylabel("USD")
plt.savefig("./data/last1.png")
plt.show()


# Plot adjusted close over time, for test set only
rcParams['figure.figsize'] = 10, 8 # width 10, height 8
ax = train.plot(x='date', y='adj_close', style='b-', grid=True)
ax = cv.plot(x='date', y='adj_close', style='y-', grid=True, ax=ax)
ax = test.plot(x='date', y='adj_close', style='g-', grid=True, ax=ax)
ax = est_df.plot(x='date', y='est', style='r-', grid=True, ax=ax)
ax.legend(['train', 'dev', 'test', 'predictions'])
ax.set_xlabel("date")
ax.set_ylabel("USD")
ax.set_xlim([date(2018, 4, 1), date(2018, 11, 30)])
ax.set_ylim([130, 155])
ax.set_title("Zoom in to test set")
plt.savefig("./data/last2.png")
plt.show()



"""

归一化函数：MinMaxScaler

fit_transform()和transform()的区别


"""