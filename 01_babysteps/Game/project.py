import gameclasses, gametasks

try:
    #declare variables
    mathInstructions = '''
    In this game, you will be given a simple arithmetic questions.
    Each correct answer gives you one mark.
    No mark is deducted for wrong answers.'''
    binaryInstructions = '''
    In this game, you will be given a number in base 10.
    Your task is to convert this number to base 2.
    Each correct answer gives you one mark.
    No mark is deducted for wrong answers.'''

    bg = gameclasses.BinaryGame()
    mg = gameclasses.MathGame()

    userName = input('\nPlease enter your username: ')
    score = int(gametasks.getUserScore(userName))
    if score == -1:
        newUser = True
        score = 0
    else:
        newUser = False

    print('Welcome %s! Your current score is %d.' %(userName, score))
    
    #use a while loop to run the program until the user chooses to exit
    userChoice = 0

    while userChoice != '-1':
        #prompt the user to select Math game or Binary game
        game = input('\nMath Game (1) or Binary Game (2)?')
        while game != '1' and game != '2':
            print('You did you did not enter a valid choice. Please try again.')
            game = input('\nMath Game (1) or Binary Game(2)?')
        
        #prompt user for number of questions per game
        numPrompt = input('\nHow many questions do you want per game (1 to 10)?: ')
        while True:
            try:
                num = int(numPrompt)
                break
            except:
                print('You did not enter a valid number.')
                numPrompt = input('How many questions do you want per game (1 to 10)?')

        #display relevant questions based on user's selection and update user's score
        if game == '1':
            mg.noOfQuestions = num
            gametasks.printInstructions(mathInstructions)
            score = score + mg.generateQuestions()
        else:
            bg.noOfQuestions = num
            gametasks.printInstructions(binaryInstructions)
            score = score + bg.generateQuestions()

        #display updated score to user
        print('Your score is ' + str(score))
        
        #prompt user to enter a choice again and use it to update userChoice
        userChoice = input('If you wish to exit the game, enter -1. Otherwise, press enter to continue: ')

    #update the user's score after he/she exits the program
    gametasks.updateUserScore(newUser, userName, str(score))

except Exception as e:
    #inform users that an error has occurred and the program will exit
    print('An error has occurred. The program will now exit.')
    print('Error: ', e)
