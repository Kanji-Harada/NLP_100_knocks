import json
import re

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

if uk_article:
    pattern = r'\[\[Category:.+?\]\]'
    text_content = uk_article.get('text', '')
    result = re.findall(pattern, text_content)
    print(result)
else:
    print("イギリスの記事が見つかりませんでした。")

