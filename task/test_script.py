import pytest
from pathlib import Path
import audit_log as m


def test_parse_attempt_line_valid():
    assert m.parse_attempt_line("user-100,true", 1) == ("user-100", True)


def test_parse_attempt_line_invalid():
    with pytest.raises(ValueError):
        m.parse_attempt_line("user-100,maybe", 1)


def test_default_attempts():
    result = m.default_attempts()
    assert isinstance(result, list)
    assert ("user-100", True) in result


def test_load_attempts_none_returns_defaults():
    assert m.load_attempts(None) == m.default_attempts()


def test_load_attempts_reads_valid_file(tmp_path):
    file_path = tmp_path / "input.txt"
    file_path.write_text(
        "# comment\nuser-100,true\n\nuser-200,false\n",
        encoding="utf-8"
    )

    result = m.load_attempts(file_path)

    assert result == [("user-100", True), ("user-200", False)]


def test_load_attempts_invalid_file_raises_value_error(tmp_path):
    file_path = tmp_path / "input.txt"
    file_path.write_text("user-100,maybe\n", encoding="utf-8")

    with pytest.raises(ValueError):
        m.load_attempts(file_path)


def test_format_timestamp_utc_z_ends_with_z():
    result = m.format_timestamp_utc_z()
    assert isinstance(result, str)
    assert result.endswith("Z")


def test_build_event_line_contains_expected_fields():
    line = m.build_event_line("user-100", True, True)

    assert "event_id=" in line
    assert "time=" in line
    assert "system=auth_service" in line
    assert "user_id=user-100" in line
    assert "user_status=known" in line
    assert "outcome=success" in line


def test_write_lines_append_only_writes_file(tmp_path):
    output_path = tmp_path / "logs" / "audit.log"

    m.write_lines_append_only(output_path, ["a", "b"])

    assert output_path.exists()
    assert output_path.read_text(encoding="utf-8") == "a\nb\n"


def test_write_lines_append_only_appends(tmp_path):
    output_path = tmp_path / "logs" / "audit.log"

    m.write_lines_append_only(output_path, ["a"])
    m.write_lines_append_only(output_path, ["b"])

    assert output_path.read_text(encoding="utf-8") == "a\nb\n"


def test_main_success(tmp_path):
    input_path = tmp_path / "input.txt"
    output_path = tmp_path / "audit.log"

    input_path.write_text("user-100,true\n", encoding="utf-8")

    result = m.main(["--input", str(input_path), "--output", str(output_path)])

    assert result == 0
    assert output_path.exists()


def test_main_invalid_input_returns_2(tmp_path):
    input_path = tmp_path / "input.txt"
    output_path = tmp_path / "audit.log"

    input_path.write_text("user-100,maybe\n", encoding="utf-8")

    result = m.main(["--input", str(input_path), "--output", str(output_path)])

    assert result == 2