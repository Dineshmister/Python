import re
#your email id should be in the format of chris001@gmail.com
def password():
    user = input("Enter your Email  :  ")
    #the pattern has defined using re.search
    email = re.search('^[a-z0-9]{5,20}\@(gmail.com)$',user)

    if email:
        print("success")
    else:
        #if the entered email id doesn't matches with pattern the function will call recursively until the valid email id is entered
        print("Email id is invalid")
        password()

password()

class passwordchecking:
    
	def length_check(self):
     #user_input variable is created for getting the password from the user
     user_input = str(input("Create your password : "))
     
	 #this pattern checks for the length whether it lies between 5-20
     length = re.compile("[A-Z0-9a-z]{5,20}")
     
	 #search is used to check the pattern is present
     operation = length.search(user_input)
     
	 #period is another condition whether it checks whether the entered password contains any periods
     period = re.search("\.",user_input)
     
	 #if it contains it give the message from print statement and recursively call the function until it get corrected
     if period:
         print("Your password shoudn't contain periods")
         self.length_check()
     
	 #after it checks for the periods it will check for the length that assigned in operation variable
     elif operation:
         print("Password is correct")
     else:
        #if the entered password contains less than 5 digits it will print the statement and the length_check function will be called again
        print("your password should contain atleast 5 digits")
        self.length_check()

#object is created for class
call = passwordchecking()
#method is called through object 'call'
call.length_check()
