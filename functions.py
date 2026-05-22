import re

def lenght(passw):
    if (len(passw) < 8):
        return False
def upperAndLowe(text):
    
    if not re.search("[A-Z]", text):
        return print("At least one uppercase letter is required.")
    if not re.search("[a-z]", text):
        return print("At least one lowercase letter is required.")

def hasANumber(passw):
    if not re.search("[0-9]", passw):
        return False

def especialChar(passw):
    if not re.search(r"[^\w\s]", passw):
        return False

def emptyEspace(passw):
    if ' ' in passw: 
        return False