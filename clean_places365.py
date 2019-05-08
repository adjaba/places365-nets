from progressbar import ProgressBar, Bar, Percentage
from imageio import imread
import numpy as np
import json
import sys
import os


def main(filename):
    # create meta directory if not present
    if not os.path.exists('meta'):
        os.mkdir('meta')

    # read the 'train' or 'val' set filepaths
    filepath = os.path.join('places365_standard', '{}.txt'.format(filename))
    files = None
    with open(filepath, 'r') as fp:
        files = [x.strip() for x in fp.readlines()]

    # meta dictionary for training set
    meta = {'sum': [0] * 3, 'cnt': 0}

    # read the files
    with open('{}.txt'.format(filename), 'w') as fp:
        bar = ProgressBar(widgets=[Bar('=', '[', ']'), ' ', Percentage()],
                          maxval=len(files)).start()
        for i, file in enumerate(files):
            # read the image at i'th position
            img = imread(os.path.join('places365_standard', file))

            # remove if the image if grayscale
            if len(img.shape) == 2 or img.shape[2] == 1:
                print('Skipping file - {}'.format(file))
                del img
                continue

            # if reading from train partition, update the min and max
            if filename == 'train':
                img_sum = img.sum(axis=(0, 1))
                for i in range(img.shape[2]):
                    meta['sum'][i] += int(img_sum[i])
                meta['cnt'] = meta['cnt'] + 1

            # delete the image object
            del img

            # write the filepath to file
            fp.write('{}\n'.format(file))
            bar.update(i + 1)
        bar.finish()

    # replace the existing file inside places365_standard
    os.rename('{}.txt'.format(filename),
              os.path.join('places365_standard', '{}.txt'.format(filename)))

    # dump the meta dictionary into meta directory
    if filename == 'train':
        print(meta)
        json.dump(meta, open(os.path.join('meta', 'meta_places365.json'), 'w'))


if __name__ == '__main__':
    main(sys.argv[1])
