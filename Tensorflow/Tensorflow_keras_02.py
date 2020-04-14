# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import *


# %%
# đề bài :
# cho phương trình : y = wx
# cho nghiệm : x = [x1,x2,x3,x4,x5....xn]
#                      y = [y1,y2,y3,y4,y5.....yn]
# tìm : w (weight)


# %%
# x_train = [ [1,2] , [1,3] ,[1,3 ], [1,4 ] , [1,5], [1,6] ] #  1

x_train_labels = [3, 6, 9, 12, 15, 18]

y_train_datas = [1, 2, 3, 4, 5, 6]  # 5

#  bằng  tính toán bình thường ta có thể nhận ra ở đây weight = [2]

x_train_labels, y_train_datas


# %%
# Thiết lập các layers

model = keras.Sequential([
    keras.layers.Dense(1, input_shape=(1,))
])
model.summary()


# %%
# Biên dịch mô hình
sgd = optimizers.SGD(lr=0.01)
model.compile(loss="mse", optimizer=sgd)
model.fit(x_train_labels, y_train_datas, epochs=100)


# %%
y_test = model.predict([10])
print(y_test)
