#导包
import sys
from matplotlib import pyplot
from tensorflow.python.keras.api import keras
from tensorflow.python.keras.api.keras.utils import to_categorical
from tensorflow.python.keras.api.keras.models import Sequential
from tensorflow.python.keras.api.keras.layers import Conv2D
from tensorflow.python.keras.api.keras.layers import MaxPooling2D
from tensorflow.python.keras.api.keras.layers import Dense
from tensorflow.python.keras.api.keras.layers import Flatten
from tensorflow.python.keras.api.keras.optimizers import SGD
from tensorflow.python.keras.api.keras.preprocessing.image import ImageDataGenerator
import tensorflow as tf
tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.ERROR)

#创建一个cnn模型
def define_cnn_model():
    conv_base = tf.keras.applications.DenseNet121(weights='imagenet', include_top=False)
    # 设置为不可训练
    conv_base.trainable = True
    # 模型搭建
    model = tf.keras.Sequential()
    model.add(conv_base)

    #     #卷积层
    # model.add(Conv2D(32,(3,3),activation="relu",padding="same",input_shape=(200,200,3)))
    #     #最大池化层
    # model.add(MaxPooling2D((2,2)))
        #Flatten层
    model.add(Flatten())
        #全连接层
    model.add(Dense(512,activation="relu"))
    model.add(Dense(2,activation="softmax"))

        #编译模型
    opt = SGD(lr=0.001,mementum=0.9)
    model.compile(optimizer=opt,
                      loss='binary_crossentropy',
                      metrics=['accuracy'])
    return model

    from keras.utils import plot_model
    model = define_cnn_model()
    plot_model(model,
               to_file='cnn_model.png',
               dpi=100,
               show_shapes=Ture,
               show_layer_names=True)


def train_cnn_model():
    #实例化模型
    model = define_cnn_model()
    #创建图片生成器
    detagen = ImageDataGenerator(rescale=1.0/255.0)
    train_it = detagen.flow_from_directory(
        '',#图片地址
        class_mode='binary',
        batch_size=32,
        target_size=(200,200)
    )
    #训练模型
    model.fit_generator(
        train_it,
        steps_per_epoch=(train_it),
        epochs=1,
        verbose=1
    )

