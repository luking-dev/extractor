def os_detect():
    return os.name


class Registry():
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


a = raw_input('> Extract: ')
a = a.split()
if len(a) == 1:
    archive = a
    if os_detect() == 'posix':
        directorie = '.'
elif len(a) == 2:
    archive = a[0]
    directorie = a[1]


f = Registry()
system(f.extract(archive, directorie))
