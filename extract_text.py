import sys, os
from os import listdir
from os.path import isfile, join
import string
from tqdm import tqdm
import enchant
import re

def clean_caption(x):
    """ cleans a caption (from corpus_generation/utils.py)
    """
    x = x.strip()                            # strip ends

    ja_parens      = re.compile('\xef\xbc\x88.*?\xef\xbc\x89')
    ja_rightarrow  = re.compile('\xe2\x86\x92')
    actor          = re.compile('[\w ]+:')
    unwanted       = re.compile('[*#]')
    brackets       = re.compile('\<.*?\>|{.*?}|\(.*?\)|\[.*?\]')
    newlines       = re.compile('\\\\n|\n')
    site_signature = re.compile('.*subtitles.*\n?|.*subs.*\n?', re.IGNORECASE)
    urls           = re.compile('www.*\s\n?|[^\s]*\. ?com\n?')
    msc            = re.compile('\\\\|\t|\\\\t|\r|\\\\r')
    encoding_error = re.compile('0000,0000,0000,\w*?')
    multi_space    = re.compile('[ ]+')

    # to and from unicode for regex to work
    # x = unicode(ja_parens.sub('', x.encode('utf8')), 'utf8')
    # x = unicode(ja_rightarrow.sub('', x.encode('utf8')), 'utf8')
    x = actor.sub('', x)
    x = unwanted.sub('', x)
    x = brackets.sub('', x)
    x = site_signature.sub('', x)
    x = urls.sub('', x)
    x = msc.sub('', x)
    x = encoding_error.sub('', x)
    x = newlines.sub(' ', x)
    x = multi_space.sub(' ', x)
    x = x.strip()

    return x

def is_time_stamp(l):
    if len(l) > 2 and is_number(l[:2]) and l[2] == ':':
        return True
    return False

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False

def has_letters(line):
    if re.search('[a-zA-Z]', line):
        return True
    return False

def has_no_text(line):
    l = line.strip()
    if not len(l):
        return True
    if is_number(l):
        return True
    if is_time_stamp(l):
        return True
    if l[0] == '(' and l[-1] == ')':
        return True
    return False

def not_in_format(file_path):
    file = open(file_path)
    lines = file.readlines()
    check = 0
    count = 0
    for line in lines:
        if is_time_stamp(line):
            check += 1
        count += 1
        if count == 20:
            break
    return check == 0


def clean_up(lines):
    """
    Get rid of all non-text lines and
    try to combine text broken into multiple lines
    """
    new_lines = []
    previous_line = ''
    for line in tqdm(lines[1:]):
        if has_no_text(line):
            previous_line = line
            continue
        else:
            cleaned_line = clean_caption(line).lstrip('- ')
            if has_no_text(cleaned_line):
                previous_line = line
                continue

            if len(new_lines) and (not is_time_stamp(previous_line)) and has_letters(cleaned_line):
                #combine with previous line
                new_lines[-1] = new_lines[-1].strip() + ' ' + cleaned_line + '\n'
            else:
                #append line
                new_lines.append(cleaned_line + '\n')
            previous_line = line
    return new_lines

def make_dir(path, name):
    directory = os.path.join(path, name)

    if not os.path.exists(directory):
        os.makedirs(directory)

    return directory

def write_to_txt(file_path, dest):
    file = open(file_path)
    lines = file.readlines()
    new_lines = clean_up(lines)
    new_file_name = file_path.split('/')[-1][:-4] + '.txt'
    new_file_path = os.path.join(dest, new_file_name)
    with open(new_file_path, 'w') as f:
        for line in new_lines:
            f.write(line)

def extract_text(src, dest):
    for film_name in listdir(src):
        film_path = os.path.join(src, film_name)
        new_folder_path = make_dir(dest, film_name)

        for srt_file in listdir(film_path):
            file_path = os.path.join(film_path, srt_file)
            if not_in_format(file_path):
                continue
            write_to_txt(file_path, new_folder_path)


if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('UTF8')
    srt = sys.argv[1]
    dest = sys.argv[2]
    extract_text(srt, dest)
