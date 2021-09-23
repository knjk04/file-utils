import pytest

from src.validate_file_name import is_not_reserved_word


@pytest.mark.parametrize("reserved_word", [('CON'), ('PRN'), ('AUX'), ('NUL'), ('COM1'), ('COM2'), ('COM3'), ('COM4'),
                                           ('COM5'), ('COM6'), ('COM7'), ('COM8'), ('COM9'), ('LPT1'), ('LPT2'),
                                           ('LPT3'), ('LPT4'), ('LPT5'), ('LPT6'), ('LPT7'), ('LPT8'), ('LPT9')])
def test_is_not_reserved_word(reserved_word):
    assert is_not_reserved_word(reserved_word) is False
