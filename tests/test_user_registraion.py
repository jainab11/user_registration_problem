from unittest.mock import patch
import pytest
from src.user_registration import UserRegistration

@pytest.fixture
def user_registration():
    return UserRegistration()
    """ test cases for first name
    """

def test_first_name(user_registration):
     assert user_registration.first_name_input("Jainab") == True
     
def test_first_name_invalid_small(user_registration):
    assert user_registration.first_name_input("jai")== False
    
def test_first_name_small_letter(user_registration):
    assert user_registration.first_name_input("jainab") == False

def test_first_name_number(user_registration):
    assert user_registration.first_name_input("123456") == False

def test_first_name_all_cap(user_registration):
    assert user_registration.first_name_input("JAINAB") == False
    

