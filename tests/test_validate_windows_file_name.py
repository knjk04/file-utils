import pytest

from src.validate_windows_file_name import is_reserved_word, ends_in_space_or_period, \
    contains_reserved_char


@pytest.mark.parametrize("reserved_word", ['CONA', 'PRNA', 'AUXA', 'NULA', 'COM1A', 'COM2A',
                                           'COM3A', 'COM4A', 'COM5A', 'COM6A', 'COM7A', 'COM8A',
                                           'COM9A', 'LPT1A', 'LPT2A', 'LPT3A', 'LPT4A', 'LPT5A',
                                           'LPT6A', 'LPT7A', 'LPT8A', 'LPT9A'])
def test_is_reserved_word_at_start(reserved_word):
    assert not is_reserved_word(reserved_word)


@pytest.mark.parametrize("reserved_word", ['CON', 'PRN', 'AUX', 'NUL', 'COM1', 'COM2', 'COM3',
                                           'COM4', 'COM5', 'COM6', 'COM7', 'COM8', 'COM9', 'LPT1',
                                           'LPT2', 'LPT3', 'LPT4', 'LPT5', 'LPT6', 'LPT7', 'LPT8',
                                           'LPT9'])
def test_is_reserved_word(reserved_word):
    assert is_reserved_word(reserved_word)


@pytest.mark.parametrize("reserved_word", ['SCON', 'SPRN', 'SAUX', 'SNUL', 'SCOM1', 'SCOM2',
                                           'SCOM3', 'SCOM4', 'SCOM5', 'SCOM6', 'SCOM7', 'SCOM8',
                                           'SCOM9', 'SLPT1', 'SLPT2', 'SLPT3', 'SLPT4', 'SLPT5',
                                           'SLPT6', 'SLPT7', 'SLPT8', 'SLPT9'])
def test_is_reserved_word_at_end(reserved_word):
    assert not is_reserved_word(reserved_word)


@pytest.mark.parametrize('word', ['<', '>', ':', '"', '/', '\\', '|', '?', '*'])
def test_contains_reserved_char(word):
    assert contains_reserved_char(word)


@pytest.mark.parametrize('word', ['<file', '>file', ':file', '"file', '/file', '\\file', '|file',
                                  '?file', '*file'])
def test_contains_reserved_char_when_reserved_char_at_start(word):
    assert contains_reserved_char(word)


@pytest.mark.parametrize('word', ['fil<e', 'fil>e', 'fil:e', 'fil"e', 'fil/e', 'fil\\e', 'fil|e',
                                  'fil?e', 'fil*e'])
def test_contains_reserved_char_when_reserved_char_in_middle(word):
    assert contains_reserved_char(word)


@pytest.mark.parametrize('word', ['file<', 'file>', 'file:', 'file"', 'file/', 'file\\', 'file|',
                                  'file?', 'file*'])
def test_contains_reserved_char_when_reserved_char_at_end(word):
    assert contains_reserved_char(word)


@pytest.mark.parametrize('word', [' file', '.file'])
def test_ends_in_space_or_period_if_at_start(word):
    assert not ends_in_space_or_period(word)


@pytest.mark.parametrize('word', ['Space in middle', 'Period . in middle'])
def test_ends_in_space_or_period_if_in_middle(word):
    assert not ends_in_space_or_period(word)


@pytest.mark.parametrize('word', ['file ', 'file.'])
def test_ends_in_space_or_period(word):
    assert ends_in_space_or_period(word)
