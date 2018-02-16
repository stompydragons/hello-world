class Game:
    def __init__(self, noOfQuestions = 0):
        self._noOfQuestions = noOfQuestions

    @property
    def noOfQuestions(self):
        return self._noOfQuestions

    @noOfQuestions.setter
    def noOfQuestions(self, value):
        if value < 1:
            self._noOfQuestions = 1
            print('Minimum Number of Questions = 1')
            print('Hence, number of questions will be set to 1')
        elif value > 10:
            self._noOfQuestions = 10
            print('Maximum Number of Questions = 1')
            print('Hence, number of questions will be set to 10')
        else:
            self._noOfQuestions = value

class BinaryGame(Game):
    def generateQuestions(self):
        #import randint
        from random import randint
        #declare local variable called score
        score = 0
        #use for loop to generate questions and evaluation answers
        for i in range(self.noOfQuestions):
            base10 = randint(1, 100)
            prompt = '\nCalculate the binary value of %s: ' %(base10)
            userResult = input(prompt)

            while True:
                try:
                    #cast the user answer to an integer and evaluate the answer
                    #update user score based on the answer
                    #break out from the while true loop using the break statement
                    answer = int(userResult, base = 2)
                    if answer == base10:
                        print('\nCorrect answer!')
                        score += 1
                        break
                    else:
                        print('Wrong answer. The correct answer is {:b}.'.format(base10))
                        break
                    
                except:
                    #print error message if casting fails
                    #prompt user to key in the answer again
                    prompt = '\That was not a binary value. Please try again: '
                    userResult = input(prompt)
        #return the value of score
        return score

class MathGame(Game):
    def generateQuestions(self):
        #import randint
        from random import randint

        #declare four local variables called score, numberList, symbolList, operatorDict
        score = 0
        numberList = [0, 0, 0, 0, 0]
        symbolList = ['', '', '', '']
        operatorDict = {1:' + ', 2:' - ', 3:'*', 4:'**'}
        
        #use for loop to generate questions and evaluate answers
        for i in range(self.noOfQuestions):
            for index in range(0,5):
                numberList[index] = randint(1,9)
            for index in range(0,4):
                if index > 0 and symbolList[index-1] == '**':
                    symbolList[index] = operatorDict[randint(1,3)]
                else:
                    symbolList[index] = operatorDict[randint(1,4)]
            
            questionString = str(numberList[0])
            for index in range(0,4):
                questionString = questionString + symbolList[index] + str(numberList[index + 1])
            
            result = eval(questionString)
            questionString = questionString.replace('**', '^')
            prompt = '\nPlease evalueate %s: ' %(questionString)
            userResult = input(prompt)

            while True:
                try:
                    answer = int(userResult)
                    if answer == result:
                        print('Correct answer!')
                        score += 1
                        break
                    else:
                        print('Wrong answer. The correct answer is {:d}.'.format(result))
                        break

                except:
                    prompt = '\nThat was not a number value. Please try again: '
                    userResult = input(prompt)
        #return the value of the score
        return score
        
