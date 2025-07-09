name = ('student', 'gender', 'class', 'school', 'address', 'age', 'grade') # variables with so many objects

# pros:
# 1. it reduces the human effort for coding
# 2. easy to write for long dataset
# 3. easy to recall

# Strategies
# 1. only those jo python ke language main nahi hay
# 2. mean jo already python ma exsit karty wo apny nahi likhny -- it called reserved words
# 3. what is reserved words?
#  --False, None, True, and, as, assert, break, class, continue, def, del, elif, else, except, finally, for, from, global, if, import, in, is, lambda, nonlocal, not, or, pass, raise, return, try, while, with, yield.
# 4.don't ever write varaibles name with spaces instead use underscore.
# 5, capitaliza na karian 
# 6. don't use lengthy list of alphabets mean variables. always use short words.like -(student_name)
# 7. Special character sy na use karian like 2 and ?, # this signs
# 8. don't use numbers in beginning like 2 @ etc.
# 9.  meaningfull hona chiye - like student ka data hay tu osi sy related ho 
# 10.  Sabsy important  hay --> Global trends ka khyal rakhian ( df = dataframe like plot , glob etc)
# 11. Don't ever repeat the same variable (pehly wlaa update ho jay ga warna)
# 12. Variable naming convention ' don't use operators in variables. 
# 13. Final rule ---> agr pichy waly ko update krian tu new name say update karian like student tha osko student_name_1 kardian 
# 14. don't use "" for variables in print function
x = 2+3+9-2*12*(2/3)
# we always use small x 
name_2 = ("My name ")  # we use variables like this not use any function name. 

#("apple","banana", "peach", "mango ","pine") # this list needs a variable we don't use like this now we declare it like -->
fruit_basket = ("apple","banana", "peach", "mango ","pine")

print(fruit_basket)
print(name_2)
# print(x)

x=15.7 # now it is float variable but afte rtype_cast it's value will be changed.
print(type(x))
print(x)
 
x= int(x)  # we use it for type_conversion
print(type(x)) # type_cast mean jo data tha oska type change kardia hay 
print(x)