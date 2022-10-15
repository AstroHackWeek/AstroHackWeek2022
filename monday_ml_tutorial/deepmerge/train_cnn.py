import os

import numpy as np
from keras.models import Model
from keras.layers import Input, Flatten, Dense, Dropout, BatchNormalization
from keras.layers.convolutional import Convolution2D, MaxPooling2D
from keras.regularizers import l2
from keras.callbacks import ModelCheckpoint, EarlyStopping


def get_cnn_architecture(imsize=75, channels=3):
    input_shape = (imsize, imsize, channels)

    x_in = Input(shape=input_shape)
    c0 = Convolution2D(8, (5, 5), activation='relu', strides=(1, 1), padding='same')(x_in)
    b0 = BatchNormalization()(c0)
    d0 = MaxPooling2D(pool_size=(2, 2), strides=None, padding='valid')(b0)
    e0 = Dropout(0.5)(d0)

    c1 = Convolution2D(16, (3, 3), activation='relu', strides=(1, 1), padding='same')(e0)
    b1 = BatchNormalization()(c1)
    d1 = MaxPooling2D(pool_size=(2, 2), strides=None, padding='valid')(b1)
    e1 = Dropout(0.5)(d1)

    c2 = Convolution2D(32, (3, 3), activation='relu', strides=(1, 1), padding='same')(e1)
    b2 = BatchNormalization()(c2)
    d2 = MaxPooling2D(pool_size=(2, 2), strides=None, padding='valid')(b2)
    e2 = Dropout(0.5)(d2)

    f = Flatten()(e2)
    z0 = Dense(64, activation='softmax', kernel_regularizer=l2(0.0001))(f)
    z1 = Dense(32, activation='softmax', kernel_regularizer=l2(0.0001))(z0)
    y_out = Dense(1, activation='sigmoid')(z1)

    return Model(inputs=x_in, outputs=y_out)


def get_prepared_data(data_dir='deepmerge/prepared_data'):
    return [load_by_name(name, data_dir) for name in [
        'X_train',
        'X_valid',
        'X_test',
        'y_train',
        'y_valid',
        'y_test'
    ]]

def load_by_name(name, data_dir):
        path = os.path.join(data_dir, name + '.npy')
        with open(path, 'r') as f: 
            return np.load(path)


if __name__ == '__main__':

    cnn = get_cnn_architecture()
    prepared_data = get_prepared_data()
    X_train, X_valid, X_test, y_train, y_valid, y_test = prepared_data

    optimizer = 'adam'
    fit_metrics = ['accuracy']
    loss = 'binary_crossentropy'
    cnn.compile(loss=loss, optimizer=optimizer, metrics=fit_metrics)

    nb_epoch = 2
    batch_size = 128
    shuffle = True

    # model checkpoints will be saved here (only the best)
    # directory "latest", checkpoint name "model"
    model_save_dir = 'deepmerge/models/latest/model'
    callbacks = [
        ModelCheckpoint(model_save_dir, save_best_only=True, save_weights_only=True),
        EarlyStopping(patience=5, restore_best_weights=True)
    ]


    # Train
    history = cnn.fit(X_train, y_train, 
                    batch_size=batch_size, 
                    epochs=nb_epoch, 
                    validation_data=(X_valid, y_valid),
                    shuffle=shuffle,
                    callbacks=callbacks,
                    verbose=1)

    cnn.evaluate(X_test, y_test)
