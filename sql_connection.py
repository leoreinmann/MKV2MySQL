import mysql.connector
import json

def connect_to_database():
    return mysql.connector.connect(
        host="localhost",
        user="movie",
        password="1234",
        database="moviedb"
    )

def insert_movie(title, video_data, audio_data_list):
    create_tables()
    db = connect_to_database()
    cursor = db.cursor()

    # Check if the movie already exists
    select_query = "SELECT id FROM movie WHERE title = %s"
    cursor.execute(select_query, (title,))
    result = cursor.fetchone()
    if result:
        print(f"Movie '{title}' already exists in the database, skipping insertion.")
        return

    # Insert movie data
    movie_query = "INSERT INTO movie (title) VALUES (%s)"
    movie_values = (title,)
    cursor.execute(movie_query, movie_values)
    movie_id = cursor.lastrowid

    # Insert video data
    video_query = "INSERT INTO video_track (movie_id,codec_id, display_height) VALUES (%s, %s, %s)"
    video_values = (movie_id, video_data['codec_id'], video_data['display_height'])
    cursor.execute(video_query, video_values)
    video_id = cursor.lastrowid

    # Insert audio data
    audio_ids = []
    for audio_data in audio_data_list:
        audio_query = "INSERT INTO audio_track (name, codec_id, language, movie_id) VALUES (%s, %s, %s, %s)"
        audio_values = (audio_data['name'], audio_data['codec_id'], audio_data['language'], movie_id)
        cursor.execute(audio_query, audio_values)
        audio_ids.append(cursor.lastrowid)

    # Insert JSON data
    json_data = {
        "title": title,
        "video_data": video_data,
        "audio_data_list": audio_data_list
    }
    json_query = "INSERT INTO movie_json (movie_id, json_data) VALUES (%s, %s)"
    json_values = (movie_id, json.dumps(json_data))
    cursor.execute(json_query, json_values)

    db.commit()
    db.close()


def create_tables():
    db = connect_to_database()

    cursor = db.cursor()

    # Create "movie" table
    cursor.execute("CREATE TABLE IF NOT EXISTS movie (id INT AUTO_INCREMENT PRIMARY KEY, title VARCHAR(255))")

    # Create "video_track" table
    cursor.execute("CREATE TABLE IF NOT EXISTS video_track (id INT AUTO_INCREMENT PRIMARY KEY, display_height INT, codec_id VARCHAR(255), movie_id INT, FOREIGN KEY (movie_id) REFERENCES movie(id))")

    # Create "audio_track" table
    cursor.execute("CREATE TABLE IF NOT EXISTS audio_track (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), codec_id VARCHAR(255), language VARCHAR(255), movie_id INT, FOREIGN KEY (movie_id) REFERENCES movie(id))")

    # Create "movie_json" table
    cursor.execute("CREATE TABLE IF NOT EXISTS movie_json (id INT AUTO_INCREMENT PRIMARY KEY, movie_id INT, json_data TEXT, FOREIGN KEY (movie_id) REFERENCES movie(id))")

    db.commit()
    db.close()