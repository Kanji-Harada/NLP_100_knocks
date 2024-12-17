import sys

def head(file_path, n):
    """
    指定されたファイルの先頭N行を表示する
    :param file_path: ファイルパス
    :param n: 表示する行数
    """
    with open(file_path, 'r') as file:
        for i, line in enumerate(file):
            if i >= n:
                break
            print(line, end='')

# コマンドライン引数の簡略化
if __name__ == "__main__":
    if len(sys.argv) == 3:
        file_path, n = sys.argv[1], int(sys.argv[2])
        head(file_path, n)
    else:
        print("使い方: python C2_14.py ファイル名 N")
