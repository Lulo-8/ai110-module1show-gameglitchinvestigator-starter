from logic_utils import check_guess, parse_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result[0] == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result[0] == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result[0] == "Too Low"

def test_parse_guess_decimal_truncates():
    # "45.7" should be accepted and truncated to integer 45
    ok, value, err = parse_guess("45.7")
    assert ok is True
    assert value == 45
    assert err is None

def test_parse_guess_invalid_input_returns_false():
    # Non-numeric input should fail with ok=False
    ok, value, err = parse_guess("abc")
    assert ok is False
    assert value is None
    assert err is not None

def test_parse_guess_negative_number():
    # Negative numbers are valid integers and should be parsed correctly
    ok, value, err = parse_guess("-10")
    assert ok is True
    assert value == -10
    assert err is None