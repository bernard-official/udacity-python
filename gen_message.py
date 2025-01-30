# get and process input for a list of names
names = input("Enter names separated by commas: ").title().split("," )
# print(names)


 # get and process input for a list of the number of assignments
assignments =  input("Enter number of assignments: ").split(",")
print(assignments)

# get and process input for a list of grades

grades = input("Enter grades separated by commas: ").split(",")

# grades = [50,80,70]

## message string to be used for each student
## HINT: use .format() with this string in your for loop
message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. You're current grade is {} and can increase \
# to {} if you submit all assignments before the due date.\n\n"

# ## write a for loop that iterates t
for name,assignment,grade in zip(names,assignments,grades):
    # print("{},{},{}".format(name,assignment,grade))
    print(message.format(name,assignment,int(grade)))