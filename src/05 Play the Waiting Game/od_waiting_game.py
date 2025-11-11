import time
import random

def waiting_game():
  waiting_time = random.randint(2, 4)
  print(f"Your target time is {waiting_time} seconds.")

  text = input(" ---Press Enter to start--- ")  # or raw_input in python2
  while True:
    if text == "":
      start_time = time.time()
      break

  text = input(f"...Press Enter again after {waiting_time} seconds...")
  while True:
    if text == "":
      end_time = time.time()
      break
  duration = end_time - start_time
  print(f"Elapced tiem: {duration} seconds.")

  if duration == waiting_time:
    print("Perfect timing!")
  elif duration > waiting_time:
    print(f"Too late! You were {duration - waiting_time} seconds over.")
  else:
    print(f"Too soon! You were {waiting_time - duration} seconds early.")

print("Let's play the waiting game!")
waiting_game()  
