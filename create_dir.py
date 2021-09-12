import os
import sys
from pathlib import Path


def create_numbered_dirs(parent_dir, start, end):
    """
    Creates folders from start to end (both inclusive) at the specified parent directory (absolute path).
    If a directory to add already exists, it skips adding it and moves on to the next directory to add
    """
    for i in range(start, end + 1):
        new_dir = os.path.join(parent_dir, str(i))
        try:
            Path(new_dir).mkdir()
            print(f'Added directory {new_dir} ...')
        except FileExistsError:
            print(f'Cannot add directory {new_dir} as it already exists. Skipping...')


def print_error(error_message):
    usage = 'Usage: python create_dir.py [absolute-path-to-parent-directory] [start-digit] [end-digit]'
    print(f'Error: {error_message}')
    print(usage)


def main():
    parent_dir = sys.argv[1]
    if not os.path.isdir(parent_dir):
        error = f'not a path to a folder on your system: {sys.argv[1]}'
        print_error(error)
        sys.exit()

    start = int(sys.argv[2]) if sys.argv[2].isdigit() else None
    end = int((sys.argv[3])) if sys.argv[3].isdigit() else None
    if start is None or end is None:
        error = 'we expected digits, but you passed in something else'
        print_error(error)
        sys.exit()
    elif start > end:
        error = f'The starting number should be less than the end. ' \
                f'You passed in {start} for the start and {end} for the end'
        print_error(error)
        sys.exit()

    create_numbered_dirs(parent_dir, start, end)


if __name__ == '__main__':
    main()
