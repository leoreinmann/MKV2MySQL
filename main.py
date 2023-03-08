import enzyme
import os



if __name__ == '__main__':
    rootdir = '/home/host/movies'

    for subdir, dirs, files in os.walk(rootdir):
        name = str(subdir.rsplit('/', 1)[-1]) # Title (YEAR)
        title = ''
        year = ''
        if '(' in name:
            year = name.split('(', 1)[-1][:-1]
            title = name.split('(', 1)[0]


        if files:
            print(title)
            with open(str(subdir) + '/' + str(files[0]), 'rb') as f:
                mkv = enzyme.MKV(f)

                audio = mkv.audio_tracks
                video = mkv.video_tracks
                print(str(video))
