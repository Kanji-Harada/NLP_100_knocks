import json

def extract_uk_article(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            data = json.loads(line)
            if data.get('title') == 'イギリス':
                return data

# ファイルのパスを指定
file_path = 'jawiki-country.json/jawiki-country.json'

# 「イギリス」に関する記事を抽出
uk_article = extract_uk_article(file_path)

# 結果を表示
if uk_article:
    print(uk_article)
else:
    print("イギリスの記事が見つかりませんでした。")
