from os import listdir

from src.create_dir import create_numbered_dirs, get_parent_dir


def get_files_in(dir: str):
    """Sorts files alphabetically in the specified folder"""
    return [file for file in listdir(dir)]


def create_new_dirs(parent_dir: str, number_of_dirs: int):
    start = 1
    create_numbered_dirs(parent_dir, start, number_of_dirs)



def main():
    parent_dir = get_parent_dir()
    files = get_files_in(parent_dir)
    print(files)

    create_new_dirs(parent_dir, len(files))



if __name__ == '__main__':
    main()
