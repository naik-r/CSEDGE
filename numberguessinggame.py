import random

def guess_number(min_num, max_num, num_attempts):
  """
  This function plays a number guessing game with the user.

  Args:
      min_num: The minimum value for the random number (inclusive).
      max_num: The maximum value for the random number (inclusive).
      num_attempts: The allowed number of attempts for the user to guess.

  Returns:
      None
  """

  secret_number = random.randint(min_num, max_num)

  for attempt in range(1, num_attempts + 1):
    try:
      guess = int(input(f"Guess #{attempt} (between {min_num} and {max_num}): "))
    except ValueError:
      print("Invalid input. Please enter an integer.")
      continue

    if guess == secret_number:
      print(f"Congratulations! You guessed the number in {attempt} attempts.")
      return
    elif guess < secret_number:
      print("Too low, try again.")
    else:
      print("Too high, try again.")

  print(f"You ran out of guesses. The number was {secret_number}.")

if __name__ == "__main__":
  min_num = 1
  max_num = 10

  num_attempts = 7

  guess_number(min_num, max_num, num_attempts)
