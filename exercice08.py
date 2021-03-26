def get_word_count(sentence: str):
       result = 0

       word_list = sentence.split(" ")

       for word in word_list:
              if word.isalpha():
                     result += 1

       return result


def run():
   assert get_word_count("Bonjour") == 1
   assert get_word_count("Bonjour toi") == 2
   assert get_word_count("Bonjour ca va ?") == 3
   assert get_word_count("Bonjour ca va toi ?!") == 4
   assert get_word_count("") == 0
