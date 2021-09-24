import re

# The rules of whether a file name is valid is based on
# https://docs.microsoft.com/en-us/windows/win32/fileio/naming-a-file
def is_valid_windows_file_name(file_name):
    return is_not_reserved_word(file_name) \
           and not_contains_reserved_char(file_name) \
           and not_ends_in_space_or_period(file_name)


def not_contains_reserved_char(word: str):
    """
        The following reserved chars are not permitted at all:
        < (less than)
        > (greater than)
        : (colon)
        " (double quote)
        / (forward slash)
        \\ (single backslash (escaped here))
        | (vertical bar or pipe)
        ? (question mark)
        * (asterisk)
    """
    # single backslash, vertical bar, question mark and asterisk are escaped
    return re.match(r'\S*(<+|>+|:+|"+|/+|\\+|\|+|\?+|\*+)', word) is None


def is_not_reserved_word(word: str):
    reserved_words = {
       'CON', 'PRN', 'AUX', 'NUL', 'COM1', 'COM2', 'COM3', 'COM4', 'COM5',
       'COM6', 'COM7', 'COM8', 'COM9', 'LPT1', 'LPT2', 'LPT3', 'LPT4', 'LPT5',
       'LPT6', 'LPT7', 'LPT8', 'LPT9'
    }
    return word not in reserved_words


def not_ends_in_space_or_period(word: str):
    return not (word.endswith(' ') or word.endswith('.'))
