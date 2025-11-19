import random

def generate_number():
  dicerolls = []
  for _ in range(5):
      roll = str(random.randint(1, 6))
      dicerolls.append(roll)
  return ''.join(dicerolls)

def generate_passphrase(number_of_words):
  with open('diceware.wordlist.asc', 'r', encoding='utf-8') as file:
    word_list = file.readlines()[2:7778]
    words_dict = {}
    for line in word_list:
      key, val = line.split('\t')
      words_dict[key] = val.strip()       
  password = []
  for _ in range(number_of_words):
      dicerolls = generate_number()
      #print(dicerolls)
      password.append(words_dict.get(dicerolls))
  return " ".join(password)

print(f'Password 1:', generate_passphrase(6))
print(f'Password 2:', generate_passphrase(4))
print(f'Password 3:', generate_passphrase(16))