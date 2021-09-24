import re


# The rules of whether a file name is valid is based on
# https://docs.microsoft.com/en-us/windows/win32/fileio/naming-a-file
def is_valid_windows_file_name(file_name):
    if is_reserved_word(file_name):
        raise Exception(f'You entered {file_name}, but you cannot use any of these reserved '
                        f'words:  {get_reserved_words()}')
    elif contains_reserved_char(file_name):
        raise Exception(f'You entered {file_name}, but you cannot use any of these characters: '
                        f'{get_reserved_char_list()}')
    elif ends_in_space_or_period(file_name):
        raise Exception(f'You entered {file_name}, but you cannot have a period or space at the end.')

    return True


def get_reserved_char_list():
    return ['<', '>', ':', '"', '/', '\\ (single backslash)', '|', '?', '*']


def contains_reserved_char(word: str):
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
    return re.match(r'\S*(<+|>+|:+|"+|/+|\\+|\|+|\?+|\*+)', word) is not None


def get_reserved_words():
    return {
        'CON', 'PRN', 'AUX', 'NUL', 'COM1', 'COM2', 'COM3', 'COM4', 'COM5',
        'COM6', 'COM7', 'COM8', 'COM9', 'LPT1', 'LPT2', 'LPT3', 'LPT4', 'LPT5',
        'LPT6', 'LPT7', 'LPT8', 'LPT9'
    }


def is_reserved_word(word: str):
    return word in get_reserved_words()


def ends_in_space_or_period(word: str):
    return word.endswith(' ') or word.endswith('.')
