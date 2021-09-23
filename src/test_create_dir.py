import pytest
from _pytest.monkeypatch import MonkeyPatch

from src.create_dir import get_digit_from_user, get_parent_dir

@pytest.fixture(scope="class")
def set_up_monkeypatch(request):
    request.cls.monkeypatch = MonkeyPatch()

@pytest.mark.usefixtures("set_up_monkeypatch")
class TestCreateDir():
    def test_get_parent_dir_exists_if_parent_dir_does_not_exist(self):
        self.monkeypatch.setattr('builtins.input', lambda: '')
        self.monkeypatch.setattr('os.path.isdir', lambda _: False)

        with pytest.raises(SystemExit):
            get_parent_dir()


    def test_get_digit_from_user_exits_if_not_digit(self):
        self.monkeypatch.setattr('builtins.input', lambda: 'not digit')

        with pytest.raises(SystemExit):
            get_digit_from_user('prompt')
