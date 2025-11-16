def count_words(path):
  with open(path, "r", encoding="utf-8") as f:
    text = f.read() 
  words = text.split()
  print(f"Total words: {len(words)}")
  unique_words_dict = {}
  for word in words:
    word = word.lower()
    if word in unique_words_dict:
      unique_words_dict[word] += 1
    else:
      unique_words_dict[word] = 1
  
  print(f"Top 20 words:")
  for word, count in sorted(unique_words_dict.items(), key=lambda item: item[1], reverse=True)[:20]:
    print(f"{word}: {count}")

#count_words('input_text.txt')  # Example usage
count_words('shakespeare.txt')  # Example usage
