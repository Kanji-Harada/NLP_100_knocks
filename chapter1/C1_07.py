def create_sentence(x, y, z):
    """
    引数 x, y, z を受け取り、「x時のyはz」という文字列を返す関数
    :param x: 時刻 (例: 12)
    :param y: 対象 (例: "気温")
    :param z: 値 (例: 22.4)
    :return: フォーマットされた文字列
    """
    return f"{x}時の{y}は{z}"

# 関数の実行例
x = 12
y = "気温"
z = 22.4
result = create_sentence(x, y, z)

print(result)
