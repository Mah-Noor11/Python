# while and For loop
# while Loop

# x=0 # we define x and its value
# while (x<=5):
#     print(x)
#     x= x+1

# For loop
    
# for x in range(4,10):
#     print(x)

# array = dataset

# days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
# for d in days:
#     print(d)

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
for d in days:
    # if (d=="Fri"):break # loops stops
    if (d=="Fri"):continue # skips d
    print(d)


