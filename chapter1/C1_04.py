# 対象の文
sentence = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

# 単語に分解し、句読点を除去
words = sentence.replace(".", "").split()

# 1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語（1文字を取り出す位置）集合で指定するとin演算子で素早く確認できる
one_letter_positions = {1, 5, 6, 7, 8, 9, 15, 16, 19}

# 単語の位置と先頭文字を格納する辞書を生成
result = {index: (word[0] if index in one_letter_positions else word[:2]) 
          for index, word in enumerate(words, start=1)}

print(result)
