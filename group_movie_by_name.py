import os,sys,shutil
from os import listdir
from guessit import guessit
from tqdm import tqdm

def get_name(film_name):
    return film_name.split('_')[0]

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

def group_film_by_name(movie_path):
    ja_path = os.path.join(movie_path, 'ja')
    vi_path = os.path.join(movie_path, 'vi')
    for fn in tqdm(listdir(ja_path)):
        film_path = os.path.join(ja_path, fn)
        film_name = get_name(fn)
        name_path = make_dir(movie_path, film_name)
        new_ja_path = make_dir(name_path, 'ja')
        copyDirectory(film_path, new_ja_path)
        shutil.rmtree(film_path)
    shutil.rmtree(ja_path)

    for fn in tqdm(listdir(vi_path)):
        film_path = os.path.join(vi_path, fn)
        film_name = get_name(fn)
        name_path = make_dir(movie_path, film_name)
        new_vi_path = make_dir(name_path, 'vi')
        copyDirectory(film_path, new_vi_path)
        shutil.rmtree(film_path)
    shutil.rmtree(vi_path)

if __name__ == '__main__':
    movie_path = sys.argv[1]
    group_film_by_name(movie_path)
