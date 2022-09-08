def ahmad():
    """
   this function takes no argument but takes input from user such as name
    month of birth
    ..
    """
    name=input("please enter your name: ")
    month=input("please enter your birth month: ")
    day=input("please enter your birthday: ")
    year=input("please enter your birth year: ")

    #thiss line prints name and ahmad
    print("hello",name,",", "your birthday is on",month, day, year)
    
def addition():
    number1=input("please enter a number to be added: ")
    number2=input("please enter another number to be added: ")
    print("your result is" , int(number1)+int(number2))
#ahmad() when you dont add the int then it will be just a statement it will not add them.
addition()