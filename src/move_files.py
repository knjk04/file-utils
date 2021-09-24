import os
import sys
from os import listdir # TODO: why do we need to import os twice?
from pathlib import Path

from src.create_dir import create_numbered_dirs, get_parent_dir


# TODO: ignore folders
from src.validate_windows_file_name import is_valid_windows_file_name


def get_files_in(dir: str):
    """Returns a list of absolute paths to files sorted alphabetically in the specified folder"""
    return [dir + '\\' + file for file in listdir(dir) if os.path.isfile(os.path.join(dir, file))]


def create_new_dirs(parent_dir: str, number_of_dirs: int):
    start = 1
    return create_numbered_dirs(parent_dir, start, number_of_dirs)


def move_files(path_to_files: [str], destinations: [str], new_file_name: str):
    """
    Assumes that every file in the parameter files is an absolute path to a file.
    Also assumes that both parameters are non-empty lists
    new_file_name does not change the file extension
    """
    for index, source_path in enumerate(path_to_files):
        original_file_name = os.path.basename(source_path)
        file_extension = Path(original_file_name).suffix
        # don't want to set this expression to new_file_name because it will overwrite the value and affect subsequent
        # iterations of the loop
        new_file_name2 = new_file_name + file_extension
        dest = os.path.join(destinations[index], new_file_name2)
        os.rename(source_path, dest)
        print(f'Moved {original_file_name}...')


def ask_for_file_name():
    for i in range(3):
        print('What do you want to to use for the new file names ?', sep='')
        file_name = input()
        if is_valid_windows_file_name(file_name):
            return file_name
        print('Invalid file name. Try again.')
    print('Error: you did not enter in a valid name after 3 attempts. Exiting...')
    sys.exit()


def main():
    parent_dir = get_parent_dir()
    files = get_files_in(parent_dir)
    if not files:
        print(f'Cannot find any files in {parent_dir}')
        sys.exit()

    new_dirs = create_new_dirs(parent_dir, len(files))
    if not new_dirs:
        print(f'Could not create new directories. Perhaps those directories already exist in {parent_dir}?')
        sys.exit()

    move_files(files, new_dirs, ask_for_file_name())


if __name__ == '__main__':
    main()
