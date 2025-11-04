def is_palindrome(str):
  clear_str = ''.join(e for e in str if e.isalnum())
  clear_str = clear_str.lower()
  print("clear_str:", clear_str)
  len_str = len(clear_str)
  for i in range (len_str // 2):
    if clear_str[i] != clear_str[len_str - i - 1]:
      return False
  return True

print("madam:", is_palindrome("madam"))  # True
print("level:", is_palindrome("level"))  # True
print("hello world:", is_palindrome("hello world"))  # False
print("Go hang a salami, I’m a lasagna hog.:", is_palindrome("Go hang a salami, I’m a lasagna hog."))  # False