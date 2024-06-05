def calculate(num1, num2, operator):


  if operator == "+":
    return num1 + num2
  elif operator == "-":
    return num1 - num2
  elif operator == "*":
    return num1 * num2
  elif operator == "/":
    if num2 == 0:
      print("Error: Division by zero")
      return None
    else:
      return num1 / num2
  else:
    print("Invalid operator")
    return None

def main():
  """
  The main loop that keeps prompting the user for calculations until the end button is pressed.
  """

  while True:
    try:
      num1 = float(input("Enter the first number: "))
      num2 = float(input("Enter the second number: "))
      operator = input("Enter the operator (+, -, *, /): ")
      result = calculate(num1, num2, operator)
      if result is not None:
        print(f"{num1} {operator} {num2} = {result}")

      end_choice = input("Press 'q' to quit or any 'y' to continue: ")
      if end_choice.lower() == 'q':
        break
      elif end_choice.lower() == 'y':
        continue
    except ValueError:
      print("Invalid input! Please enter numbers only.")

  print("Thanks for using the calculator!")

if __name__ == "__main__":
  main()
