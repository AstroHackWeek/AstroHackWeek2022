from astropy.io import fits
import numpy as np

if __name__ == '__main__':

    # just a little dev script to make the data smaller by taking the first N images/labels
    # not generally advised, just makes the download quicker for a demo

    fits_loc = 'deepmerge/latest_data_untrimmed.fits'
    max_examples = 3000

    hdu = fits.open(fits_loc)
    random_indices = np.random.choice(np.arange(len(hdu[0].data)), size=max_examples, replace=False)
    hdu[0].data = hdu[0].data[random_indices]
    hdu[1].data = hdu[1].data[random_indices]

    hdu.writeto('deepmerge/latest_data.fits', overwrite=True)
