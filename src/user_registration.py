'''
@Author: Sheikh Jainab
@Date: 2022-05-31 16:20:30
@Last Modified by: Sheikh Jainab
@Last Modified time: 2022-05-31 16:20:30
@Title :User Registration
User Registration System needs to ensure all validations 
are in place during the User Entry
'''
import re
import logging
class UserRegistration:

    def __init__(self):
        self.first_name = None
        self.last_name = None
        self.phone_number = None
        self.password = None
        self.logger = logging.getLogger(__name__) #loger instance

    def first_name_input(self,first_name):
        """
            Description: 
                This function is use for the user to input their first name and validates it.
            Parameter:
                self instance of class
            Return:
                None
        """
        if re.match("^[A-Z][a-z].{2,}$", first_name):
            self.first_name = first_name
            self.logger.info("Your first name is: %s", first_name)
            return True
        else:
            self.logger.error("First letter needs to be capital and name should be more than three characters: %s", first_name)
            return False
    def last_name_input(self):
        """
            Description: 
                This function is use for the user to input their last name and validates it.
            Parameter:
                self instance of class
            Return:
                None
        """

        while True:
            last_name = input("Enter your last name : ")
            if re.match("^[A-Z][a-z].{2,}$",last_name):
                self.last_name = last_name
                self.logger.info({last_name})
                self.logger.info("Your first name is : %s",last_name)
                break

            else:
                self.logger.error("First letter needs to be capital and name should be more that three characters %s",last_name)        

    def email_input(self):
        """
        Description: 
            Validates an email address using a regular expression.
        Returns:
            True if the email address is valid, False otherwise.
        """
    # ^[a-zA-Z0-9]+: The email starts with one or more alphanumeric characters.
    # (\.[a-zA-Z0-9]+)*: Optionally followed by a dot and more alphanumeric characters, zero or more times.
    # @: Followed by the @ symbol.
    # [a-zA-Z0-9]+: Followed by one or more alphanumeric characters.
    # (\.[a-zA-Z]{2,}){1,2}$: Followed by a dot and two or more letters, one or two times.

        '''  E.g. abc.xyz@bl.co.in - Email has 3 mandatory parts (abc, bl 
& co) and 2 optional (xyz & in) with 
precise @ and . positions
'''
        pattern = r'^[a-zA-Z0-9]+(\.[a-zA-Z0-9]+)*@[a-zA-Z0-9]+(\.[a-zA-Z]{2,}){1,2}$'


        while True:
            email_id = input("Enter your email id : ")
            if re.match(pattern,email_id):
                self.logger.info("Your Email id is : %s",email_id)
                return True

            else:
                print("eg. example@example.com")
                print("Email should contain dot(.) and(@)ex.com ")
                self.logger.error("Invalid Email id %s " ,email_id)

    def phone_input(self):
        """
         Description: 
                This function is use for the user to input their valid phone number with contry code and 10 digit phone number.
            Parameter:
                self instance of class
            Return:
                If phone number is not valid throws an error
      
        """
        regex_ex = r'^\+\d{1,3} \d{10}$'
    
        while True:
            phone_number = input("Enter your phone number (e.g., 91 9919819801): ")
            if re.match(regex_ex, phone_number):
                self.phone_number = phone_number
                self.logger.info("Your phone number is: %s", phone_number)
                print("Valid phone number.")
                break
            else:
                self.logger.error("Invalid phone number entered: %s", phone_number)
                print("Country code separated by space.")
                print("Please enter a valid phone number with country code and 10 digits.")

    def password_input(self):
        while True:
            password = input("Enter password : ")
            if len(password) < 8:
                self.logger.error("Invalid password ")
                print(" Password needs to be 8 char or more ")
                continue

            if not re.search(r'[A-Z]', password):
                self.logger.error("Needs to have at least one upper case")
                print(" Password needs at least one upper case ")
                continue

            if not re.search(r'\d', password):
                self.logger.error("Needs to have at least one numeric digit")
                print(" Password needs at least one numeric digit  ")
                continue

            special_char = re.findall(r'[^a-zA-Z0-9]', password)
            if len(special_char) != 1:
                self.logger.error("Invalid password: Password must contain exactly one special character")
                print("Password must contain exactly one special character.")
                continue

            self.password = password
            self.logger.info("valid password")
            print("Password is valid")
            break

def main():

    # logger
    logging.basicConfig( filename= 'user.log',level=logging.INFO)
    user_registration = UserRegistration()
    user_registration.first_name_input()
    user_registration.last_name_input()
    user_registration.email_input()
    user_registration.phone_input()
    user_registration.password_input()


if __name__ == "__main__":
    main()
