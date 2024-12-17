def combine_columns(col1_file, col2_file, output_file):
    """
    col1.txt と col2.txt を結合し、タブ区切りで並べたテキストファイルを作成する
    :param col1_file: 1列目のファイル
    :param col2_file: 2列目のファイル
    :param output_file: 結合結果を保存するファイル
    """
    with open(col1_file, 'r') as col1, open(col2_file, 'r') as col2, open(output_file, 'w') as outfile:
        for col1_line, col2_line in zip(col1, col2):
            # タブ区切りで結合して書き込む
            outfile.write(f"{col1_line.strip()}\t{col2_line.strip()}\n")

# 入力ファイル
col1_file = 'col1.txt'
col2_file = 'col2.txt'
output_file = 'combined.txt'

# 実行
combine_columns(col1_file, col2_file, output_file)

print(f"{col1_file} と {col2_file} を結合して {output_file} を作成しました。")
