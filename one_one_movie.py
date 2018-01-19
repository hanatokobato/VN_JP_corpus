import os,sys,shutil
from os import listdir
from guessit import guessit
from tqdm import tqdm
from shutil import copyfile


def check_not_zero(name):
    ja_dir = os.path.join(name, 'ja')
    vi_dir = os.path.join(name, 'vi')
    if not os.path.exists(ja_dir) or not os.path.exists(vi_dir):
        return False
    ja_count = len(listdir(ja_dir))
    vi_count = len(listdir(vi_dir))
    return ja_count > 0 and vi_count > 0

def make_dir(path, name):
    directory = os.path.join(path, name)

    if not os.path.exists(directory):
        os.makedirs(directory)

    return directory

def copyDirectory(src, dest):
    try:
        shutil.copytree(src, os.path.join(dest, src.split('/')[-1]))
    # Directories are the same
    except shutil.Error as e:
        print('Directory not copied. Error: %s' % e)
    # Any error saying that the directory doesn't exist
    except OSError as e:
        print('Directory not copied. Error: %s' % e)

def group_by_one_one(movie_path, one_one_path):
    for name in tqdm(listdir(movie_path)):
        name_path = os.path.join(movie_path, name)
        if check_not_zero(name_path):
            new_name_path = make_dir(one_one_path, name)
            new_ja_path = make_dir(new_name_path, 'ja')
            new_vi_path = make_dir(new_name_path, 'vi')
            ja_path = os.path.join(name_path, 'ja')
            vi_path = os.path.join(name_path, 'vi')
            ja_file = listdir(ja_path)[0]
            vi_file = listdir(vi_path)[0]
            ja_file_path = os.path.join(ja_path, ja_file)
            vi_file_path = os.path.join(vi_path, vi_file)
            copyfile(ja_file_path, os.path.join(new_ja_path, ja_file))
            copyfile(vi_file_path, os.path.join(new_vi_path, vi_file))


if __name__ == '__main__':
    movie_path = sys.argv[1]
    one_one_path = sys.argv[2]
    group_by_one_one(movie_path, one_one_path)
