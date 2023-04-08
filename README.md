# MKV2MySQL
## Table of content
1. [General](#General)
2. [Folder strucure](#folder-structure)
3. [SQL Database](#sql-database)


## General

With [enzyme](https://pypi.org/project/enzyme/) the app scans through a directory and stores metadata of .mkv files into a MySQL database. 

## Folder structure

The folder structure must be as following:
```
├── Robocop (2014)
│   └── RoboCop_t00.mkv
├── Rocky
│   ├── Rocky (1976)
│   │   └── Rocky_t00.mkv
│   ├── Rocky 2 (1979)
│   │   └── Rocky II_t00.mkv
│   ├── Rocky 3 (1982)
│   │   └── Rocky III_t00.mkv
│   ├── Rocky 4 (1985)
│   │   └── Rocky IV_t00.mkv
│   ├── Rocky 5 (1990)
│   │   └── Rocky V_t00.mkv
│   └── Rocky Balboa (2006)
│       └── title_t00.mkv
```

Explanation: The .mkv files must be located in a folder with the naming convention ```title (YEAR)```. 
It is possible to make collections as shown with the Rocky movies, but the naming convention must be met, otherwise the program will fail.
Also make sure, that there only one .mkv file!


## SQL Database

We store the relevant audio and video properties in seperate tables, ```audio_track``` and ```video_track```. For the case we need more information about specific .mkv files, we provide the whole json from enzyme of the audio and video track.


### movie
| Field | Type         | Null | Key | Default | Extra          |
|-------|--------------|------|-----|---------|----------------|
| id    | int          | NO   | PRI | NULL    | auto_increment |
| title | varchar(255) | YES  |     | NULL    |                |



### audio_track
| Field    | Type         | Null | Key | Default | Extra          |
|----------|--------------|------|-----|---------|----------------|
| id       | int          | NO   | PRI | NULL    | auto_increment |
| name     | varchar(255) | YES  |     | NULL    |                |
| codec_id | varchar(255) | YES  |     | NULL    |                |
| language | varchar(255) | YES  |     | NULL    |                |
| movie_id | int          | YES  | MUL | NULL    |                |






### video_track
| Field          | Type         | Null | Key | Default | Extra          |
|----------------|--------------|------|-----|---------|----------------|
| id             | int          | NO   | PRI | NULL    | auto_increment |
| display_height | int          | YES  |     | NULL    |                |
| codec_id       | varchar(255) | YES  |     | NULL    |                |
| movie_id       | int          | YES  | MUL | NULL    |                |



### movie_json
| Field     | Type | Null | Key | Default | Extra          |
|-----------|------|------|-----|---------|----------------|
| id        | int  | NO   | PRI | NULL    | auto_increment |
| movie_id  | int  | YES  | MUL | NULL    |                |
| json_data | text | YES  |     | NULL    |                |
