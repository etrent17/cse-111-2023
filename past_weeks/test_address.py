from address import *
import pytest

def test_extract_city():
    ...
    assert extract_city("6213 N Cloverdale Rd, Boise, ID 83713") == "Boise"
    assert extract_city("6213 N Cloverdale Rd, Boise, ID 83713") == "Boise"



pytest.main(["-v", "--tb=line", "-rN", __file__])
