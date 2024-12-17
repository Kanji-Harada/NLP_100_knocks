def replace_tabs_with_spaces(file_path, output_path):
    """
    ファイル内のタブ文字をスペースに置換して、新しいファイルに保存する
    :param file_path: 入力ファイルのパス
    :param output_path: 出力ファイルのパス
    """
    with open(file_path, 'r') as infile, open(output_path, 'w') as outfile:
        for line in infile:
            outfile.write(line.replace('\t', ' '))

# 入力ファイルと出力ファイルのパスを指定
input_file = 'popular-names.txt'
output_file = 'popular-names-spaces.txt'

# タブをスペースに置換
replace_tabs_with_spaces(input_file, output_file)

print(f"タブをスペースに置換しました。出力ファイル: {output_file}")
