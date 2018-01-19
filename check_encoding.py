import glob
from chardet.universaldetector import UniversalDetector

import os,sys
from os import listdir
from os.path import isfile, join


def get_charset(fp):
    detector = UniversalDetector()

    detector.reset()
    for line in file(fp, 'rb'):
        detector.feed(line)
        if detector.done: break
    detector.close()
    return detector.result


filename = sys.argv[1]
print(get_charset(filename).get('encoding'))
