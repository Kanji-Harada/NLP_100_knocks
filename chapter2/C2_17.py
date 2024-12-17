def unique_column_values(file_path, column_index):
    """
    指定されたファイルの指定列に含まれる異なる文字列を求める
    :param file_path: ファイルパス
    :param column_index: 対象列のインデックス（0始まり）
    :return: 異なる文字列の集合
    """
    with open(file_path, 'r') as file:
        unique_values = {line.split('\t')[column_index] for line in file} #重複を防ぎたいときは集合で得る
    return unique_values

# ファイルと列番号を指定
file_path = 'popular-names.txt'
column_index = 0  # 1列目を指定

# 実行
unique_values = unique_column_values(file_path, column_index)
print("1列目の異なる文字列の種類:")
for value in sorted(unique_values):
    print(value)
