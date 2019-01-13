import shutil
import os


def main():
    print("Starting directory is: {}".format(os.getcwd()))

    # Change to desired directory
    os.chdir('FilesToSort')

    existing_dirs = []

    for filename in os.listdir('.'):
        # Ignore directories, just process files
        if os.path.isdir(filename):
            existing_dirs.append(filename)
            continue

        extension = filename.split('.')[1]
        if extension not in existing_dirs:
            # create a new dir
            try:
                os.mkdir(extension)
                existing_dirs.append(extension)
            except FileExistsError:
                print('File already exists')

        # just move the file to new folder location
        shutil.move(filename, extension + '/' + filename)

main()
