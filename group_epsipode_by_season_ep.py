import os,sys,shutil
from os import listdir
from guessit import guessit
from tqdm import tqdm
from shutil import copyfile

def get_ep(srt_name):
    ep = str(guessit(srt_name).get('episode'))
    if ep == 'None':
        try:
            e_index = srt_name.index('E')
        except ValueError:
            return 'None'
        begin = e_index + 1
        end = e_index + 3
        try:
            ep = int(srt_name[begin:end])
            ep = str(ep)
        except ValueError:
            return 'None'
    return 'episode' + ep

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

def group_film_by_ep(epsipode_path):
    for name in listdir(epsipode_path):
        name_path = os.path.join(epsipode_path, name)
        for season in listdir(name_path):
            season_path = os.path.join(name_path, season)
            ja_path = os.path.join(season_path, 'ja')
            vi_path = os.path.join(season_path, 'vi')

            if os.path.exists(ja_path):
                for fn in tqdm(listdir(ja_path)):
                    srt_path = os.path.join(ja_path, fn)
                    ep = get_ep(fn)
                    ep_path = make_dir(season_path, ep)
                    new_ja_path = make_dir(ep_path, 'ja')
                    copyfile(srt_path, os.path.join(new_ja_path, fn))
                    os.remove(srt_path)
                shutil.rmtree(ja_path)

            if os.path.exists(vi_path):
                for fn in tqdm(listdir(vi_path)):
                    srt_path = os.path.join(vi_path, fn)
                    ep = get_ep(fn)
                    ep_path = make_dir(season_path, ep)
                    new_vi_path = make_dir(ep_path, 'vi')
                    copyfile(srt_path, os.path.join(new_vi_path, fn))
                    os.remove(srt_path)
                shutil.rmtree(vi_path)


if __name__ == '__main__':
    epsipode_path = sys.argv[1]
    group_film_by_ep(epsipode_path)
