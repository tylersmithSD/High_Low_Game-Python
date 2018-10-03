#Developer: Tyler Smith
#Date:      10.13.16
#Purpose:   The program is intended for the computer to guess
#           a number in the range. The range is adjusted according to
#           how the user responds to the computer's guesses.


#Initialization of variables
guessNumber = True         # Condition variable for loop
guessCount  = 0            # Keep track of amount of times user guessed
highBound   = 99           # Higher bound for random number generator
lowBound    = 2            # Lower bound for random number generator

#Random library to generate random number
import random

#Begin: Title of program
print ("-------------------------------------------")
print ("-                                         -")
print ("-           High-Low Master 9001          -")
print ("-                                         -")
print ("-------------------------------------------")
#End:   Title of program

#Ask the user to guess the correct number until they get it correct
while(guessNumber == True):
    
  guessCount = (guessCount + 1)
  if(guessCount == 1):
    print("\nThink of a number between 1 and 100.")         # Prompt the user asking them for a
    print("I'll Guess a number, and you tell me if I'm ")   # number between 1 & 100
    print("too (h)igh, (l)ow or (c)orrect.")
    compNum = random.randint(lowBound, highBound)           # Generate a random guess

  if(highBound == lowBound):
   print('I know for a fact, the answer is %d' %highBound) # User's responses doesn't make sense and low bound is
   userResponse = 'C'                                      # equal to high bound
    
  else:
   print('My guess is %d' %compNum)                          # Print the random guess for user to respond to  
   userResponse = input('Am I too (h)igh, (l)ow or (c)orrect. ')# Ask user to respond to our guess
   userResponse = userResponse[0].upper()                    # Change the response to uppercase for the if statement

  if(userResponse == 'H'):                                  # Check if the guess is too high
    highBound = (compNum - 1)                               # Technically with the way the range works we have to
                                                            # subtract one for the proper range on the upper bound
    compNum = random.randint(lowBound, highBound)           # Generate a random guess
    
  elif(userResponse == 'L'):                                # Check if the guess is too low
    lowBound = (compNum + 1)                                # Technically with the way the range works we have to
                                                            # add one for the proper range on the lower bound
    compNum = random.randint(lowBound, highBound)           # Generate a random guess

  else:                                            
    print('It took me %d tries' %guessCount)                # Computer has gotten guess correct
    playAgain = input('Would you like to play again? ')     # Ask the user if they want to play again 
    playAgain = playAgain[0].upper()                        # Convert first letter to uppercase for if statement

    if(playAgain == 'N'):                                   # User doesn't want to play again
     guessNumber = False                                    # Change condition variable to leave loop
     
    else:                                                   # User wants to keep playing
     guessCount  = 0                                        # Stay in loop, but reset guess count
     lowBound    = 2
     highBound   = 99

else:
  quit() #The user doesn't to play anymore, end program

