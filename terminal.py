import random
#TODO: Add support for capitol and lowercase letters.
def divider(y):
    from os.path import dirname, join
    current_dir = dirname(__file__)
    file_path = join(current_dir, 'wordbank.txt')
    with open(file_path,'r') as f:
    
            listl=[]
            for line in f:
                    strip_lines=line.strip()
                    listli=strip_lines.split()
                    m=listl.append(listli)
    z = listl
    x = []
    for element in z:
        if type(element) is list:
         
            for item in element:
                x.append(item)
        else:
            x.append(element)
    only = []
    i = 0
    while i < len(x):
        
        if len(x[i]) == y:
            only.append(x[i])
        i = i + 1
    return only

def terminal():
    diffCheck = 0
    difficulty = 0
    while diffCheck != 1:
        response = input('Please select your difficulty: \nEasy\nMedium\nHard\nVery Hard\n').strip()
        response = response.upper()
        if response=='EASY':
            difficulty = random.randint(5,6)
            diffCheck = 1
        elif response=='MEDIUM':
            difficulty = random.randint(7,8)
            diffCheck = 1
        elif response=='HARD':
            difficulty = random.randint(9,10)
            diffCheck = 1
        elif response=='VERY HARD':
            difficulty = random.randint(11,13)
            diffCheck = 1
        elif response=='L O R G E':
            difficulty = 14
            diffCheck = 1
    #Getting the 15 numbers and the 1 answer from those 15
    list_of_words = divider(difficulty)
    chosenList = []
    i = 0
    while i < 15:
        chosenWord = random.randint(0,len(list_of_words)-1)
        chosenValue = list_of_words[chosenWord]
        chosenList.append(list_of_words[chosenWord])
        list_of_words.remove(list_of_words[chosenWord])
        i = i + 1
    answer = chosenList[random.randint(0,14)]
    
    #Printing the Terminal
    count = 0
    numbah = 0
    printed = 0
    intCheck = 0
    randomStuff = ['!','@','#','$','%','^','&','*','(',')','[',']','{','}','/','<','>','?']
    while printed != 14:
        x = random.randint(1,150)
        if count == 100:
            #print("")
            
            count = 0
            intCheck = 0
        elif x == 12 and intCheck != 1:
            z = random.randint(10,99)
            print(z,end = '')
            numbah = numbah + z
            count = count + 2
            intCheck = 1
        elif x == 11 or x == 10 and intCheck != 2:
            j = 0
            rando = random.randint(1,120)
            print(chosenList[printed], end = '')
            while j < rando:
                print(randomStuff[random.randint(0,len(randomStuff)-1)], end = '')
                j = j + 1
            printed = printed + 1
            count = count + difficulty
            intCheck = 2
        else:
            print(randomStuff[random.randint(0,len(randomStuff)-1)], end = '')
            count = count + 1
            intCheck = 0
    hashTest = 0
    bashTest = 'brecksit'        
    chances = 5   
    while chances != -1:
        if chances == 0:
            print("TERMINAL LOCKED\nPLEASE CONTACT AN ADMINISTRATOR")

            chances = -1
            break
        response1 = input("\n" + str(chances) + " Attempt(s) Left" + '\nENTER PASSWORD NOW\n').strip()
        if response1 == bashTest:
            print(answer)
            print(numbah)
        elif response1 == str(numbah) and hashTest == 1:
            print("HASH ALREADY RECORDED")
        elif response1 == str(numbah) and hashTest != 1:
            print("HASH ACCEPTED, ATTEMPTS RESTORED")
            chances = 5
            hashTest = 1
        elif response1.upper() == answer:
            print("ACCESS GRANTED")
            break
        else:
            print("ERROR: INVALID PASSWORD ")
            print(str(stringComp(response1.upper(),answer)) + "/" + str(difficulty) + " CORRECT")
            chances = chances - 1
    endCheck = 0
    while endCheck != 1:
        response = input('').strip()
        if response=='ans':
            print(answer)
        elif response=='q':
            endCheck = 1
        elif response == 'r':
            terminal()
                 
def stringComp(x,y):
    count = 0
    for a, b in zip(x, y):
        if a == b:
            count = count + 1
    return count
            
if __name__ == '__main__':
  terminal()
