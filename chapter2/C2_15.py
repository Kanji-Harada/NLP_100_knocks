import sys

def tail(file_path, n):
    """
    指定されたファイルの末尾N行を表示する
    :param file_path: ファイルパス
    :param n: 表示する行数
    """
    with open(file_path, 'r') as file:
        # 全行を読み込んで末尾N行を取得
        lines = file.readlines()[-n:]
        for line in lines:
            print(line, end='')

# コマンドライン引数の処理
if __name__ == "__main__":
    if len(sys.argv) == 3:
        file_path, n = sys.argv[1], int(sys.argv[2])
        tail(file_path, n)
    else:
        print("使い方: python C2_15.py ファイル名 N")
        
