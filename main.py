import os



if __name__ == '__main__':
    rootdir = 'movies'

    for subdir, dirs, files in os.walk(rootdir):
        text = subdir.rsplit('/', 1)[0]
        print(subdir)