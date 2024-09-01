import random
print("welcome to rock,paper,scissors game:")
confirm=input("press enter to continue or type (help) for the rules").lower()
if confirm=="help":
  print("""
  ********rules********
  1)you choose and the computer chooses
  2)rock smaches scissors->rock wins
  3)scissors cut paper->scissors win
  4)paper covers rock->paper wins
  """)
user_choice=input("enter your choice (rock,paper,scissors) :").lower()
rock_ascii="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

"""
paper_ascii="""
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

"""
scissors_ascii="""
  _______
---'   ____)____
        ______)
     __________)
    (____)
---.__(___)
"""
if user_choice not in["rock","paper","scissors"]:
  print("invalid choice")
else:
  if user_choice =="rock" :
    print(f"you choose{rock_ascii}")
  elif user_choice =="paper":
    print(f"you choose {paper_ascii}")
  else:
    print(f"you choose{scissors_ascii}")
computer_choice=random.choice(["rocks","paper","scissors"])
if computer_choice =="rock" :
  print(f"computer choose{rock_ascii}")
elif computer_choice =="paper":
  print(f"computer choose{paper_ascii}")
else:
  print(f"computer choose{scissors_ascii}")
if user_choice==computer_choice:
  print("its a tie")
elif (
  (user_choice == "rock" and computer_choice == "scissors")
   or
  (user_choice =="paper" and computer_choice =="rock" )
  or
  (user_choice == "scissors" and computer_choice == "paper")
    ):
  print(f"you choose {user_choice} and the computer choose {computer_choice}.you win")
else:
   print(f"you choose {user_choice} and the computer choose {computer_choice}.you lose")
