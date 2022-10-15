import argparse

import urllib.request


if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        'Download data',
        'Download simulated merger images and labels',
    )
    parser.add_argument('fits_loc', default='deepmerge/latest_data.fits')
    parser.add_argument('--noise', dest='noise', default=False, action='store_true')

    args = parser.parse_args()

    if args.noise:
        version = 'noise'
    else:
        version = 'pristine'

    fits_url = 'https://archive.stsci.edu/hlsps/deepmerge/hlsp_deepmerge_hst-jwst_acs-wfc3-nircam_illustris-z2_f814w-f160w-f356w_v1_sim-'+version+'.fits'
    
    print('Downloading from {} to {} - please wait'.format(fits_url, args.fits_loc))
    urllib.request.urlretrieve(fits_url, args.fits_loc)
