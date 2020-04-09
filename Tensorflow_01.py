# Phân loại cơ bản: Dự đoán ảnh quần áo giày dép
# Hướng dẫn này dùng tf.keras, một API cấp cao để xây dựng và huấn luyện các mô hình trong TensorFlow.

import tensorflow as tf
from tensorflow import keras

# Helper libraries
import numpy as np
import matplotlib.pyplot as plt

print(tf.__version__)

# mport tập dữ liệu về quần áo và giày dép từ Fashion MNIST

fashion_mnist = keras.datasets.fashion_mnist

(train_images, train_labels), (test_images, test_labels) \
    = fashion_mnist.load_data()


class_names = ['Áo thun', 'Quần dài', 'Áo liền quần', 'Đầm', 'Áo khoác',
               'Sandal', 'Áo sơ mi', 'Giày', 'Túi xách', 'Ủng']

for x in class_names:
    print(" class : ", x)
