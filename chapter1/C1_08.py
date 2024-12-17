def cipher(text):
    """
    与えられた文字列の各文字を以下の仕様で変換する関数:
    - 英小文字: (219 - 文字コード) の文字に置換
    - その他の文字: そのまま出力
    :param text: 入力文字列
    :return: 変換後の文字列
    """
    return ''.join(
        chr(219 - ord(char)) if 'a' <= char <= 'z' else char
        for char in text
    )

# 暗号化と復号化の実行例
message = "I love python"
encrypted = cipher(message)
decrypted = cipher(encrypted)

print("Original Message:", message)
print("Encrypted Message:", encrypted)
print("Decrypted Message:", decrypted)
