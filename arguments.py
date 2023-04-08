import argparse

parser = argparse.ArgumentParser(description='App scans through a directory and stores metadata of .mkv files into a MySQL database')
parser.add_argument('database_name', type=str, help='the name of the database')
parser.add_argument('database_user', type=str, help='the user to connect to the database')
parser.add_argument('database_password', type=str, help='the password to connect to the database')
parser.add_argument('folder', type=str, help='the folder containing the .mkv files')

args = parser.parse_args()

# access the arguments using args.database_name, args.database_user, args.database_password, and args.folder
