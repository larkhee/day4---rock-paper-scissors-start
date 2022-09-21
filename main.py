rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

playerInput = input('Choose Rock, Paper or Scissors!')

if playerInput.lower() == 'rock':
  print(rock)
elif playerInput.lower() == 'paper':
  print(paper)
elif playerInput.lower() == 'scissors':
  print(scissors)

computerInput = ''

randomNumber = random.randint(0,2)

if randomNumber == 0:
  computerInput = 'rock'
  print(f'computer plays {rock}')
elif randomNumber == 1:
  computerInput = 'paper'
  print(f'computer plays {paper}')
elif randomNumber == 2:
  computerInput = 'scissors'
  print(f'computer plays {scissors}')

if playerInput.lower() == computerInput:
  print('You draw.')
elif playerInput.lower() == 'rock' and computerInput == 'scissors':
  print('You win.')
elif playerInput.lower() == 'paper' and computerInput == 'rock':
  print('You win.')
elif playerInput.lower() == 'scissors' and computerInput == 'paper':
  print('You win.')
else:
  print('You lose.')

