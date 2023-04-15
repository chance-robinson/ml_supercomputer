import numpy as np
import tensorflow as tf
from tensorflow import keras
from keras import layers
import sys
import os

os.chdir('..')
cwd = os.getcwd()

dataset = np.load(f'{cwd}/content/cifar100.npz')
y_train = dataset['y_train']
y_val = dataset['y_val']
x_train = dataset['x_train']
x_val = dataset['x_val']

y_train = tf.one_hot(y_train,
                     depth=y_train.max() + 1,
                     dtype=tf.float64)
y_val = tf.one_hot(y_val,
                   depth=y_val.max() + 1,
                   dtype=tf.float64)
  
y_train = tf.squeeze(y_train)
y_val = tf.squeeze(y_val)

BATCH_SIZE = int(sys.argv[1])
EPOCHS = int(sys.argv[2])
LEARNING_RATE = float(sys.argv[3])
L1NF = int(sys.argv[4])
FDROPOUT = float(sys.argv[5])

# constant values
NUM_CLASSES = 100 #100 prediction classes
INPUT_SHAPE = (32,32,3) #shape of the input image 32x32 with 3 channels

model = tf.keras.models.Sequential([
                
                # CHANGE THESE: these are layers you should mix up and change
                layers.Conv2D(L1NF, (3, 3), input_shape = INPUT_SHAPE,
                                activation='relu',
                                padding='same'),
                layers.MaxPooling2D(2,2),
                layers.Dropout(FDROPOUT),
                
                # DO NOT CHANGE THESE. They should be at the end of your model
                layers.Flatten(),
                layers.Dense(NUM_CLASSES, activation='softmax')])

model.compile(loss='categorical_crossentropy',
            optimizer=keras.optimizers.Nadam(learning_rate=LEARNING_RATE),
            # DO NOT CHANGE THE METRIC. This is what you will be judging your model on
            metrics=['accuracy'],)

# here you train the model using some of your hyperparameters and send the data
# to weights and biases after every batch            
history = model.fit(x_train, y_train,
                    epochs=EPOCHS,
                    batch_size=BATCH_SIZE,
                    verbose=1,
                    validation_data=(x_val, y_val),
                    )

model.save(f'{cwd}/models/model_{BATCH_SIZE}_{EPOCHS}_{LEARNING_RATE}_{L1NF}_{FDROPOUT}.h5')

with open(f'{cwd}/results/accuracy_{BATCH_SIZE}_{EPOCHS}_{LEARNING_RATE}_{L1NF}_{FDROPOUT}.txt', 'w') as f:
    f.write(str(history.history['accuracy'][-1]))
    # f.write(str(history.history['val_loss'][-1]))
    # f.write(str(history.history['val_accuracy'][-1]))