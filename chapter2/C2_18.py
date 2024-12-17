def sort_by_third_column(file_path, output_path):
    """
    ファイルを3列目の数値をキーにして逆順でソートし、結果を新しいファイルに保存する
    :param file_path: 入力ファイルのパス
    :param output_path: ソート結果を保存するファイルのパス
    """
    with open(file_path, 'r') as file:
        # 各行をリストとして読み込み
        lines = file.readlines()
        # 3列目を数値として抽出して逆順にソート
        sorted_lines = sorted(lines, key=lambda x: int(x.split('\t')[2]), reverse=True)
    
    # 結果をファイルに保存
    with open(output_path, 'w') as output_file:
        output_file.writelines(sorted_lines)

# 実行例
file_path = 'popular-names.txt'
output_path = 'sorted-names.txt'

sort_by_third_column(file_path, output_path)
print(f"3列目の数値で逆順にソートし、結果を '{output_path}' に保存しました。")
