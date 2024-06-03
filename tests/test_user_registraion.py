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
    
def test_first_name_all_num(user_registration):
    assert user_registration.first_name_input("Jainab123") == True
    
    
    """ test cases for last name """
    
def test_valid_last_name(user_registration):
    assert user_registration.last_name_input("Sheikh") == True

def test_invalid_last_name(user_registration):
    assert user_registration.last_name_input("sheikh") ==  False

def test_invalid_last_name_small(user_registration):
    assert user_registration.last_name_input("She") ==  False

def test_invalid_last_name_num(user_registration):
    assert user_registration.last_name_input("sheikh123") ==  False

def test_invalid_last_name_num_only(user_registration):
    assert user_registration.last_name_input("133456") ==  False  

def test_invalid_last_name_CAPITAL(user_registration):
    assert user_registration.last_name_input("SHEIKH") ==  False

    """ test cases of email input """
def test_email_1(user_registration):
    assert user_registration.email_input("abc@gmail.com") == True

def test_email_2(user_registration):
    assert user_registration.email_input("abc-100@gmail.com") == True
    
def test_email_3(user_registration):
    assert user_registration.email_input("abc.100@yahoo.com") == True
    
def test_email_4(user_registration):
    assert user_registration.email_input("abc.100@yahoo.com") == True
   
def test_email_5(user_registration):
    assert user_registration.email_input("abc111@abc.com") == True

def test_email_6(user_registration):
    assert user_registration.email_input("abc-100@gmail.com.net") == True
    
def test_email_7(user_registration):
    assert user_registration.email_input("abc.100@yahoo.com.net.au") == True
    
def test_email_8(user_registration):
    assert user_registration.email_input("abc@1.com") == True
# invalid inputs
def test_email_invalid_1(user_registration):
    assert user_registration.email_input("abcgmail.com") == False

def test_email_invalid_2(user_registration):
    assert user_registration.email_input(".abc-100@gmail.com") == False
    
def test_email_invalid_3(user_registration):
    assert user_registration.email_input("abc.100@yahoo.com.a") == False
    
def test_email_invalid_4(user_registration):
    assert user_registration.email_input("abc.100@.yahoo.com") == False
   
def test_email_invalid_5(user_registration):
    assert user_registration.email_input("abc111@.abc.com,") == False
    
#  abc()*@gmail.com – email’s is only allow character, digit, underscore and dash
def test_email_invalid_6(user_registration):
    assert user_registration.email_input("abc()*@gmail.com") == False

# abc@%*.com – email’s tld is only allow character and digit
def test_email_invalid_7(user_registration):
    assert user_registration.email_input("abc@%*.com") == False
    
# abc..2002@gmail.com – double dots “.” are not allow
def test_email_invalid_8(user_registration):
    assert user_registration.email_input("abc..2002@gmail.com") == False

# 10. abc.@gmail.com – email’s last character can not end with dot “.”
def test_email_invalid_9(user_registration):
    assert user_registration.email_input("abc.@gmail.com") == False
    
# 11. abc@abc@gmail.com – double “@” is not allow
def test_email_invalid_10(user_registration):
    assert user_registration.email_input("abc@abc@gmail.com") == False

# 12. abc@gmail.com.1a -email’s tld which has two characters can not contains digit
def test_email_invalid_11(user_registration):
    assert user_registration.email_input("abc@gmail.com.1a") == False

# 13. abc@gmail.com.aa.au - cannont have multiple email’s tld
def test_email_invalid_12(user_registration):
    assert user_registration.email_input("abc@gmail.com.11.au") == False
    
""" test cases for phone input """
def test_phone_number_valid(user_registration):
    assert user_registration.phone_input("+91 7900047628") == True
    
def test_phone_number_invalid_1(user_registration):
    assert user_registration.phone_input("+91 1234567898") == False

def test_phone_number_invalid_2(user_registration):
    assert user_registration.phone_input("917900047628") == False
    
def test_phone_number_invalid_3(user_registration):
    assert user_registration.phone_input("+917900047628") == False

def test_phone_number_invalid_4(user_registration):
    assert user_registration.phone_input("7900047628") == False
    
def test_phone_number_invalid_5(user_registration):
    assert user_registration.phone_input("+12 7895") == False

""" test cases for password validation """
def test_password_valid(user_registration):
    assert user_registration.password_input("Acskjl11@") == True
    
def test_password_invalid_1(user_registration):
     assert user_registration.password_input("password@123") == False

def test_password_invalid_2(user_registration):
    assert user_registration.password_input("Password@") == False
    
def test_password_invalid_3(user_registration):
    assert user_registration.password_input("password123") == False

def test_password_invalid_4(user_registration):
    assert user_registration.password_input("P@123") == False

def test_password_invalid_5(user_registration):
    assert user_registration.password_input("PASSWORD@123") == False
    
def test_password_invalid_6(user_registration):
    assert user_registration.password_input("@qwerty123AasfshadfhnWBHsrw") == False