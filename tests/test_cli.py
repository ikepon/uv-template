"""Tests for example_package.cli module."""

import pytest

from example_package.cli import main


class TestCLIGreetCommand:
    """Tests for the greet CLI command."""

    def test_greet_command_basic(self, capsys: pytest.CaptureFixture[str]) -> None:
        """Test basic greet command."""
        exit_code = main(["greet", "World"])
        captured = capsys.readouterr()
        
        assert exit_code == 0
        assert captured.out.strip() == "Hello, World!"

    def test_greet_command_with_japanese(self, capsys: pytest.CaptureFixture[str]) -> None:
        """Test greet command with Japanese characters."""
        exit_code = main(["greet", "Python"])
        captured = capsys.readouterr()
        
        assert exit_code == 0
        assert captured.out.strip() == "Hello, Python!"

    def test_greet_command_empty_name(self, capsys: pytest.CaptureFixture[str]) -> None:
        """Test greet command with empty name shows error."""
        exit_code = main(["greet", ""])
        captured = capsys.readouterr()
        
        assert exit_code == 1
        assert "Error: Name cannot be empty" in captured.err


class TestCLISumCommand:
    """Tests for the sum CLI command."""

    def test_sum_command_integers(self, capsys: pytest.CaptureFixture[str]) -> None:
        """Test sum command with integers."""
        exit_code = main(["sum", "1", "2", "3"])
        captured = capsys.readouterr()
        
        assert exit_code == 0
        assert captured.out.strip() == "Sum: 6.0"

    def test_sum_command_floats(self, capsys: pytest.CaptureFixture[str]) -> None:
        """Test sum command with floats."""
        exit_code = main(["sum", "1.5", "2.5"])
        captured = capsys.readouterr()
        
        assert exit_code == 0
        assert captured.out.strip() == "Sum: 4.0"

    def test_sum_command_mixed_numbers(self, capsys: pytest.CaptureFixture[str]) -> None:
        """Test sum command with mixed numbers."""
        exit_code = main(["sum", "1", "2.5", "3"])
        captured = capsys.readouterr()
        
        assert exit_code == 0
        assert captured.out.strip() == "Sum: 6.5"

    def test_sum_command_negative_numbers(self, capsys: pytest.CaptureFixture[str]) -> None:
        """Test sum command with negative numbers."""
        exit_code = main(["sum", "-1", "1", "-1", "1"])
        captured = capsys.readouterr()
        
        assert exit_code == 0
        assert captured.out.strip() == "Sum: 0.0"

    def test_sum_command_single_number(self, capsys: pytest.CaptureFixture[str]) -> None:
        """Test sum command with single number."""
        exit_code = main(["sum", "42"])
        captured = capsys.readouterr()
        
        assert exit_code == 0
        assert captured.out.strip() == "Sum: 42.0"

    @pytest.mark.parametrize("numbers,expected", [
        (["1", "2", "3"], "Sum: 6.0"),
        (["10", "-5", "0"], "Sum: 5.0"),
        (["100"], "Sum: 100.0"),
        (["-1", "1"], "Sum: 0.0"),
    ])
    def test_sum_command_parametrized(
        self, 
        capsys: pytest.CaptureFixture[str],
        numbers: list[str], 
        expected: str
    ) -> None:
        """Test sum command with various number combinations."""
        exit_code = main(["sum"] + numbers)
        captured = capsys.readouterr()
        
        assert exit_code == 0
        assert captured.out.strip() == expected


class TestCLIGeneral:
    """Tests for general CLI behavior."""

    def test_no_command_shows_help(self, capsys: pytest.CaptureFixture[str]) -> None:
        """Test that running without command shows help and returns 1."""
        exit_code = main([])
        captured = capsys.readouterr()
        
        assert exit_code == 1
        assert "usage:" in captured.out.lower()
        assert "example-package" in captured.out

    def test_invalid_command_shows_error(self, capsys: pytest.CaptureFixture[str]) -> None:
        """Test that invalid command shows error."""
        exit_code = main(["invalid-command"])
        captured = capsys.readouterr()
        
        assert exit_code != 0
        assert "invalid choice" in captured.err.lower()

    def test_greet_missing_argument(self, capsys: pytest.CaptureFixture[str]) -> None:
        """Test greet command without name argument shows error."""
        exit_code = main(["greet"])
        captured = capsys.readouterr()
        
        assert exit_code != 0
        assert "required" in captured.err.lower()

    def test_sum_missing_arguments(self, capsys: pytest.CaptureFixture[str]) -> None:
        """Test sum command without numbers shows error."""
        exit_code = main(["sum"])
        captured = capsys.readouterr()
        
        assert exit_code != 0
        assert "required" in captured.err.lower()

    def test_sum_invalid_number(self, capsys: pytest.CaptureFixture[str]) -> None:
        """Test sum command with invalid number shows error."""
        exit_code = main(["sum", "not-a-number"])
        captured = capsys.readouterr()
        
        assert exit_code != 0
        assert "invalid" in captured.err.lower()