from poslaju_tracker import (
    is_still_running_program,
    return_value,
    extract_data_from_response,
    is_valid_tracking_number_format,
)
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


class TestReturnValue:
    def test_return_value_if_key_exists(self):
        test_input_data = {"tracking_data": "Delivery completed"}
        real_return_value = return_value(test_input_data, "tracking_data")
        assert real_return_value == "Delivery completed"

    def test_return_value_if_key_not_exists(self):
        test_input_data = {"tracking_data": "Delivery completed"}
        real_return_value = return_value(test_input_data, "non_existing")
        assert real_return_value == "N/A"

    def test_return_value_if_value_is_empty_str(self):
        test_input_data = {"tracking_data": ""}
        real_return_value = return_value(test_input_data, "tracking_data")
        assert real_return_value == "N/A"


class TestExtractDataFromResponse:
    def test_when_data_is_null(self):
        test_input_data = {"data": None}
        returned_data = extract_data_from_response(test_input_data)
        assert returned_data == {}


class TestValidateTrackingNumberFormat:
    def test_tracking_number_less_than_13(self):
        returned_data = is_valid_tracking_number_format("PL123456789")
        assert returned_data is False

    def test_invalid_initial_tracking_number(self):
        returned_data = is_valid_tracking_number_format("LP1234567890M")
        assert returned_data is False
