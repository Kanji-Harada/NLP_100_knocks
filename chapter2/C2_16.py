import sys

def split_file(file_path, n):
    """
    入力ファイルを行単位でN分割する
    :param file_path: 入力ファイルのパス
    :param n: 分割する数
    """
    with open(file_path, 'r') as file:
        lines = file.readlines()
        chunk_size = -(-len(lines) // n)  # 切り上げ計算
        for i in range(n):
            with open(f"{file_path}_{i + 1}.txt", 'w') as output:
                output.writelines(lines[i * chunk_size:(i + 1) * chunk_size])

if __name__ == "__main__":
    if len(sys.argv) == 3:
        split_file(sys.argv[1], int(sys.argv[2]))
    else:
        print("使い方: python C2_16.py ファイル名 N")
