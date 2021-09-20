#custom exception is imported from the file called Exception
from Exception import Specialcharacter,Lengtherror
from datetime import datetime as d
d = d.now()
#method is created
def agechecking():

    #enter is used to enter the Date of birth of user
    enter = (input("Enter your dob: "))

    #check_length is used to check the length of entered date of birth
    check_length = len(enter)

    #custom exception is used to check the if the length exceeds more or less 10
    try:
      if check_length != 10:

       #raise will give the error message to the user
       raise Lengtherror("Your DOB must be in the format of dd-mm-yyyy")

      #user should use the hypens(-) before date and month
      if "-" not in enter:
        #If user doesn't use the hyphen this will give the error message
        raise Specialcharacter("You should use hypens")
    except Specialcharacter as error:
      print(error)
    except Lengtherror as error1:
        print(error1)
    else:
      """if there is no error while entering the date of birth the else block will execute
      in present variable only present year is used """
      present = d.strftime("%Y")

      """here slicing is used to ignore the digits before the year
       eg:01-02-2002 this slice will ignore the 6 digits before 2002"""
      year = enter[6:]

      #calculate ius used to find the difference and the string type of year is converted into int
      calculate = int(present) - int(year)

      #it will print the user's age
      print("Your age is : " , abs(calculate),"years")


#method is called
agechecking()
