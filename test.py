import os,sys,shutil
from os import listdir
from extract_text import not_in_format

# def not_in_format(file_path):
#     file = open(file_path)
#     lines = file.readlines()
#     check = 0
#     count = 0
#     for line in lines:
#         if is_time_stamp(line):
#             check += 1
#         count += 1
#         if count == 20:
#             break
#     return check == 0

def count(ep_path):
    count = 0
    for name in listdir(ep_path):
        name_path = os.path.join(ep_path, name)
        for season in listdir(name_path):
            season_path = os.path.join(name_path, season)
            count += len(listdir(season_path))
    return count

if __name__ == '__main__':
    path = sys.argv[1]
    print(count(path))
    # print(not_in_format(path))
