# Simple skeleton file for running tests on our project

from nose.tools import *
from titanic.titanic import header_idx

def test_header_idx() :
    assert_equals(header_idx['sex'],4 )