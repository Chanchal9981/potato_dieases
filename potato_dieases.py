

import keras
import tensorflow
import numpy as np
from keras.preprocessing.image import ImageDataGenerator

print("ver of ter",tensorflow.__version__)
print("ver of ter",keras.__version__)

data="/content/drive/MyDrive/archive (1)/PlantVillage"
train_data=ImageDataGenerator(rescale=1./255,
                             rotation_range=40,
                             width_shift_range=0.2,
                             height_shift_range=0.2,
                             shear_range=0.2,
                             zoom_range=0.2,
                             horizontal_flip=True,
                             fill_mode='nearest'
)

data_train_path=train_data.flow_from_directory(data,target_size=(224,224),batch_size=500,class_mode='binary')

data_train_path.class_indices

valid_data=ImageDataGenerator(rescale=1./255,validation_split=0.3)
validation_data=valid_data.flow_from_directory(data,
                                               target_size=(224, 224), 
                                               color_mode='rgb',
                                               batch_size=500, 
                                               class_mode='binary',
                                               shuffle=False,
                                               subset = 'validation'
                                               )

model=keras.models.Sequential([
                               keras.layers.Conv2D(filters=32,kernel_size=5,input_shape=[224,224,3]),
                               keras.layers.MaxPooling2D(pool_size=(2,2)),
                               keras.layers.Conv2D(filters=64,kernel_size=4),
                               keras.layers.MaxPooling2D(pool_size=(2,2)),
                               keras.layers.Conv2D(filters=128,kernel_size=3),
                               keras.layers.MaxPooling2D(pool_size=(2,2)),
                               keras.layers.Dropout(0.5),
                               keras.layers.Flatten(),
                               keras.layers.Dense(128,activation='relu'),
                               keras.layers.Dropout(0.3),
                               keras.layers.Dense(256,activation='relu'),
                               keras.layers.Dropout(0.4),
                               keras.layers.Dense(12,activation='softmax')
])

from tensorflow.keras.optimizers import Adam
model.compile(optimizer=Adam(lr=0.0001),loss="sparse_categorical_crossentropy",metrics=["accuracy"])

model.fit(data_train_path,epochs=20,verbose=1,validation_data=validation_data)

"""**Transfer learning**"""

from tensorflow.keras.layers import Input,Lambda,Dense,Flatten
from tensorflow.keras.models import Model
from tensorflow.keras.applications.inception_v3 import preprocess_input
from tensorflow.keras.preprocessing import image
from tensorflow.keras.preprocessing.image import ImageDataGenerator,load_img
from tensorflow.keras.models import Sequential
import numpy as np
from glob import glob

data="/content/drive/MyDrive/archive (1)/PlantVillage"
img_size=[224,224]

import tensorflow
resnet_152v2=tensorflow.keras.applications.ResNet152V2(input_shape=img_size+[3],weights='imagenet',include_top=False)

for layer in resnet_152v2.layers:
  layer.trainable=False

folder="/content/drive/MyDrive/archive (1)/PlantVillage/*"
list(folder[:5])

x=Flatten()(resnet_152v2.output)
predictions=Dense(len(folder),activation='softmax')(x)
model=Model(inputs=resnet_152v2.input,outputs=predictions)

Image_gen=ImageDataGenerator(rescale=1./255,
                             rotation_range=40,
                             width_shift_range=0.2,
                             height_shift_range=0.2,
                             shear_range=0.2,
                             zoom_range=0.2,
                             horizontal_flip=True,
                             fill_mode='nearest')

train_image_gen=Image_gen.flow_from_directory(data,target_size=(224,224),batch_size=400,class_mode='binary')

valid_data=ImageDataGenerator(rescale=1./255,validation_split=0.4)
validation_data=valid_data.flow_from_directory(data,
                                               target_size=(224, 224), 
                                               color_mode='rgb',
                                               batch_size=400, 
                                               class_mode='binary',
                                               shuffle=False,
                                               subset = 'validation'
                                               )

model.compile(optimizer='adam',loss="sparse_categorical_crossentropy",metrics=["accuracy"])

model.fit(train_image_gen,epochs=10,verbose=1,validation_data=validation_data)

model.fit(train_image_gen,epochs=10,verbose=1,validation_data=validation_data)

model.fit(train_image_gen,epochs=10,verbose=1,validation_data=validation_data)

model.fit(train_image_gen,epochs=10,verbose=1,validation_data=validation_data)

model.save("potato_diease_plant.h5")
