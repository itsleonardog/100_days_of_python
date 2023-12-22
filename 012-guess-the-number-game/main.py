from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

turns = 0


# function to check user's guess against actual answer
def check_answer(guess, answer, turns):
  """
  checks answer against guess. 
  returns number of turns remaining
  """
  if guess > answer:
    print("Too high.")
    return turns - 1
  elif guess < answer:
    print("Too low.")
    return turns - 1
  else:
    print(f"You got it! The answer was {answer}")


# make function to set difficulty
def set_difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  return EASY_LEVEL_TURNS if level == "easy" else HARD_LEVEL_TURNS


def game():
  # choosing a random number between 1 and 100
  print("Welcome to the Guessing Game!")
  print("I'm thinking of a number between 1 and 100...")
  answer = randint(1, 100)

  turns = set_difficulty()

  guess = 0
  while guess != answer:
    # let the user guess a number
    guess = int(input("Make a guess: "))
    print(f"You have {turns} attempts remaining to guess the number.")
    turns = check_answer(guess, answer, turns)
    if turns == 0:
      print("You've run out of guesses. You lose.")
      return
    elif guess != answer:
      print("Guess again.")

  # track the number of turns and reduce by 1 if they get it wrong


game()
