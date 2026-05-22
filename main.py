def verification(passoword : str):
    if (len(passoword) < 8):
        raise Exception('The password is too short')
    
    upperAndLowe(passoword)
    hasANumber(passoword)
    especialChar(passoword)
    
def upperAndLowe(text):
    upper = False
    lower = False
    
    for char in text:
        if char.isupper():
            upper = True
        if char.islower():
            lower = True
    
    if not upper:
        raise Exception('At least one uppercase letter is required.')
    if not lower:
        raise Exception('At least one lowercase letter is required.')

def hasANumber(passw):
    number = any(char.isdigit() for char in passw)
    if not number:
        raise Exception('At least one number is required.')

def especialChar(passw):
    
    char = any(char.isalnum() for char in passw)
    if not char:
        raise Exception('At least one special character is required.')
    if ' ' in passw: 
        raise Exception('No spaces allowed')
        