import urllib.request
import re

url = ("https://raw.githubusercontent.com/rasbt/"
       "LLMs-from-scratch/main/ch02/01_main-chapter-code/"
       "the-verdict.txt")
file_path = "the-verdict.txt"
urllib.request.urlretrieve(url, file_path)


def split(text):
    return re.split(r'([,.:;?_!"()\']|--|\s)', text)


class Tokenizer:
    def __init__(self):
        with open("the-verdict.txt", "r", encoding="utf-8") as f:
            raw_text = f.read()
        result = split(raw_text)
        all_words_sorted = sorted(set(result))
        self.vocab = {token: integer for token, integer in enumerate(all_words_sorted)}

    def encoder(self, text):
        # split code into the tokens
        # string to integer mapping
        encoded_result = []
        text_split = split(text)
        for token in text_split:
            value_found = False
            for key, value in self.vocab.items():
                if token == value:
                    encoded_result.append(key)
                    value_found = True
                    break
            if not value_found: encoded_result.append(str(token) + ": not in vocab")

        print(encoded_result)


    def decoder(self, ids: list):
        # reverse mapping to convert ids back to text
        decoded_result = []
        key_found = False

        for id in ids :
            for key, value in self.vocab.items():
                if id == key:
                    decoded_result.append(value)
                    key_found = True
                    break

            if not key_found: decoded_result.append(str(id) + ": not in vocab")
        print(decoded_result)

if __name__ == '__main__':
    tokenizer = Tokenizer()
    print(tokenizer.encoder("Begin, Claude!"))
    print(tokenizer.decoder([33]))
    #tokenizer.decoder([1, 2, 3])

    # Tokenizing Text
    # with open("the-verdict.txt", "r", encoding="utf-8") as f:
    #     raw_text = f.read()
    # # use library re to split the text
    # result = re.split(r'([,.:;?_!"()\']|--|\s)', raw_text)
    # print("Total number of character:", len(raw_text))
    # print(raw_text[:99])
    # print(result[:99])

# Converting tokens into token IDs
#  Next, let’s convert these tokens from a Python string to an integer representation to
#  produce the token IDs. This conversion is an intermediate step before converting the
#  token IDs into embedding vectors.
#  To map the previously generated tokens into token IDs, we have to build a vocabu
# lary first.

# sort words alphabetically

    # all_words_sorted = sorted(set(result))
    # print(all_words_sorted)
    # vocab = {token: integer for token, integer in enumerate(all_words_sorted)}
    # print(vocab)
