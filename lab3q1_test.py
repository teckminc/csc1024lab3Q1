import lab3q1
from io import StringIO
from sys import stderr
def test_case1(monkeypatch, capsys):
    number_inputs = StringIO('')

    monkeypatch.setattr('sys.stdin', number_inputs)
    lab3q1.main()
    captured_stdout, captured_stderr = capsys.readouterr()

    assert captured_stdout.strip().find(f'0 1 2 3 4 5 6 7 8 9') != -1

def test_case2(monkeypatch, capsys):
  with open(f"lab3q1.py") as tf:
    head = [next(tf) for _ in range(10)]
    s = tf.read()
    assert(s.find("while") != -1 )

def test_case3(monkeypatch, capsys):
    number_inputs = StringIO('')

    monkeypatch.setattr('sys.stdin', number_inputs)
    lab3q1.main()
    captured_stdout, captured_stderr = capsys.readouterr()

    assert captured_stdout.strip().find(f'Starting') != -1
    assert captured_stdout.strip().find(f'Done') != -1