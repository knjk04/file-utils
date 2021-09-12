import os
import sys
from os import listdir

from src.create_dir import create_numbered_dirs, get_parent_dir


# TODO: ignore folders
def get_files_in(dir: str):
    """Returns a list of absolute paths to files sorted alphabetically in the specified folder"""
    return [dir + '\\' + file for file in listdir(dir) if os.path.isfile(os.path.join(dir, file))]


def create_new_dirs(parent_dir: str, number_of_dirs: int):
    start = 1
    return create_numbered_dirs(parent_dir, start, number_of_dirs)


def move_files(path_to_files: [str], destinations: [str]):
    """
    Assumes that every file in the parameter files is an absolute path to a file.
    Also assumes that both parameters are non-empty lists
    """
    for index, source_path in enumerate(path_to_files):
        file_name = os.path.basename(source_path)
        print('File name ' + file_name)
        dest = os.path.join(destinations[index], file_name)
        os.rename(source_path, dest)
        print(f'Moved {file_name}...')



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

    move_files(files, new_dirs)


if __name__ == '__main__':
    main()
