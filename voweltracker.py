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