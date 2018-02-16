def printInstructions(instruction):
    print(instruction)

def getUserScore(userName):
    try:
        f = open('userScores.txt', 'r')
        for line in f:
            content = line.split(', ')
            if content[0]==userName:
                f.close()
                return content[1]
        f.close()
        return '-1'
    except IOError:
        print('No score file exists yet. Creating...')
        f = open('userScores.txt', 'w')
        f.close()
        return '-1'

def updateUserScore(newUser, userName, score):
    from os import remove, rename
    if newUser == True:
        f = open('UserScores.txt', 'a')
        f.write(userName + ', ' + score + '\n')
        f.close()
    else:
        temp = open('userScores.tmp', 'w')
        f = open('userScores.txt', 'r')
        for line in f:
            content = line.split(', ')
            if content[0]==userName:
                temp.write(userName + ', ' + score  + '\n')
            else:
                temp.write(line)
        f.close()
        temp.close()
        remove('userScores.txt')
        rename('userScores.tmp', 'userScores.txt')
