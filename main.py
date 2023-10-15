# 📌Напишите код, который запускается из командной строки и получает на вход путь
# до директории на ПК.
# 📌Соберите информацию о содержимом в виде объектов namedtuple.
# 📌Каждый объект хранит: ○ имя файла без расширения или название каталога,
#   ○ расширение, если это файл, ○ флаг каталога,
#   ○ название родительского каталога.
# 📌В процессе сбора сохраните данные в текстовый файл используя логирование.


import os
import logging
from collections import namedtuple

def data_folder_log(path_in: str):
    """Функция получения данных о директории и её содержимом

    Функция на вход принимаеи путь до папки и записывает в лог файл информацию о содержимом:
    Имя объекта, родительский каталог, типа объекта, размер"""

    logger = logging.getLogger(__name__)
    my_format = '{levelname:<4} - {msg}'
    logging.basicConfig(filename='mylog.log', filemode='w', encoding='UTF-8',
                        level=logging.INFO, style='{', format=my_format)
    for dir_path, dirs_names, files_names in os.walk(path_in):
        dir_name = os.path.basename(dir_path)
        size = get_size(dir_path)
        Dir = namedtuple('Dir', ['dir_name', 'type', 'size', 'parent_dir'])
        dir = Dir(dir_name, 'DIR', round(size/1024, 2), os.path.dirname(dir_path))

        result = f'dir_name: {dir_name:<36} {"DIR":<5}   size: {round(size/1024, 2):<10} {"KiB":<11}' \
                 f' parent_dir: {os.path.dirname(dir_path)}'
        logger.info(msg=f'{result}')


        for file in files_names:
            if '.' in file:
                *file_name, ext = str(file).split('.')
                file_name = ''.join(file_name)
            else:
                file_name = file
            file_path = os.path.join(dir_path, file)
            size = get_size(file_path)
            File = namedtuple('File', ['file_name', 'ext', 'type', 'size', 'parent_dir'])
            file1 = File('file_name', ext,'File', round(size / 1024, 2), os.path.dirname(file_path))

            result = f'file_name: {file_name:<16} ext: {ext:<13} {"File":<7} size: {round(size / 1024, 2):<10} {"KiB":<10} ' \
                     f' parent_dir: {os.path.dirname(file_path)}'
            logger.info(msg=f'{result}')
    # return result


def get_size(p):
    """Функция определения размера файла или папки

    Функция на вход принимаеи путь до объекта и возвращает его размер"""

    size = 0
    if os.path.isfile(p):
        size = os.path.getsize(p)
    if os.path.isdir(p):
        for dir_path, dir_name, files_names in os.walk(p):
            for file_name in files_names:
                file_path = os.path.join(dir_path, file_name)
                size += os.path.getsize(file_path)
    return size



# print(os.path.join(os.getcwd()))
path_dir = os.path.join(os.getcwd(), 'venv')
data = data_folder_log(path_dir)