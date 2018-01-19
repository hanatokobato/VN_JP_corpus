import os,sys,shutil
from os import listdir
from extract_text import not_in_format

def one_one_sub(ep_path, mo_path):
    def check_one_one(ep):
        ja_dir = os.path.join(ep, 'ja')
        vi_dir = os.path.join(ep, 'vi')
        if not os.path.exists(ja_dir) or not os.path.exists(vi_dir):
            return False
        ja_count = len(listdir(ja_dir))
        vi_count = len(listdir(vi_dir))
        return ja_count == 1 and vi_count == 1

    count = 0
    for film in listdir(ep_path):
        film_path = os.path.join(ep_path, film)
        for season in listdir(film_path):
            season_path = os.path.join(film_path, season)
            for ep in listdir(season_path):
                ep_path_s = os.path.join(season_path, ep)
                if check_one_one(ep_path_s):
                    print(ep_path_s)
                    count += 1

    for film in listdir(mo_path):
        film_path = os.path.join(mo_path, film)
        if check_one_one(film_path):
            count += 1

    return count

def not_zero_sub(ep_path, mo_path):
    count = 0
    for name in listdir(ep_path):
        name_path = os.path.join(ep_path, name)
        for season in listdir(name_path):
            season_path = os.path.join(name_path, season)
            count += len(listdir(season_path))

    count += len(listdir(mo_path))
    return count

def error_sub(utf8_path, extract_path):
    utf8_count = 0
    for folder in listdir(utf8_path):
        folder_path = os.path.join(utf8_path, folder)
        utf8_count += len(listdir(folder_path))

    extract_count = 0
    for folder in listdir(extract_path):
        folder_path = os.path.join(extract_path, folder)
        extract_count += len(listdir(folder_path))

    count = utf8_count - extract_count
    return count

def zero_n_sub(ep_path, mo_path):
    def check_zero(ep):
        ja_dir = os.path.join(ep, 'ja')
        if not os.path.exists(ja_dir):
            return True
        ja_count = len(listdir(ja_dir))
        return ja_count == 0

    count = 0
    for film in listdir(ep_path):
        film_path = os.path.join(ep_path, film)
        for season in listdir(film_path):
            season_path = os.path.join(film_path, season)
            for ep in listdir(season_path):
                ep_path_s = os.path.join(season_path, ep)
                if check_zero(ep_path_s):
                    print(ep_path_s)
                    count += 1

    for film in listdir(mo_path):
        film_path = os.path.join(mo_path, film)
        if check_zero(film_path):
            count += 1

    return count

def m_zero_sub(ep_path, mo_path):
    def check_zero(ep):
        vi_dir = os.path.join(ep, 'vi')
        if not os.path.exists(vi_dir):
            return True
        vi_count = len(listdir(vi_dir))
        return vi_count == 0

    count = 0
    for film in listdir(ep_path):
        film_path = os.path.join(ep_path, film)
        for season in listdir(film_path):
            season_path = os.path.join(film_path, season)
            for ep in listdir(season_path):
                ep_path_s = os.path.join(season_path, ep)
                if check_zero(ep_path_s):
                    print(ep_path_s)
                    count += 1

    for film in listdir(mo_path):
        film_path = os.path.join(mo_path, film)
        if check_zero(film_path):
            count += 1

    return count

def one_n_sub(ep_path, mo_path):
    def check_zero(ep):
        ja_dir = os.path.join(ep, 'ja')
        vi_dir = os.path.join(ep, 'vi')
        if not os.path.exists(ja_dir) or not os.path.exists(vi_dir):
            return False
        ja_count = len(listdir(ja_dir))
        vi_count = len(listdir(vi_dir))
        return ja_count == 1 and vi_count > 1

    count = 0
    for film in listdir(ep_path):
        film_path = os.path.join(ep_path, film)
        for season in listdir(film_path):
            season_path = os.path.join(film_path, season)
            for ep in listdir(season_path):
                ep_path_s = os.path.join(season_path, ep)
                if check_zero(ep_path_s):
                    print(ep_path_s)
                    count += 1

    for film in listdir(mo_path):
        film_path = os.path.join(mo_path, film)
        if check_zero(film_path):
            count += 1

    return count

def m_one_sub(ep_path, mo_path):
    def check_zero(ep):
        ja_dir = os.path.join(ep, 'ja')
        vi_dir = os.path.join(ep, 'vi')
        if not os.path.exists(ja_dir) or not os.path.exists(vi_dir):
            return False
        ja_count = len(listdir(ja_dir))
        vi_count = len(listdir(vi_dir))
        return ja_count > 1 and vi_count == 1

    count = 0
    for film in listdir(ep_path):
        film_path = os.path.join(ep_path, film)
        for season in listdir(film_path):
            season_path = os.path.join(film_path, season)
            for ep in listdir(season_path):
                ep_path_s = os.path.join(season_path, ep)
                if check_zero(ep_path_s):
                    print(ep_path_s)
                    count += 1

    for film in listdir(mo_path):
        film_path = os.path.join(mo_path, film)
        if check_zero(film_path):
            count += 1

    return count


def zero_zero(ep_path, mo_path):
    def check_zero(ep):
        ja_dir = os.path.join(ep, 'ja')
        vi_dir = os.path.join(ep, 'vi')
        if not os.path.exists(ja_dir) and not os.path.exists(vi_dir):
            return True

        return False
        # ja_count = len(listdir(ja_dir))
        # vi_count = len(listdir(vi_dir))
        # return ja_count == 0 and vi_count == 0

    count = 0
    for film in listdir(ep_path):
        film_path = os.path.join(ep_path, film)
        for season in listdir(film_path):
            season_path = os.path.join(film_path, season)
            for ep in listdir(season_path):
                ep_path_s = os.path.join(season_path, ep)
                if check_zero(ep_path_s):
                    print(ep_path_s)
                    count += 1

    for film in listdir(mo_path):
        film_path = os.path.join(mo_path, film)
        if check_zero(film_path):
            count += 1

    return count

def m_n_sub(ep_path, mo_path):
    def check_many(ep):
        ja_dir = os.path.join(ep, 'ja')
        vi_dir = os.path.join(ep, 'vi')
        if not os.path.exists(ja_dir) or not os.path.exists(vi_dir):
            return False
        ja_count = len(listdir(ja_dir))
        vi_count = len(listdir(vi_dir))
        return ja_count > 1 and vi_count > 1

    count = 0
    for film in listdir(ep_path):
        film_path = os.path.join(ep_path, film)
        for season in listdir(film_path):
            season_path = os.path.join(film_path, season)
            for ep in listdir(season_path):
                ep_path_s = os.path.join(season_path, ep)
                if check_many(ep_path_s):
                    print(ep_path_s)
                    count += 1

    for film in listdir(mo_path):
        film_path = os.path.join(mo_path, film)
        if check_many(film_path):
            count += 1

    return count

if __name__ == '__main__':
    # ep_path = sys.argv[1]
    # mo_path = sys.argv[2]
    # print(one_one_sub(ep_path, mo_path))

    # ep_path = sys.argv[1]
    # mo_path = sys.argv[2]
    # print(not_zero_sub(ep_path, mo_path))

    # utf8_path = sys.argv[1]
    # extract_path = sys.argv[2]
    # print(error_sub(utf8_path, extract_path))

    # ep_path = sys.argv[1]
    # mo_path = sys.argv[2]
    # print(zero_n_sub(ep_path, mo_path))

    # ep_path = sys.argv[1]
    # mo_path = sys.argv[2]
    # print(m_zero_sub(ep_path, mo_path))

    # ep_path = sys.argv[1]
    # mo_path = sys.argv[2]
    # print(zero_zero(ep_path, mo_path))

    ep_path = sys.argv[1]
    mo_path = sys.argv[2]
    print(m_n_sub(ep_path, mo_path))

    # mot nhieu
    # ep_path = sys.argv[1]
    # mo_path = sys.argv[2]
    # print(one_n_sub(ep_path, mo_path))

    # nhieu mot
    # ep_path = sys.argv[1]
    # mo_path = sys.argv[2]
    # print(m_one_sub(ep_path, mo_path))
