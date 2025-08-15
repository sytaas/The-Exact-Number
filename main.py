import random
print('WELCOME TO THE GAME -"THE EXACT GUESS"...')

n = random.randint(1,100)
inp = -1
guess = 1
while(n!=inp):
    
    inp = int(input(f'[Attempt {guess}]: Guess a number : '))
    if(inp>n):
        guess += 1
        print('Lower number please\n')
    elif(n>inp):
        guess += 1
        print('Higher number please\n')    
    else:
        break

if guess <= 5:
    print("🏆 Genius! That was fast!")
elif 6 <= guess <= 10:
    print("👏 Well done! You got it in a decent number of tries.")
else:
    print("😅 You got there in the end! Keep practicing!")

print(f'You guessed the correct number in {guess} attempts\n')