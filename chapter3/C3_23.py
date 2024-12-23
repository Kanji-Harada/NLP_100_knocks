import json
import re

def extract_uk_article(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            data = json.loads(line)
            if data.get('title') == 'イギリス':
                return data

def extract_section_names_and_levels(article_text):
    pattern = r'^(={2,})\s*(.*?)\s*\1$'
    matches = re.findall(pattern, article_text, re.MULTILINE)
    return [(match[1], len(match[0]) - 1) for match in matches]

# ファイルのパスを指定
file_path = 'jawiki-country.json/jawiki-country.json'

# 「イギリス」に関する記事を抽出
uk_article = extract_uk_article(file_path)

# 結果を表示
if uk_article:
    article_text = uk_article.get('text', '')
    sections = extract_section_names_and_levels(article_text)
    for section, level in sections:
        print(f"Level {level}: {section}")
else:
    print("イギリスの記事が見つかりませんでした。")
