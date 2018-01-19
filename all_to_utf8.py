import glob
from chardet.universaldetector import UniversalDetector

import os,sys
from os import listdir
from os.path import isfile, join
from tqdm import tqdm
from shutil import copyfile

def make_dir(path, name):
    directory = os.path.join(path, name)

    if not os.path.exists(directory):
        os.makedirs(directory)

    return directory

def to_utf8(all_sub_path, utf8_sub_path):
    """Given a file path, converts that file in-place to utf-8
    """

    def get_charset(fp):
        detector = UniversalDetector()

        detector.reset()
        for line in file(fp, 'rb'):
            detector.feed(line)
            if detector.done: break
        detector.close()
        return detector.result

    for folder_name in tqdm(listdir(all_sub_path)):
        folder_path = os.path.join(all_sub_path, folder_name)
        new_folder_path = make_dir(utf8_sub_path, folder_name)

        for file_name in listdir(folder_path):
            if file_name.endswith('.srt'):
                file_path = os.path.join(folder_path, file_name)
                charset = get_charset(file_path).get('encoding')
                new_file_path = os.path.join(new_folder_path, file_name)

                if charset == 'SHIFT_JIS' or charset == 'UTF-16LE':
                    command = 'iconv -f ' + str(charset) + ' -t UTF-8 "' + file_path + '" -o "' + new_file_path + '"'
                    os.system(command)
                else:
                    copyfile(file_path, new_file_path)

if __name__ == '__main__':
    folder_path = sys.argv[1]
    utf8_sub_path = sys.argv[2]
    to_utf8(folder_path, utf8_sub_path)
