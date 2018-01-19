import os,sys,shutil
from os import listdir
from guessit import guessit
from tqdm import tqdm
from shutil import copyfile

def get_season(srt_name):
    season = str(guessit(srt_name).get('season'))
    if season == 'None':
        try:
            s_index = srt_name.index('S')
        except ValueError:
            return 'None'
        begin = s_index + 1
        end = s_index + 3
        try:
            season = int(srt_name[begin:end])
            season = str(season)
        except ValueError:
            return 'None'
    return 'season' + season

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

def group_film_by_season(epsipode_path):
    for name in listdir(epsipode_path):
        name_path = os.path.join(epsipode_path, name)
        ja_path = os.path.join(name_path, 'ja')
        vi_path = os.path.join(name_path, 'vi')

        if os.path.exists(ja_path):
            for fn in tqdm(listdir(ja_path)):
                film_path = os.path.join(ja_path, fn)
                for fm in listdir(film_path):
                    if fm.endswith('.txt'):
                        srt_path = os.path.join(film_path, fm)
                        season = get_season(fm)
                        season_path = make_dir(name_path, season)
                        new_ja_path = make_dir(season_path, 'ja')
                        copyfile(srt_path, os.path.join(new_ja_path, fm))
                        os.remove(srt_path)
                    else:
                        continue
                shutil.rmtree(film_path)
            shutil.rmtree(ja_path)

        if os.path.exists(vi_path):
            for fn in tqdm(listdir(vi_path)):
                film_path = os.path.join(vi_path, fn)
                for fm in listdir(film_path):
                    if fm.endswith('.txt'):
                        srt_path = os.path.join(film_path, fm)
                        season = get_season(fm)
                        season_path = make_dir(name_path, season)
                        new_vi_path = make_dir(season_path, 'vi')
                        copyfile(srt_path, os.path.join(new_vi_path, fm))
                        os.remove(srt_path)
                    else:
                        continue
                shutil.rmtree(film_path)
            shutil.rmtree(vi_path)


if __name__ == '__main__':
    epsipode_path = sys.argv[1]
    group_film_by_season(epsipode_path)
