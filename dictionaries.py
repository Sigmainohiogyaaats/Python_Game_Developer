capital = {'Mexico':'Mexico city', 'Bangladesh':'Dhaka', 'Netherlands':['Amsterdam', 'The Hague'], 'Germany':'Berlin', 'Australia':'Canberra ', 'Sweden':'Stockholm'} 
print(capital['Netherlands']) 
#new item 
capital['UK'] = 'London' 
print(capital) 

#difference between list and dictionary 
sample_list =['Mexico city', 'Dhaka' , 'Amsterdam' , 'berlin' , 'Canberra', 'Stockholm'] 
print(sample_list[1]) 

#get list of keys 
print(capital.keys()) 
#get list of values  
print(capital.values())  

#check if key exists in dictionary 
#not in and in 
if 'India' in capital: 
    print(capital['India']) 
else : 
    print('Key does not exist')
#delete item from dict. 
del(capital['Mexico']) 
print(capital) 

# change value 
capital['Netherlands']:['Amsterdam','The Hague'] 
print (capital['Netherlands'][1])