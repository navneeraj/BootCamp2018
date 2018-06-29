import unit
import pytest
def test_smallest_factor():
    assert unit.smallest_factor(1) == 1, "failed the test for 1"
    assert unit.smallest_factor(7) == 7, "failed the test for primes"
    assert unit.smallest_factor(4) == 2, "failed the test"
    assert unit.smallest_factor(9) == 3, "failed the test"


def test_month_length():
    assert unit.month_length("June") == 30, "failed for 30 days"
    assert unit.month_length("August") == 31, "failed for 31 days"
    assert unit.month_length("February",leap_year=False) == 28, "failed for Feb leap years"
    assert unit.month_length("February",leap_year=True) == 29, "failed for Feb leap years"
    assert unit.month_length("abracadabra",leap_year=True) == None, "failed for others"

def test_operate():
    with pytest.raises(TypeError) as excinfo:
        unit.operate(4, 5,9)
    assert unit.operate(4, 5, '+') == 9
    assert unit.operate(4, 5, '-') == -1
    assert unit.operate(7, 0, '*') == 0
    with pytest.raises(ZeroDivisionError) as excinfo:
        unit.operate(5, 0, '/')
    assert unit.operate(8, 4, '/') == 2
    with pytest.raises(ValueError) as excinfo:
        unit.operate(5, 4, 'n')


@pytest.fixture
def set_up_fractions():
    frac_1_3 = unit.Fraction(1, 3)
    frac_1_2 = unit.Fraction(1, 2)
    frac_n2_3 = unit.Fraction(-2, 3)
    frac_1_1 = unit.Fraction(1,1)
    frac_0_5 = unit.Fraction(0,5)
    return frac_1_3, frac_1_2, frac_n2_3, frac_1_1,frac_0_5

def test_fraction_init(set_up_fractions):
    frac_1_3, frac_1_2, frac_n2_3, frac_1_1, frac_0_5 = set_up_fractions
    assert frac_1_3.numer == 1
    assert frac_1_2.denom == 2
    assert frac_n2_3.numer == -2
    frac = unit.Fraction(30, 42) # 30/42 reduces to 5/7.
    assert frac.numer == 5
    assert frac.denom == 7

    with pytest.raises(ZeroDivisionError) as excinfo:
        unit.Fraction.__init__('Test', 9, 0)
    with pytest.raises(TypeError) as excinfo:
        unit.Fraction.__init__('Test', 9.7, 3)

def test_fraction_str(set_up_fractions):
    frac_1_3, frac_1_2, frac_n2_3, frac_1_1, frac_0_5 = set_up_fractions
    assert str(frac_1_3) == "1/3"
    assert str(frac_1_2) == "1/2"
    assert str(frac_1_1) == "1"


def test_fraction_float(set_up_fractions):
    frac_1_3, frac_1_2, frac_n2_3, frac_1_1, frac_0_5 = set_up_fractions
    assert float(frac_1_3) == 1 / 3
    assert float(frac_1_2) == .5
    assert float(frac_n2_3) == -2 / 3


def test_fraction_eq(set_up_fractions):
    frac_1_3, frac_1_2, frac_n2_3, frac_1_1, frac_0_5 = set_up_fractions
    assert frac_1_2 == unit.Fraction(1, 2)
    assert frac_1_3 == unit.Fraction(2, 6)
    assert frac_n2_3 == unit.Fraction(8, -12)
    assert frac_1_3 == 1/3

def test_fraction_add(set_up_fractions):
    frac_1_3, frac_1_2, frac_n2_3, frac_1_1, frac_0_5 = set_up_fractions
    assert frac_1_2 + frac_n2_3 == unit.Fraction(-1, 6)

def test_fraction_sub(set_up_fractions):
    frac_1_3, frac_1_2, frac_n2_3, frac_1_1, frac_0_5 = set_up_fractions
    assert frac_1_2 - frac_n2_3 == unit.Fraction(7, 6)

def test_fraction_mul(set_up_fractions):
    frac_1_3, frac_1_2, frac_n2_3, frac_1_1, frac_0_5 = set_up_fractions
    assert frac_1_2 * frac_n2_3 == unit.Fraction(-1, 3)

def test_fraction_truediv(set_up_fractions):
    frac_1_3, frac_1_2, frac_n2_3, frac_1_1, frac_0_5 = set_up_fractions
    with pytest.raises(ZeroDivisionError) as excinfo:
        frac_1_1/frac_0_5
    assert frac_1_2 / frac_n2_3 == unit.Fraction(-3, 4)

# Problem 5 and 6
@pytest.fixture
def set_up_hands():
    hand1 = ["1022", "1122", "0100", "2021", "0010", "2201",
             "2111", "0020", "1102", "0210", "2110", "1020"]
    handWrongNumCards = ["0000"]
    handNotUnique = ["0000", "0000", "0000", "0000", "0000", "0000",
                     "0000", "0000", "0000", "0000", "0000", "0000"]
    handWrongDigits = ["00000", "1122", "0100", "2021", "0010", "2201",
                       "2111", "0020", "1102", "0210", "2110", "1020"]
    handWrongChar = ["3022", "1122", "0100", "2021", "0010", "2201",
                     "2111", "0020", "1102", "0210", "2110", "1020"]
    return hand1, handWrongNumCards, handNotUnique, handWrongDigits, handWrongChar

def test_count_sets():
    hand1, handWrongNumCards, handNotUnique, handWrongDigits, handWrongChar = set_up_hands()
    assert unit.count_sets(hand1) == 6
    # Raises ValueError if there are not exactly 12 cards
    with pytest.raises(ValueError) as excinfo:
        unit.count_sets(handWrongNumCards)
    # Raises ValueError if the cards are not all unique
    with pytest.raises(ValueError) as excinfo:
        unit.count_sets(handNotUnique)
    # Raises ValueError if one or more cards does not have exactly 4 digits
    with pytest.raises(ValueError) as excinfo:
        unit.count_sets(handWrongDigits)
    # Raises ValueError if one or more cards has a character other than 0, 1, 2
    with pytest.raises(ValueError) as excinfo:
        unit.count_sets(handWrongChar)

def test_is_set():
    # Different in all aspects
    assert unit.is_set("0000", "1111", "2222") == True
    assert unit.is_set("2011", "1122", "1020") == False
    assert unit.is_set("1020", "1120", "1220") == True
