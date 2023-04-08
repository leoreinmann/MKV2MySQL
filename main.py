import enzyme
import os
import json
import sql_connection
import ast

def main():
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

                dict_data_audio_list = []

                for a in audio:
                    a_str =  str(a).replace("True", "true").replace("False", "false").replace("None", "null").replace("\'", "\"")
                    print(a_str)
                    
                    dict_audio_data = json.loads(a_str)

                    print(dict_audio_data["name"])

                    dict_data_audio_list.append(dict_audio_data)
                
                for v in video:
                    v_str = str(v).replace("True", "true").replace("False", "false").replace("None", "null").replace("\'", "\"")
                    print(v_str)

                    dict_video_data = json.loads(v_str)
            
            
            sql_connection.insert_movie(name, dict_video_data, dict_data_audio_list) #name, video_data, audio_data_list



if __name__ == '__main__':
    main()
    



                


                

                