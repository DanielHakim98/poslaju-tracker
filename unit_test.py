from poslaju_tracker import is_still_running_program
from _pytest.monkeypatch import MonkeyPatch


class TestIsStillRunningProgram:
    def test_returns_true_when_user_input_is_y(self, monkeypatch: MonkeyPatch):
        monkeypatch.setattr("builtins.input", lambda _: "Y")
        assert is_still_running_program() is True

    def test_returns_false_when_user_input_is_n(self, monkeypatch: MonkeyPatch):
        monkeypatch.setattr("builtins.input", lambda _: "N")
        assert is_still_running_program() is False

    def test_returns_false_when_user_input_is_invalid(self, monkeypatch: MonkeyPatch):
        monkeypatch.setattr("builtins.input", lambda _: "Invalid")
        assert is_still_running_program() is False
