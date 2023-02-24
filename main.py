#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, zipfile, shutil


def backupFiles(dirname):
    dir_name = dirname
    print('Respaldando...')
    extension = ".zip"
    for item in os.listdir(dir_name):
        if item.endswith(extension):
            file_name = os.path.abspath(item)
            print(file_name)

def decompress(dirname):
    dir_name = dirname
    extension = ".zip"
    print('Descomprimiendo archivos de la siguiente ruta... ' + dirname)
    os.chdir(dir_name)

    for item in os.listdir(dir_name):
        if item.endswith(extension):
            file_name = os.path.abspath(item)
            zip_ref = zipfile.ZipFile(file_name)
            zip_ref.extractall(dir_name)
            zip_ref.close()
            print('Limpiando...')
            os.remove(file_name)


def main():
  dirname = os.getcwd()
  #decompress(dirname)
  backupFiles(dirname)
if __name__ == '__main__':
  main()