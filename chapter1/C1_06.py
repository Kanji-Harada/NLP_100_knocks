def n_gram(sequence, n):
    """
    与えられたシーケンスから n-gram を生成する関数
    :param sequence: リストや文字列などのシーケンス
    :param n: n-gram の n の値
    :return: n-gram のリスト
    """
    return [sequence[i:i+n] for i in range(len(sequence) - n + 1)]

# 文字列
str1 = "paraparaparadise"
str2 = "paragraph"

# bi-gram を生成して集合に変換
X = set(n_gram(str1, 2))
Y = set(n_gram(str2, 2))

# 和集合、積集合、差集合を計算
union = X | Y
intersection = X & Y
difference = X - Y

# 'se' が含まれるかをチェック
contains_se_X = 'se' in X
contains_se_Y = 'se' in Y

# 結果の表示
print("X:", X)
print("Y:", Y)
print("和集合:", union)
print("積集合:", intersection)
print("差集合 (X - Y):", difference)
print("'se' が X に含まれるか:", contains_se_X)
print("'se' が Y に含まれるか:", contains_se_Y)
