str1 = "パトカー"
str2 = "タクシー"

# zip関数で文字を交互に結合
result = "".join(a + b for a, b in zip(str1, str2))

print(result)
