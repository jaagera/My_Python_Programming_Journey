s ="what is right in your mind is right in your world"
#split - to convet string into list of string 
s1=s.split(" ")
print(s1)
s1=s1[::-1]
print(s1)
#join - to convert the list again into string 
print(" ".join(s1))