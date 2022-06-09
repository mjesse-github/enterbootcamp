import importlib
import sys
import pytest


def test_print_hello(capsys):
    import 0
    importlib.reload(0)
    captured = capsys.readouterr()
    assert "Hello, World!" in captured.out, "Does the code print \"Hello world!\"? The first letter should be a capital H."