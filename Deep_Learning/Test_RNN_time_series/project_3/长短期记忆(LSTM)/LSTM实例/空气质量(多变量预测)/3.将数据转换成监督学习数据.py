from math import sqrt
from numpy import concatenate
from Example_matplotlib import pyplot
from pandas import read_csv
from pandas import DataFrame
from pandas import concat
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_squared_error
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
import pandas as pd

pd.set_option('display.max_columns',1000)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth',1000)

def series_to_supervised(data, n_in=1, n_out=1, dropnan=True):
    # ��ȡ����ֵ����n_vars
    n_vars = 1 if type(data) is list else data.shape[1]
    df = DataFrame(data)
    print(df)
    cols, names = list(), list()
    # input sequence (t-n, ... t-1)
    # ����8��v(t-1)��Ϊ����
    for i in range(n_in, 0, -1):
        # ���б�cols�����һ��df.shift(1)������
        cols.append(df.shift(i))
        print(cols)
        names += [('var%d(t-%d)' % (j+1, i)) for j in range(n_vars)]
    # forecast sequence (t, t+1, ... t+n)
    for i in range(0, n_out):
        # ���б�cols�����һ��df.shift(-1)������
        cols.append(df.shift(-i))
        print(cols)
        if i == 0:
        	names += [('var%d(t)' % (j+1)) for j in range(n_vars)]
        else:
        	names += [('var%d(t+%d)' % (j+1, i)) for j in range(n_vars)]
    print(cols)
    # ���б�����������������ƴ��������list(v1,v2)->[v1,v2],����v1�����ƶ���һ�У���ʱv1,v2�Ǽලѧϰ������
    agg = concat(cols, axis=1)
    print(agg)
    # �ض�������
    agg.columns = names
    print(agg)
    # ɾ����ֵ
    if dropnan:
    	agg.dropna(inplace=True)
    return agg

# load dataset
dataset = read_csv('pollution.csv', header=0, index_col=0)
values = dataset.values
print(values)
# �Ե����С����򡱽������ֱ���ת��
encoder = LabelEncoder()
values[:,4] = encoder.fit_transform(values[:,4])
print(values[:,4])
# ����ת��Ϊ������
values = values.astype('float32')
# �������������ŵ���0��1��֮��
scaler = MinMaxScaler(feature_range=(0, 1))
scaled = scaler.fit_transform(values)
# �����ݸ�ʽ���ɼලѧϰ������
reframed = series_to_supervised(scaled, 1, 1)
print(reframed.head())
# ɾ����Щ���ǲ���Ԥ�����,axis=1�в���
reframed.drop(reframed.columns[[9,10,11,12,13,14,15]], axis=1, inplace=True)
# ����ÿ�����ݸ�ʽ���£�����v1(t-1)~v8(t-1)��ʾǰһ������ݣ�v1(t)��ʾ����ҪԤ������ݣ�
# v1(t-1),v2(t-2),v3(t-3),v4(t-4),v5(t-5),v6(t-6),v7(t-7),v8(t-1),v1(t)
print(reframed.head())