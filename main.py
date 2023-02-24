#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, zipfile, shutil


def backupFiles(dirname):
    dir_name = dirname
    path = os.path.join(dir_name, 'tmp')
    print('Respaldando...')
    extension = ".zip"
    for item in os.listdir(dir_name):
        if item.endswith(extension):
            file_name = os.path.abspath(item)
            print(file_name)
            shutil.copy2(file_name, path) 



def initialCheck(dirname):
    print('Revisando Ajustes Inciales')
    dir_name = dirname
    directoryCheckFlag = os.path.isdir('tmp')
    if directoryCheckFlag == False:
        path = os.path.join(dir_name, 'tmp')
        os.mkdir(path)
    print('Ajustes Finalizados')

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

def cleanZip(dirname):
    dir_name = dirname
    extension = ".zip"
    print('Descomprimiendo archivos de la siguiente ruta... ' + dirname)
    os.chdir(dir_name)
    for item in os.listdir(dir_name):
        if item.endswith(extension):
            file_name = os.path.abspath(item)
            os.remove(file_name)


def cleanasc(dirname):
    dir_name = dirname
    extension = ".asc"
    os.chdir(dir_name)
    for item in os.listdir(dir_name):
        if item.endswith(extension):
            file_name = os.path.abspath(item)
            os.remove(file_name)

def concatAsc(dirname):
    initialLine = 'Patente|Pedimento|SeccionAduanera|NumeroGuia|TipoGuia|FechaPagoReal'
    f = open("Concatenated.txt", "w")
    f.write(initialLine)
    f.close()
    dir_name = dirname
    extension = ".asc"
    os.chdir(dir_name)
    for item in os.listdir(dir_name):
        if item.endswith(extension):
            file_name = os.path.abspath(item)
            cleanFirstLine(file_name)
            merge(file_name)

def merge(filename):
    data = ''
    with open(filename) as data1:
        data = data1.read()
        data1.close()
    with open ('concatenated.txt', 'a') as fp:
        fp.write(data)
        fp.close()

def cleanFirstLine(filename):
    try:
        with open(filename, 'r') as fr:
            lines = fr.readlines()
            ptr = 1
            with open(filename, 'w') as fw:
                for line in lines:
                    if ptr != 1:
                        fw.write(line)
                    ptr += 1
        print("Deleted")
    except:
        print("Oops! something error")            

def main():
    dirname = os.getcwd()
    initialCheck(dirname)
    cleanasc(dirname)
    backupFiles(dirname)
    decompress(dirname)
    concatAsc(dirname)
    cleanasc(dirname)


if __name__ == '__main__':
    main()