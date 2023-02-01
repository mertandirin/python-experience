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

import random

cc = random.randint(0,2)
print("What do you choose? 0 for rock, 1 for paper or 2 for scissors \n")
yc = int(input())

if cc == 0:
  cci = rock
elif cc == 1:
  cci = paper
elif cc == 2:
  cci = scissors

if yc == 0:
  yci = rock
elif yc == 1:
  yci = paper
elif yc == 2:
  yci = scissors  

if (yc == 0 and cc == 1) or (yc == 1 and cc == 2) or (yc == 2 and cc == 0):
  print("\nYour choice:\n" + yci + "\nComputer's choice\n" + cci + "\nYou lose\n")

elif (cc == 0 and yc == 1) or (cc == 1 and yc == 2) or (cc == 2 and yc == 0):
  print("\nYour choice:\n" + yci + "\nComputer's choice\n" + cci + "\nYou won\n")

else:
  print("try again")

  



