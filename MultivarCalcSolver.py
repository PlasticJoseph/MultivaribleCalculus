import MultivarCalcDefs as MCD
print("Hello, welcome to the solver.")
print("This program only takes vectors in the 2nd and 3rd dimension. It cannot do derivitives and integerals.")
print("Type in vectors or coordinates in format: [1,2,3]")
print("For multible,type in format: [1,2,3] [4,5,6]")
print("For squareroots, type: a√c")
print("For fractions, type: a/b")
print("For fractions*squareroots, type: a/b√(c/d) or a√(c/d)")

print()
comm = "" ##will be replaced w/ input prob

while comm != "Q":
    MCD.Commands() #print available commands
    comm = input()
    if comm == "1": #prints Dot Product and Cross Product
        print("Dot and Cross product")
        vector = MCD.vectorInput(comm)
        MCD.DotP(vector)

    elif comm == "Q":
        print("Thank you for using this program.")
    else:
        print("Invalid command")
        print("Type a valid number or Q to quit:", end='')


