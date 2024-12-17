def count_lines(file_path):
    """
    指定されたファイルの行数をカウントする関数
    :param file_path: ファイルパス
    :return: 行数
    """
    with open(file_path, 'r') as file:
        return sum(1 for _ in file)

# 入力ファイル
file_path = 'popular-names.txt'

# 実行
line_count = count_lines(file_path)
print(f"Number of lines: {line_count}")
