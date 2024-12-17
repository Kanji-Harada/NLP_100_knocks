#対象の文
sentence = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

# 単語に分解し、句読点を除去 replace(old,new)
words = sentence.replace(",", "").replace(".", "").split()

# 各単語の文字数をリストに格納
word_lengths = [len(word) for word in words]

print(word_lengths)
