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
            print(f"Success! You entered: {marks}")
            return marks
        else:
            print("Error: Number must be between 1 and 100.")
    else:
         print("Error: Enter whole numbers only.")
    return ask_marks()
ask_marks()
  
