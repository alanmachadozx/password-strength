
import functions
import subprocess
import os

def verification():

    valid = False
    while not valid:
        print("Enter your password:")
        password = input()
        
        if not functions.lenght(password):
            print("The password is too short")
            continue
        if not functions.upperAndLowe(password):
            continue   
        if not functions.hasANumber(password):
            print("At least one number is required.")
            continue
        if not functions.especialChar(password):
            print("At least one special character is required.")
            continue
        if not functions.emptyEspace(password):
            print("It's not about allowing empty spaces.")
            continue
        
        passToCpp(password)    
        valid = True
        
    
def passToCpp(valid_pass):
    
    print('Enter the desired action: \n 1- To encrypt \n 2- to decrypt')
    
    action = input()
    flag = "Error"
    if(action == "1"):
        flag = "--encrypt"
    if(action == "2"):
        flag = "--decrypt"

    print('Enter a file:')
    file = input()
    executable_path = os.path.join('..', 'file-encryptor', 'build', 'cripto')
    
    process = subprocess.Popen(
        [executable_path, flag, file],
        stdin = subprocess.PIPE,
        stdout = subprocess.PIPE,
        text = True
    )

    stdout, stderr = process.communicate(input = valid_pass)
    print(stdout)