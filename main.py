import functions

def verification(password : str):
    
    if not functions.lenght(password):
        print("The password is too short")
    functions.upperAndLowe(password)
    if not functions.hasANumber(password):
        print("At least one number is required.")
    if not functions.especialChar(password):
        print("At least one special character is required.")
    if not functions.emptyEspace(password):
        print("It's not about allowing empty spaces.")