import pytest


def test_main_maximum_points(monkeypatch, capsys):
    """
    Test case: Correct answers lead to points exceeding 100, which should be capped at 100.
    Input: 12 correct answers, 0 incorrect answers.
    Expected output: 'Endpunktzahl: 100'
    """
    # Mock user inputs
    inputs = iter(['12', '0'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Import and run main()
    from main import main
    main()

    # Capture and check output
    captured = capsys.readouterr()
    assert captured.out.strip() == 'Endpunktzahl: 100'


def test_main_minimum_points(monkeypatch, capsys):
    """
    Test case: Incorrect answers lead to negative points, which should be capped at 0.
    Input: 0 correct answers, 5 incorrect answers.
    Expected output: 'Endpunktzahl: 0'
    """
    # Mock user inputs
    inputs = iter(['0', '5'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Import and run main()
    from main import main
    main()

    # Capture and check output
    captured = capsys.readouterr()
    assert captured.out.strip() == 'Endpunktzahl: 0'


def test_main_regular_case(monkeypatch, capsys):
    """
    Test case: Normal calculation with valid points within bounds.
    Input: 8 correct answers, 4 incorrect answers.
    Expected output: 'Endpunktzahl: 60'
    """
    # Mock user inputs
    inputs = iter(['8', '4'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Import and run main()
    from main import main
    main()

    # Capture and check output
    captured = capsys.readouterr()
    assert captured.out.strip() == 'Endpunktzahl: 60'


def test_main_exact_zero_points(monkeypatch, capsys):
    """
    Test case: Correct and incorrect answers result in exactly 0 points.
    Input: 2 correct answers, 4 incorrect answers.
    Expected output: 'Endpunktzahl: 0'
    """
    # Mock user inputs
    inputs = iter(['2', '4'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Import and run main()
    from main import main
    main()

    # Capture and check output
    captured = capsys.readouterr()
    assert captured.out.strip() == 'Endpunktzahl: 0'


def test_main_mixed_case(monkeypatch, capsys):
    """
    Test case: Correct and incorrect answers result in points within bounds.
    Input: 10 correct answers, 2 incorrect answers.
    Expected output: 'Endpunktzahl: 90'
    """
    # Mock user inputs
    inputs = iter(['10', '2'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Import and run main()
    from main import main
    main()

    # Capture and check output
    captured = capsys.readouterr()
    assert captured.out.strip() == 'Endpunktzahl: 90'
