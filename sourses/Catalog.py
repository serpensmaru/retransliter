from os import listdir, chdir, rename
from re import search


class Catalog:
    """ Класс для управления файловой системой"""
    def __init__(self, path):
        self.path = r"{}".format(path)
        self.tuple_dir = self.list_file()

    def list_file(self):
        """ Возвращает список файлов в директории и создает атрибут класса"""
        self.tuple_dir = tuple(listdir(self.path))
        return self.tuple_dir

    @staticmethod
    def expansion_file(name_file, reg=r"(\w+).(.*)"):
        """ Возвращает имя файла и его расширение"""
        mirror = name_file[::-1]
        group_mirror = search(reg, mirror)
        expansion = group_mirror.group(1)[::-1]
        file_name = group_mirror.group(2)[::-1]
        return file_name, expansion

    def go_path(self):
        chdir(self.path)

    def rename_file(self, old_name, new_name):
        """ Переименовывает файлы, предварительно нужно вызвать метод list_file()"""
        if old_name in self.tuple_dir:
            rename(old_name, new_name)
