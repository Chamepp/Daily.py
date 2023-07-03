import argparse
import os


# Define Path
def path():
    parse = argparse.ArgumentParser(
        add_help=True, description="Organize your files to different directories according to their type")
    parse.add_argument('directory_path', type=str, default='./',
                       help="The absolute path to the directory")
    return parse.parse_args().directory_path


# Data
documents = ['.log', '.txt', '.doc', '.docx', '.md', '.pdf', '.wps']
picture = ['.png', '.jpg', 'jpeg', '.bmp']
music = ['.mp3', '.wav']
compressed = ['.zip', '.rar', '.tar', '.gz', '.bz2', '.xz']
video = ['.3gp', '.mov', '.mp4', '.mkv', '.srt', '.avi']
web = ['.html', '.css', '.js']
source = ['.py', '.c', '.cpp', '.java',]

# Directories
directories = [path() + '/Compressed', path() + '/Documents',
               path() + '/Pictures', path() + '/Music', path() + '/Video', path() + '/Web', path() + '/Source-codes',]

# Confirmation
print("Script Will Start Organizing By Files Type")
print("Are You Sure You Want To Continue? (y/n)")
flag = input('>>>')
if flag.lower() == 'y':
    try:
        for d in directories:
            os.mkdir(d)
    except FileExistsError:
        pass

    # Organize
    for files in os.listdir(path()):
        dot = (files.rfind('.'))
        if dot is not 0 and dot is not -1:
            if files[dot:].lower() in music:
                os.rename(path() + '/' + files, path() + '/Music/' + files)
            if files[dot:].lower() in picture:
                os.rename(path() + '/' + files, path() + '/Pictures/' + files)
            if files[dot:].lower() in documents:
                os.rename(path() + '/' + files, path() + '/Documents/' + files)
            if files[dot:].lower() in compressed:
                os.rename(path() + '/' + files, path() +
                          '/Compressed/' + files)
            if files[dot:].lower() in video:
                os.rename(path() + '/' + files, path() + '/Video/' + files)
            if files[dot:].lower() in web:
                os.rename(path() + '/' + files, path() + '/Web/' + files)
            if files[dot:].lower() in source:
                os.rename(path() + '/' + files, path() + '/Source-codes/' + files)    

    # Clean Up
    for d in directories:
        if os.listdir(d) is None:
            os.removedirs(d)
else:
    print("Exiting")
    os.sys.exit(0)
