import os,sys,shutil
from os import listdir
from guessit import guessit
from tqdm import tqdm
from shutil import copyfile

def remove_noise(movie_path):
    for name in listdir(movie_path):
        name_path = os.path.join(movie_path, name)
        ja_path = os.path.join(name_path, 'ja')
        vi_path = os.path.join(name_path, 'vi')

        if os.path.exists(ja_path):
            for folder_name in listdir(ja_path):
                folder_name_path = os.path.join(ja_path, folder_name)
                for fn in listdir(folder_name_path):
                    if fn.endswith('.txt'):
                        srt_path = os.path.join(folder_name_path, fn)
                        copyfile(srt_path, os.path.join(ja_path, fn))
                        os.remove(srt_path)
                shutil.rmtree(folder_name_path)

        if os.path.exists(vi_path):
            for folder_name in listdir(vi_path):
                folder_name_path = os.path.join(vi_path, folder_name)
                for fn in listdir(folder_name_path):
                    if fn.endswith('.txt'):
                        srt_path = os.path.join(folder_name_path, fn)
                        copyfile(srt_path, os.path.join(vi_path, fn))
                        os.remove(srt_path)
                shutil.rmtree(folder_name_path)

if __name__ == '__main__':
    movie_path = sys.argv[1]
    remove_noise(movie_path)
