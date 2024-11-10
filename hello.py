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





import pgzrun 

HEIGHT = 500 
WIDTH = 500 
from random import randint
def draw(): 
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255) 
    width = WIDTH - 200 
    height = HEIGHT - 400
    for i in range(10):
        rect = Rect((0,0),(width,height)) 
        rect.center = 250,250 
        screen.draw.rect(rect,(r,g,b))  

        width -= 10 
        height += 10

pgzrun.go() 




#count vowels 
#using dictionaries 
def check_vowel(string,vowels):  
    #casefold has been used here to ignore cases
    string = string.casefold() 
    #forms a dictionary with key as vowel 
    #value by default 0 
    count = {}.fromkeys(vowels,0) 
    # to count the vowels 
    for character in string: 
        if character in count: 
            count[character] += 1 
    return count 

# drive c 
vowels = 'aeiou' 
string = input('enter a sentence :') 
print(check_vowel(string,vowels))