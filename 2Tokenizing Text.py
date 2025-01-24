import urllib.request
import re
url = ("https://raw.githubusercontent.com/rasbt/"
       "LLMs-from-scratch/main/ch02/01_main-chapter-code/"
       "the-verdict.txt")
file_path = "the-verdict.txt"
urllib.request.urlretrieve(url, file_path)

class Tokenizer:

       def encoder(self, text):
              # split code into the tokens
              # string to inteeger mapping
              #
              pass

       def decoder(self, ids):
              #reverse mapping to convert ids back to text
              pass




if __name__ == '__main__':
# Tokenizing Text
       with open("the-verdict.txt", "r", encoding="utf-8") as f:
              raw_text = f.read()
# use library re to split the text
result = re.split(r'([,.:;?_!"()\']|--|\s)', raw_text)
print("Total number of character:", len(raw_text))
print(raw_text[:99])
print(result[:99])

#Converting tokens into token IDs
#  Next, let’s convert these tokens from a Python string to an integer representation to
#  produce the token IDs. This conversion is an intermediate step before converting the
#  token IDs into embedding vectors.
#  To map the previously generated tokens into token IDs, we have to build a vocabu
# lary first.

# sort words alphabetically

all_words_sorted = sorted(set(result))
print(all_words_sorted)
vocab = {token: integer for token, integer in enumerate(all_words_sorted)}
print(vocab)


