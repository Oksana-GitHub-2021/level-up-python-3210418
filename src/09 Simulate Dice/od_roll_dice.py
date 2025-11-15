import random 
number_of_trials = 1000000

def roll_dice(*args):
  occurence_numbers = {}
  i = 0
  while i < number_of_trials:
    random_number = 0
    for arg in args:
      random_number += random.randint(1, arg)
    if random_number in occurence_numbers:
      occurence_numbers[random_number] += 1
    else:
      occurence_numbers[random_number] = 1
    i += 1
  occurence_numbers = dict(sorted(occurence_numbers.items()))
  sum_probabilities = 0
  for trial, occures_times in occurence_numbers.items():
    probability = occures_times/number_of_trials*100
    print(f"Trial #{trial}: {round(occures_times/number_of_trials*100, 2)}%")
    sum_probabilities += probability
  print(f"Sum of probabilities: {sum_probabilities}%")
        
roll_dice(4, 6, 6, 20) 
