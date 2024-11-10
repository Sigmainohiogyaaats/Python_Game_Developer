my_tuple = (1,2,3,'hola',(5,89,3)) 
#tuple can hold multiple types of data
print(my_tuple[3]) 
packed_tuple = 1, 2, 'two' 
a, b, c = packed_tuple 

for i in my_tuple: 
    print(i) 
stuDetails = ('Arinjay',89) 

#packing 
address = ('227', 'Brickfield shelters', 'Bangalore', 'Karnataka', '562107') 

for x in address: 
    print(x,end = ' ') 

#unpacking 
houseno, apartname , city, state, pin = address 

print() 
print('HNO', houseno) 
print('APT NO',apartname) 
print(city) 
print(state) 
print(pin) 

#a tuple can be created without using parenthesis 
my_tuple = 3, 4.6, 'dog' 
print(my_tuple) 

#nested tuple  
n_tuple =('mouse', 1 )
print(n_tuple[0][1]) 

#elements beginning to 2nd 
#output: (p r ) 
print (my_tuple[:-7])  

#elements 8th 2 end 
print (my_tuple[:]) 

my_tuple = (4, 2 , 3 , [6,5]) 
# however item of mutable element can be changed  
my_tuple [3][0] = 9 
print(my_tuple) 
#tuples can be reassigned 

