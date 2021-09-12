import os
import sys
from pathlib import Path


def create_numbered_dirs(parent_dir: str, start: int, end: int):
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


def print_error(error_message: str):
    print(f'Error: {error_message}')


def get_parent_dir():
    print('Enter an absolute path to the parent directory: ', sep='')
    parent_dir = input()
    if not os.path.isdir(parent_dir):
        error = f'not a path to a folder on your system: {parent_dir}'
        print_error(error)
        sys.exit()
    return parent_dir


def get_digit_from_user(prompt: str):
    print(prompt)
    entered = input()
    digit = int(entered) if entered.isdigit() else None
    if digit is None:
        print_error('not a digit: ' + entered)
        sys.exit()
    return digit


def main():
    start = get_digit_from_user('Enter in the starting digit: ')
    end = get_digit_from_user('Enter in the end digit: ')
    if start > end:
        error = f'The starting number should be less than the end. ' \
                f'You passed in {start} for the start and {end} for the end'
        print_error(error)
        sys.exit()

    create_numbered_dirs(get_parent_dir(), start, end)


if __name__ == '__main__':
    main()
