import math as m
#
def Split(inputs): #split input into list of lists of lists
    inputs = inputs.split() #splits inputs into 2 elements
    #turning input into a list of 2 lists (vector)
    vector = []
    vector.append(inputs[0].strip('[]').split(',')) #first vector
    if len(inputs) == 2:
        vector.append(inputs[1].strip('[]').split(',')) #second vector
    vector = InputAdj(vector) #Adjust input into acceptable form (ex:√4 -> 1/1√4)
    for i in range(len(vector)): #convert each number in a vector from a√b formatted [a, b]
        for j in range(len(vector[i])):
            if "√" in vector[i][j]:
                vector[i][j] = vector[i][j].split("√")
            else:
                vector[i][j]=[vector[i][j], '1']
            for k in range(len(vector[i][j])): #convert each number in a vector from a/b formatted [a, b]
                if "/" in vector[i][j][k]:
                    vector[i][j][k] = vector[i][j][k].split("/")
                else:
                    vector[i][j][k] = [vector[i][j][k], '1']
                for u in range(len(vector[i][j][k])): #string valed number -> integer
                    vector[i][j][k][u] = int(vector[i][j][k][u].strip('()'))
    return vector

def InputAdj(vector): #Adjust input into acceptable form
    for i in range(len(vector)):
        for j in range(len(vector[i])):
            element = vector[i][j]
            if element[0] == '√': #Adjust input w/o coeiff (ex:√4 -> 1/1√4)
                vector[i][j] = '1/1' + vector[i][j]
    return vector

def Translate(vector): #translate list to string in input format
    vector = Simp(vector) #simplify the values before translating
    for i in range(len(vector)):
        for j in range(len(vector[i])):
            for k in range(len(vector[i][j])):
                vector[i][j][k] = str(vector[i][j][k][0]) + '/' + str(vector[i][j][k][1])
            vector[i][j] = str(vector[i][j][0]) + '√(' + str(vector[i][j][1]) + ")"
            vector[i][j] = vector[i][j].replace("√(1/1)", "")
            vector[i][j] = vector[i][j].replace("/1", "")
    return(vector)

def Simp(vector): #simplifies any sqrt or fractions
    for i in range(len(vector)):
        for j in range(len(vector[i])):
            for k in range(len(vector[i][j])):
                for u in range(len(vector[i][j][k])):
                    #simplifies sqrt component
                    if k == 1: #list containing sqrt component
                        factor = 2
                        while factor**2 <= abs(vector[i][j][k][u]):
                            if int(abs(vector[i][j][k][u])/factor**2) == abs(vector[i][j][k][u])/factor**2: #proceed if sqrt component can be divided by perfect sqrt
                                vector[i][j][k][u] = int(vector[i][j][k][u]/factor**2)
                                vector[i][j][0][u] = int(vector[i][j][0][u]*factor)
                                factor = 1
                            factor = factor + 1
                #simplifies fraction component
            for k in range(len(vector[i][j])):
                factr = 2 #different from factor in sqrt simp to prevent error
                while factr <= abs(vector[i][j][k][0]) and factr <= abs(vector[i][j][k][1]):
                    if int(abs(vector[i][j][k][0]/factr)) == abs(vector[i][j][k][0])/factr and int(abs(vector[i][j][k][1]/factr)) == abs(vector[i][j][k][1]/factr): #proceed if sqrt component can be divided by perfect sqrt
                        vector[i][j][k][1] = int(vector[i][j][k][1]/factr)
                        vector[i][j][k][0] = int(vector[i][j][k][0]/factr)
                        factr = 1
                    factr = factr + 1
    return vector

def SumSimp(L1): #simplifies sums
    L2 = []
    index = 0
    while index < len(L1): #simplify coeiffs with equal sqet
        target = L1[index]
        top = target[0][0]
        bttm= target[0][1]
        checker = False
        L1.pop(index)
        i = 0
        while i < len(L1):
            if target[1] == L1[i][1]:
                top = top*L1[i][0][1] + L1[i][0][0]*bttm
                bttm = bttm*L1[i][0][1]
                checker = True
                L1.pop(i)
            else:
                i=i+1
        if checker ==True: #there are values w/ same sqrt
            L2.append([[top,bttm],target[1]])
        else: #no values with same sqrt
            L2.append(target)
    return Simp([L2]) #dot product answer in list form

def Commands(): #print available commands
    print("Commands: Q=Quit, RE=Return")
    print()
    print("1: Dot Product and Cross Product") #
    print("3: Magnitude") #
    print("4: Distance b/w two points A->B") #
    print("Choose a number from above:", end='')
    return()

def vectorInput(num): #tell user to type input
    if num == '1':
        print("type in two vectors: ", end='')
    vector = input()
    return vector

def DotP(vector):
    vec = Split(vector)
    L1 = vec[0] #recycle into w/ L1[i][j][k]*L2[i][j][k]
    L2 = vec[1] #recycle into simplified DotP values
    for i in range(len(L1)):
        for j in range(len(L1[i])):
            for k in range(len(L1[i][j])):
                L1[i][j][k] = L1[i][j][k]*L2[i][j][k]
    L2= SumSimp(Simp([L1])[0]) #simplify factions and sqrt of DotP values to prevent error in sum simplify
    vector = Translate(Split(vector))
    answerStr=str(vector[0])+'*'+str(vector[1]) +' = '+ str(Translate(L2)[0]).strip("[]").replace("'", "").replace(", ", " + ")
    print(answerStr) #dot product answer
    return(L2)
#
def CrossP(L1,L2):
    if len(L1) == 2:
        print(L1, "X", L2, "=", L1[0]*L2[1]-L1[1]*L2[0])
        return L1[0]*L2[1]-L1[1]*L2[0]
    elif len(L1) == 3:
        vList = [0,0,0] # I+J+K vector
        vList[0]= L1[1]*L2[2]-L1[2]*L2[1]
        vList[1]= -(L1[0]*L2[2]-L1[2]*L2[0])
        vList[2]= L1[0]*L2[1]-L1[1]*L2[0]
        print(L1, "X", L2, "=", vList )
        return vList
    else:
        return print("invalid")

#
def Magnitude(L1):
    sum = 0
    for i in range(len(L1)):
        sum = sum + L1[i]*L1[i]
    print("||" + str(L1) + "|| =" + str(RootSimp(sum)))
    return RootSimp(sum)

#
def Distance2P(L1,L2):
    vector = []
    for i in range(len(L1)):
        vector.append(L1[i]-L2[i])
    print("Vector A->B = B - A " + str(L1) + " - " + str(L2) + " = " + str(vector))
    return vector


x1=("[-9/2√(4/4),2√(4/4),3/3√(10)] [14/7√(5/5),2√(4/4),5√(12)]")
print('splitted: ', Split(x1))
print('translated: ', Translate(Split(x1)))
DotP(x1)
print('----')
x1=("[5/2√(4/3),2√(4/4)] [14/7√(5/5),2√(4/3)]")
print('splitted: ', Split(x1))
print('translated: ', Translate(Split(x1)))
DotP(x1)





