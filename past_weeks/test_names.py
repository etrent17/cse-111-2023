from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest

def test_make_full_name():
    assert make_full_name(" John", "Wick") == "Wick; John"
    assert make_full_name(" Eric", "Benge") == "Benge; Eric"
    assert make_full_name(" Adam", "Steiner") == "Steiner; Adam"


def test_extract_family_name():
    assert extract_family_name("Wick; John") == "Wick"
    assert extract_family_name("Benge; Eric") == "Benge"
    assert extract_family_name("Steiner; Adam") == "Steiner"

def test_extract_given_name():
    assert extract_given_name("Brown; Sally") == "Sally"
    assert extract_given_name("Trent; Elijah") == "Elijah"
    assert extract_given_name("Steiner; Adam") == "Adam"

pytest.main(["-v", "--tb=line", "-rN", __file__])
