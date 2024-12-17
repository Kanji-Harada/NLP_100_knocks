import random

def shuffle_inner(word):
    """
    単語の先頭と末尾を残し、それ以外の文字をランダムに並び替える関数。
    長さが4以下の単語はそのまま返す。
    :param word: 単語
    :return: 並び替え後の単語
    """
    if len(word) <= 4:
        return word
    # 内部の文字をランダムに並び替える
    inner = list(word[1:-1])
    random.shuffle(inner)
    return word[0] + ''.join(inner) + word[-1]

def process_sentence(sentence):
    """
    文をスペースで区切り、各単語を shuffle_inner 関数で処理する。
    :param sentence: 入力文
    :return: 処理後の文
    """
    words = sentence.split()
    return ' '.join(shuffle_inner(word) for word in words)

# 入力文
sentence = "I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

# 処理実行
result = process_sentence(sentence)

print("Original Sentence:", sentence)
print("Processed Sentence:", result)
