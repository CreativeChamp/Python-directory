#this program is meant to be a directory.
#the idea is that it may help one to organise and systematically display information
#like say, phone no., address, etc.
# I hope to build it more complex than this, but i can't seem to enter the info in.

# REMOVED YOUR INLINE COMMENTS FOR CLARITY

"""
eg op = {'KG': {'N': 'KG', 'C':'1234'},'AS': {'N': 'AS', 'C':'4321'}} instead of {'AS': {'N': 'AS'}}
"""
dict1 = {}   #* 1. dict1 has to be outside the scope as everytime the for-loop runs, a new & empty dict1 gets created

m = int (input ("Please enter no. of people: "))
for i in range (m):
    #* 2. declaring dict1 here is causing dict1 to get created eveytime for loop runs
    temp = {}  #* 3. This temporary dict will help in adding multiple values to dict1, it is the internal dict

    var1 = str (input ("Enter name of the person: "))
    print()
    n = int (input ("Please enter no. of categories"))


    for i in range(n):
        var2 = str(input("Enter name of category: "))
        print()
        choice = input("What is the type of value that you want to enter, integer, float, string?")
        print()
        choice = choice.lower().strip()   #* 4. We can do this in a single line like this

        if choice == "1" or choice == "int" or choice == "integer"  or choice == "i":  #* 5. Changed this last choice from 's' to 'i'
            var3 = int(input("Enter value: "))
            #dict1.update({var1:{var2:var3}})     #* 6. This command is 'updating' to the same key and hence it will never have more than one {var2:var3} pair against key 'var1'
            temp[var2] = var3                     #* 7. Creating the internal Dictionary first, i.e, {'N':'KG'},{var2:var3} pairs

        elif choice == "2" or choice == "float" or choice == "f" or choice == "decimal":
            var3 = float(input("Enter value: "))
            temp[var2] = var3

        elif choice == "3" or choice == "string" or choice == "str" or choice == "s":
            var3 = input("Enter value: ")
            temp[var2] = var3

        dict1[var1] = temp    #* 8. Updating the dictionary as a whole

        print()
        print(dict1)   #* 9. printing it only once as this is what happens anyway if u put in if-else
        print()

print("Would you like to know information of a scpecific person, or of a specific category?")
print("Type in yes or no as per your wish. ")
choice2 = input()
choice2 = choice2.lower().strip()
if choice2 == "yes" or choice2 == "y":
    print("To know information about a specific person type in 'p' or")
    print("To know information about a specific category type in 'c'.")
    choice3 = input()
    choice3 = choice3.lower().strip()
    if choice3 == "p":
        print

#* P.S. that if you remove the '#' you can see that it is being updated to dict1
#       but for some reason it is being changed everytime it loops
#       Something similar happened when i used lists
#       Is there a different way to approach this problem?
#       Thank you for the help!
