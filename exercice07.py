def get_letter_count(word: str):
       result = 0

       for letter in word:
              if letter.isalpha():
                     result += 1

       return result

def run():
   assert get_letter_count("Oui") == 3
   assert get_letter_count("Bonjour") == 7
   assert get_letter_count("") == 0
   assert get_letter_count(".........hein???") == 4
   assert get_letter_count("Attention y'a quatre mots !") == 21
