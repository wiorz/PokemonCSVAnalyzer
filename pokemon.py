#Ko, Ivan
#CS120-1F
#HW2: pokemon

#About the program:
#1. Read the file and santitize the inputs.
#2. Make a list with just the relevant data, i.e. type, strength, hp, etc.
#3. Make a dictionary with type (key) paired with stats (values), i.e. {'Grass' : 35, 20, 10}
#4. Make two dictionaries from the Type dictionary above. 
#One for the inner level with each type paired with one value, i.e. {'grass': 10, 'fire': 45};
#The other for the outer level with each stat paired with the type, i.e. {hp: 'grass', 'fire'}.
#5. Ask for user input, then find and print the maximum value of that stat.
#6. Loop the user input, as long as the query isn't an empty string.


#Relevant global indexing table from spec
name = 1
type1 = 2
strength = 4
hp = 5
attack = 6
defense = 7
specialattack = 8
specialdefense = 9
speed = 10


def read_file(filename):
    try:
        fileIn = open(filename)
    except OSError:
        print("File error, probably wrong name/path.")
        return
    
    listIn = fileIn.readlines()
    
    listOut = []
    
    for i in listIn:
        """Only read in a line that is has no '#'. 
        Ideally it should check for '#' only at the beginning of the line, but this is good enough."""
        if "#" not in i:
            """Strip the null chracters first, then split the elements at ',' , and then append to the new list."""
            listOut.append(i.strip().split(","))
    
    """Convert the relevant strings into int"""
    for i in range(len(listOut)):
        for j in range(strength, speed+1):
            listOut[i][j] = int(listOut[i][j])
            
    #print(listOut)
    fileIn.close()
    return (listOut)
    

def make_dictType(listIn):
    dictType, dictFull = {}, {}
    currentType = ""
    listMain, listTemp = [], []
    count = 1
    
    for i in range(len(listIn)):
        count = 1
        currentType = listIn[i][type1] 
        """Only loop through the list if the type has not been added before."""
        if currentType not in dictType.keys():
            dictType[currentType] = ""                    
            listMain = listIn[i][strength:speed+1]
            #print(currentType, listMain)
            """Loop through the list for every new type.
            Each iteration will add all elements from strength to speed(+1) and make a list of them.
            Each list is then sum with another list of stats from the same type."""
            for j in range(i+1, len(listIn)):
                """If we found the same type, count + 1 and sum each element of two lists together, 
                i.e. [1, 2, 3] + [3, 2, 1] = [5, 5, 5]."""
                if currentType == listIn[j][type1]:
                    count += 1
                    listTemp = listIn[j][strength:speed+1]
                    #print("next", currentType, listTemp)
                    listMain = [listMain[h] + listTemp[h] for h in range(len(listMain))]
                    #print(listMain)
            """Update the listMain elements here by dividing each element by count."""
            listMain = [listMain[k]/count for k in range(len(listMain))]
            #print("avg stats:", listMain)
            
            """Pair the type (key) to the list of stats (value)."""
            dictType[currentType] = listMain
    #print(dictType)
    return (dictType)

def make_dictFull(dictType):
    dictSt, dictHp, dictAt, dictDe, dictSA, dictSD, dictSp = {}, {}, {}, {}, {}, {}, {}
    dictFull = {}
    
    """Make the inner levels of the 2D dict here.
    Pair each key with its corresponding value, 
    i.e. {'a': {1, 2, 3}, 'b': {4, 5, 6}} to {'a': 1, 'b': 4}, or {'a': 2, 'b': 5}"""
    for ke, v in dictType.items():
        #print(ke, v)
        dictSt.update({ke: v[0]})
        dictHp.update({ke: v[1]})
        dictAt.update({ke: v[2]})
        dictDe.update({ke: v[3]})
        dictSA.update({ke: v[4]})
        dictSD.update({ke: v[5]})
        dictSp.update({ke: v[6]})
    
    """Merge all inner dicts to the outer level dict here."""
    dictFull["strength"] = dictSt
    dictFull["hp"] = dictHp
    dictFull["attack"] = dictAt
    dictFull["defense"] = dictDe
    dictFull["specialattack"] = dictSA
    dictFull["specialdefense"] = dictSD
    dictFull["speed"] = dictSp
    #print(dictFull)
    
    return(dictFull)

"""Find the pair(s) of keys and values with the maximum value.
First find the max among the values of the relevant key,
and then make a list so that we can add any pairs of the same max value to the list."""
def find_max(dictIn, keyIn):
    """Get max value here."""
    maxValue = max(dictIn[keyIn].values())
    #print("max value is -", maxValue, "- among values ", dictIn[keyIn].values())
    
    listMax = []
    strTemp = ""
    
    """Add to the list of max pairs here."""
    for k,v in dictIn[keyIn].items():
        #print("v is ", v)
        if v == maxValue:
            """Format according to spec."""
            strTemp = "{}: {}".format(k, v)
            listMax.append(strTemp)
            
    return (listMax)

"""As long as the user input is NOT an empty string, keep asking user for more queries."""
def user_query(dictFull):
    print("Select one of the following: \n" +
          "strength, hp, attack, defense, specialattack, specialdefense, speed\n" +
          "(Enter nothing or 'q' to quit.)\n")
    userIn = "x"
    while (userIn != "") and (userIn != "q"):
        print("hey")
        """Convert all user input to lower case here."""
        userIn = input().lower()
        """Use continue so it will loop back to the beginning."""
        if userIn not in dictFull.keys():
            continue
        else:
            listMax = find_max(dictFull, userIn)
            """The *listX and sep = '' is to get the system to print without the quotes, 
            i.e. instead of printing ['a: 12', 'b: 14'], we have 'a:12, b: 14'. """
            print(*listMax, sep = "")
    
    return

def main():
    listFull = read_file(input("Input filename: ")) #"PokeInfo-small.csv"
    #print(listFull)
    
    dictType = make_dictType(listFull)
    #print(dictType)
    dictFull = make_dictFull(dictType)
    #print(dictFull)
    
    user_query(dictFull)
    
main()