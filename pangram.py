#if string is pangram 
def check_pangram(String): 
    alphabet = 'abcdefghijklmnopqrstuvwxyz' 
    for char in alphabet: 
        if char not in string.lower(): 
            return False 
    return True 

# drive coe 
string = input('enter a sentence : ')  
if(check_pangram(string) == True) : 
    print('yes its a pangram')
else: 
    print('no') 

    