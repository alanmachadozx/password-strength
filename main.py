
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

def verification(passoword):
    if (len(passoword) < 8):
        raise Exception('The password is too short')
    
    upperAndLowe(passoword)