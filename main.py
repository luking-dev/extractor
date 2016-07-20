#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse, sys
from os import name, system


class Registry(object):
    def extract(self, archive, dir):
        filename = archive.split('.')
        if len(filename) == 2:
            extension = filename[1]
        elif len(filename) == 3:
            extension = []
            extension[0] = filename[1]
            extension[1] = filename[2]

        # Identify file extension
        if extension[0] == 'tar':
            if len(extension) == 1:
                # tar file
                cmd = 'tar xvf '
            elif len(extension) == 2 or extension[0] == 'tgz':
                if extension[1] == 'gz' or extension[0] == 'tgz':
                    # tar.gz file
                    cmd = 'tar xvzf '
                elif extension[1] == 'bz2':
                    # tar.bz2 file
                    cmd = 'tar xvjf '
        elif extension[0] == 'bz2':
            cmd = 'bzip -d '
        elif extension[0] == 'gz':
            cmd = 'gzip -d '
        elif extension[0] == 'zip':
            cmd = 'unzip '
        elif extension[0] == 'rar':
            cmd = 'rar -x '

        return cmd + self.archive + ' ' + self.directorie


def check_dir(dir):
    if len(dir) == 0:
        if os_name() == 'posix':
            return '.'
        else:
            return ''

if __name__ == '__main__':
    file = sys.argv[1]
    dir_from = check_dir(sys.argv[2])
    dir_to = check_dir(sys.argv[3])
    e = Registry()
    e.extract(file, dir_from)
    print "File extracted to '{0}'".format(dir_to)

    '''parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose", help="Mostrar información de depuración", action="store_true")
    parser.add_argument("-f", "--file", help="Nombre de archivo a procesar", action="store_true")
    args = parser.parse_args()

    # Process each argument
    if args.verbose:
        print "depuración activada!!!"
    if args.file:
        print "El nombre de archivo a procesar es: ", args.file'''


    '''a = raw_input('> Extract: ')
    a = a.split()
    if len(a) == 1:
        archive = a
        if os_name() == 'posix':
            directorie = '.'
        else:
            directorie = ''
    elif len(a) == 2:
        archive = a[0]
        directorie = a[1]'''
