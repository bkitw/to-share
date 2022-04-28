import argparse
from genericpath import exists
from pathlib import Path
from re import A
from shutil import copyfile
import os
CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k",
               "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y",
               "", "e", "yu", "ja", "je", "i", "ji", "g")

TRANS = {}

for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
    TRANS[ord(c)] = l
    TRANS[ord(c.upper())] = l.upper()



def normalize(name):
    global TRANS
    normalized = ''
    nums = '1234567890'
    for i in name:
        if i.isalpha() == False and i not in nums and not ".":
            i = '_'
            normalized += i
        else:
            normalized += i
    return normalized.translate(TRANS)

parser = argparse.ArgumentParser(description='Sorting Folder')

parser.add_argument('--source', '-s', default='jk_0', help='Source folder')
parser.add_argument('--output', '-o', default='your_sorted_trash', help='Output folder')

args = vars(parser.parse_args())

source = args.get('source')
output = args.get('output')

print(source, output)

def read_folder(path):
    restricted_dirs = ('pictures', 'videos', 'docs', 'archives', 'music')
    for el in path.iterdir():
        if el.is_dir() and os.path.dirname(el) in restricted_dirs:
            print(os.path.dirname(el))
            continue
        try:
            el.rmdir()
        except OSError:
            pass
        print(el)
        if el.is_dir():
            read_folder(el)
        else:
            copy_file(el)
            print(copy_file(el))

def copy_file(file):
    ext = file.suffix.upper()[1:]
    pictures = ('JPEG', 'PNG', 'JPG', 'SVG')
    p_name = 'pictures'
    videos = ('AVI', 'MP4', 'MOV', 'MKV')
    v_name = 'videos'
    docs = ('DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX')
    d_name = 'docs'
    archives = ('ZIP', 'GZ', 'TAR')
    a_name = 'archives'
    music = ('MP3', 'OGG', 'WAV', 'AMR', 'FLAC')
    m_name = 'music'
    if ext in pictures:
        new_path = output_folder / p_name
        new_path.mkdir(exist_ok = True, parents = True)
        copyfile(file, new_path/normalize(file.name))
    elif ext in videos:
        new_path = output_folder / v_name
        new_path.mkdir(exist_ok = True, parents = True)
        copyfile(file, new_path/normalize(file.name))
    elif ext in docs:
        new_path = output_folder / d_name
        new_path.mkdir(exist_ok = True, parents = True)
        copyfile(file, new_path/normalize(file.name))
    elif ext in archives:
        new_path = output_folder / a_name
        new_path.mkdir(exist_ok = True, parents = True)
        copyfile(file, new_path/normalize(file.name))
    elif ext in music:
        new_path = output_folder / m_name
        new_path.mkdir(exist_ok = True, parents = True)
        copyfile(file, new_path/normalize(file.name))
    else:
        pass
    known = f"{pictures}."
    not_known = ''
    files = ''
    return known
output_folder = Path(output)
read_folder(Path(source))
#print(normalize('матеріал4568%;№Н№?;$$$'))