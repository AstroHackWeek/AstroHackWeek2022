import os

import numpy as np
from astropy.io import fits
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


def split(X, y, random_state):
    

        # First split off 30% of the data for validation+testing
    X_train, X_split, y_train, y_split = train_test_split(X, y, test_size=0.3, random_state=random_state, shuffle=True)

        # Then divide this subset into training and testing sets
    X_valid, X_test, y_valid, y_test = train_test_split(X_split, y_split, test_size=0.666, random_state=random_state, shuffle=True)

    return X_train, y_train, X_valid, y_valid, X_test, y_test


def normalise(X):
    # divide each channel by channel mean
    channel_means = X.mean(axis=(0, 1, 2))
    return X / channel_means



if __name__ == '__main__':

    fits_loc = 'deepmerge/latest_data.fits'

    hdu = fits.open(fits_loc)
    X = hdu[0].data.transpose(0, 2, 3, 1)  # channels last
    y = hdu[1].data


    X = np.asarray(X).astype('float32')
    y = np.asarray(y).astype('float32')

    X = normalise(X)
    print('Normalised to: ', X.mean(axis=(0, 1, 2)))

    random_state = 42
    X_train, y_train, X_valid, y_valid, X_test, y_test = split(X, y, random_state)

    prepared_data_dir = 'deepmerge/prepared_data'
    os.mkdir(prepared_data_dir)

    for name, data in [
        ('X_train', X_train),
        ('X_valid', X_valid),
        ('X_test', X_test),
        ('y_train', y_train),
        ('y_valid', y_valid),
        ('y_test', y_test)
    ]:
        path = os.path.join(prepared_data_dir, name + '.npy')
        with open(path, 'w') as f: 
            np.save(path, data)