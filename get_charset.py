import glob
from chardet.universaldetector import UniversalDetector

import os,sys
from os import listdir
from os.path import isfile, join
from tqdm import tqdm


def get_charset(fp):
    detector = UniversalDetector()

    detector.reset()
    for line in file(fp, 'rb'):
        detector.feed(line)
        if detector.done: break
    detector.close()
    return detector.result

if __name__ == '__main__':
    filename = sys.argv[1]
    for film in tqdm(listdir(filename)):
        # print(film)
        film_path = os.path.join(filename, film)
        # for file in listdir(film_path):
        #     file_path_s = os.path.join(film_path, file)
        #     print(file_path_s)
    #     film_path = os.path.join(filename, film)
    # for file in tqdm(listdir(filename)):
    #       file_path = os.path.join(filename, file)
        # if file.endswith('.srt'):
        print(get_charset(film_path).get('encoding'))
    # print(get_charset(filename).get('encoding'))
