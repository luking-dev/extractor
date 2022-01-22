#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sys import argv, exit
import os


class Extractor:
    file = None
    cmd = None
    
    def _identify_ext(self):
        if self.file.endswith('.tar.gz'):
            cmd = 'tar xvzf'
        elif self.file.endswith('.tar.bz2'):
            cmd = 'tar xvjf'
        elif self.file.endswith('.tar'):
            cmd = 'tar xvf'
        elif self.file.endswith('.gz'):
            cmd = 'gzip -d'
        elif self.file.endswith('.bz2'):
            cmd = 'bzip -d'
        elif self.file.endswith('.zip'):
            cmd = 'unzip'
        elif self.file.endswith('.rar'):
            cmd = 'rar -x'

        return f'{cmd} {file}'

    def extract(self, file, dir):
        self.file = file
        os.system(f'{self._identify_ext()} {dir}')
        print(f'Files has been extracted to: {dir}')

if __name__ == '__main__':
    if len(argv) > 1:
        file = argv[1]
        e = Extractor()
        e.extract(file, argv[2]) if len(argv) > 2 else e.extract(file, os.getcwd())
    else:
        exit(1)
    
