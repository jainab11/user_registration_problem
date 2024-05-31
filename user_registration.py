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
        self.logger = logging.getLogger(__name__) #loger instance
        
    def first_name_input(self):
        """
            Description: 
                This function is use for the user to input their first name and validates it.
            Parameter:
                self instance of class
            Return:
                None
        """
        
        while True:
            first_name = input("Enter your first name : ")
            if re.match("^[A-Z][a-z].{2,}$",first_name):
                self.first_name = first_name
                self.logger.info({first_name})
                self.logger.info("Your first name is : %s",first_name)
                break
                
            else:
                self.logger.error("First letter needs to be capital and name should be more that three characters %s",first_name)
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
            

            

def main():
    # logger
    logging.basicConfig( filename= 'user.log',level=logging.INFO)
    user_registration = UserRegistration()
    user_registration.first_name_input()
    user_registration.last_name_input()
    user_registration.email_input()
    
    
if __name__ == "__main__":
    main()