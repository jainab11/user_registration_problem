import re
import logging
class UserRegistration:
    
    def __init__(self):
        self.first_name = None
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
            
def main():
    # logger
    logging.basicConfig( filename= 'user.log',level=logging.INFO)
    user_registration = UserRegistration()
    user_registration.first_name_input()
    
    
if __name__ == "__main__":
    main()