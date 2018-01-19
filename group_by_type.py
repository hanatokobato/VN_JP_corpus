import os,sys,shutil
from os import listdir
from guessit import guessit

def get_type(film_name):
    return guessit(film_name).get('type')

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


def group_film_by_type(ja_src, vi_src, dest):
    for fn in listdir(ja_src):
        film_type = get_type(fn)
        type_path = make_dir(dest, film_type)
        ja_path = make_dir(type_path, 'ja')
        film_path = os.path.join(ja_src, fn)
        copyDirectory(film_path, ja_path)

    for fn in listdir(vi_src):
        film_type = get_type(fn)
        type_path = make_dir(dest, film_type)
        vi_path = make_dir(type_path, 'vi')
        film_path = os.path.join(vi_src, fn)
        copyDirectory(film_path, vi_path)

if __name__ == '__main__':
    ja_src = sys.argv[1]
    vi_src = sys.argv[2]
    dest = sys.argv[3]
    group_film_by_type(ja_src, vi_src, dest)
