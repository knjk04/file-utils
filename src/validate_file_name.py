import re

# Based on https://docs.microsoft.com/en-us/windows/win32/fileio/naming-a-file
def is_valid_windows_file_name(file_name):
    # TODO add other checks
    return not is_reserved_word(file_name)


'''
    < (less than)
    > (greater than)
    : (colon)
    " (double quote)
    / (forward slash)
    \ (backslash)
    | (vertical bar or pipe)
    ? (question mark)
    * (asterisk)
'''
def contains_reserved_char():
    raise NotImplementedError


def is_reserved_word(word: str):
    reserved_words = {
       'CON', 'PRN', 'AUX', 'NUL', 'COM1', 'COM2', 'COM3', 'COM4', 'COM5', 'COM6', 'COM7', 'COM8', 'COM9', 'LPT1',
       'LPT2', 'LPT3', 'LPT4', 'LPT5', 'LPT6', 'LPT7', 'LPT8', 'LPT9'
    }
    return word in reserved_words


def ends_in_space_or_period():
    raise NotImplementedError



