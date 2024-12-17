from collections import Counter

def count_and_sort_frequencies(file_path):
    """
    各行の1列目の文字列の出現頻度を求め、高い順に並べて表示する
    :param file_path: 入力ファイルのパス
    """
    with open(file_path, 'r') as file:
        # 1列目を取得して出現頻度をカウント
        first_column = [line.split('\t')[0] for line in file]
        frequencies = Counter(first_column)
    
    # 出現頻度の降順に並べ替えて表示
    for word, count in frequencies.most_common():
        print(f"{word}: {count}")

# ファイルパスを指定
file_path = 'popular-names.txt'
count_and_sort_frequencies(file_path)
