def ask_text():
    while True:
        name = input("What is your name? ")
        if name == "":
            return("Can't be empty. Try again.")
        else:
            return(name)
            break
    while True:
        sub_name = input("Enter subject name? ")
        if sub_name == "":
            return("Can't be empty. Try again.")
        else:
            return(sub_name)
            break
def ask_marks():
    user_input = input("Enter marks (1-100): ")
    
    if user_input.isdigit():
        marks = int(user_input)
        if 1 <= marks <= 100:
            return(f"Success! You entered: {marks}")
            return marks
        else:
            return("Error: Number must be between 1 and 100.")
    else:
         return("Error: Enter whole numbers only.")
    return ask_marks()
ask_marks()

def ask_y_n():
    while True:
        user_input=input("do you want to add another subject:-")
        if user_input == "y":
            return(True)
            break
        elif user_input == "n":
            return(False)
            break
        else:
            print("type only y/n only")
ask_y_n()
  
