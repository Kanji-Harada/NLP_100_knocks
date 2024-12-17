def extract_columns(input_file, col1_file, col2_file):
    """
    入力ファイルの1列目と2列目をそれぞれ別のファイルに保存する
    :param input_file: 入力ファイルパス
    :param col1_file: 1列目を保存するファイルパス
    :param col2_file: 2列目を保存するファイルパス
    """
    with open(input_file, 'r') as infile, \
         open(col1_file, 'w') as col1_outfile, \
         open(col2_file, 'w') as col2_outfile:
        for line in infile:
            columns = line.strip().split('\t')  # タブで分割
            if len(columns) >= 2:  # 少なくとも2列がある場合のみ処理
                col1_outfile.write(columns[0] + '\n')
                col2_outfile.write(columns[1] + '\n')

# ファイルパスの設定
input_file = 'popular-names.txt'
col1_file = 'col1.txt'
col2_file = 'col2.txt'

# 列の抽出を実行
extract_columns(input_file, col1_file, col2_file)

print(f"1列目を {col1_file} に、2列目を {col2_file} に保存しました。")