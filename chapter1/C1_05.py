def n_gram(sequence, n):
    """
    与えられたシーケンスから n-gram を生成する関数
    :param sequence: リストや文字列などのシーケンス
    :param n: n-gram の n の値
    :return: n-gram のリスト
    """
    return [sequence[i:i+n] for i in range(len(sequence) - n + 1)]

# 対象の文
sentence = "I am an NLPer"

# 単語 bi-gram
words = sentence.split()  # 文を単語に分割
word_bigrams = n_gram(words, 2)  # 単語 bi-gram を生成

# 文字 bi-gram
char_bigrams = n_gram(sentence.replace(" ", ""), 2)  # 空白を除去して文字 bi-gram を生成

# 結果の表示
print("単語 bi-gram:", word_bigrams)
print("文字 bi-gram:", char_bigrams)

