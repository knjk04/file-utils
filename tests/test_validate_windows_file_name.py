import pytest

from src.validate_windows_file_name import is_not_reserved_word, not_ends_in_space_or_period, \
    not_contains_reserved_char

@pytest.mark.parametrize("reserved_word", ['CON', 'PRN', 'AUX', 'NUL', 'COM1', 'COM2', 'COM3',
                                           'COM4', 'COM5', 'COM6', 'COM7', 'COM8', 'COM9', 'LPT1',
                                           'LPT2', 'LPT3', 'LPT4', 'LPT5', 'LPT6', 'LPT7', 'LPT8',
                                           'LPT9'])
def test_is_not_reserved_word(reserved_word):
    assert is_not_reserved_word(reserved_word) is False


@pytest.mark.parametrize("reserved_word", ['SCON', 'SPRN', 'SAUX', 'SNUL', 'SCOM1', 'SCOM2',
                                           'SCOM3', 'SCOM4', 'SCOM5', 'SCOM6', 'SCOM7', 'SCOM8',
                                           'SCOM9', 'SLPT1', 'SLPT2', 'SLPT3', 'SLPT4', 'SLPT5',
                                           'SLPT6', 'SLPT7', 'SLPT8', 'SLPT9'])
def test_is_not_reserved_word_at_end(reserved_word):
    assert is_not_reserved_word(reserved_word)


@pytest.mark.parametrize('word', ['<', '>', ':', '"', '/', '\\', '|', '?', '*'])
def test_not_contains_reserved_char(word):
    assert not_contains_reserved_char(word) is False


@pytest.mark.parametrize('word', ['<file', '>file', ':file', '"file', '/file', '\\file', '|file',
                                  '?file', '*file'])
def test_not_contains_reserved_char_when_reserved_char_at_start(word):
    assert not_contains_reserved_char(word) is False


@pytest.mark.parametrize('word', ['fil<e', 'fil>e', 'fil:e', 'fil"e', 'fil/e', 'fil\\e', 'fil|e',
                                  'fil?e', 'fil*e'])
def test_not_contains_reserved_char_when_reserved_char_in_middle(word):
    assert not_contains_reserved_char(word) is False


@pytest.mark.parametrize('word', ['file<', 'file>', 'file:', 'file"', 'file/', 'file\\', 'file|',
                                  'file?', 'file*'])
def test_not_contains_reserved_char_when_reserved_char_at_end(word):
    assert not_contains_reserved_char(word) is False


@pytest.mark.parametrize('word', [' file', '.file'])
def test_not_ends_in_space_or_period_returns_true_if_at_start(word):
    assert not_ends_in_space_or_period(word)


@pytest.mark.parametrize('word', ['Space in middle', 'Period . in middle'])
def test_not_ends_in_space_or_period_returns_true_if_in_middle(word):
    assert not_ends_in_space_or_period(word)


@pytest.mark.parametrize('word', ['file ', 'file.'])
def test_not_ends_in_space_or_period_returns_false(word):
    assert not_ends_in_space_or_period(word) is False
