import json
import re

def extract_uk_article(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            data = json.loads(line)
            if data.get('title') == 'イギリス':
                return data
            
def clean_markup(text):
    # Remove MediaWiki emphasis markup (e.g., '', ''' and ''''')
    text = re.sub(r"''+", "", text)
    # Remove MediaWiki internal link markup (e.g., [[Article|displayed text]] or [[Article]])
    text = re.sub(r"\[\[(?:[^|\]]*\|)?([^\]]+)\]\]", r"\1", text)
    # Remove external links (e.g., [https://example.com description])
    text = re.sub(r"\[https?://[^ ]+ (.*?)\]", r"\1", text)
    # Remove HTML tags (e.g., <ref>...</ref>, <br>, etc.)
    text = re.sub(r"<ref.*?>.*?</ref>", "", text)
    text = re.sub(r"<ref.*?>|<br />", "", text)
    # Remove file markup (e.g., [[File:example.jpg|...]])
    text = re.sub(r"\[\[File:[^\]]+\]\]", "", text)
    # Remove {{lang|...|foreign text}} markup
    text = re.sub(r"\{\{lang\|.*?\|", "", text)
    # Remove nested {{center|...}} markup
    text = re.sub(r"\{\{.*?\{\{center\|", "", text)
    # Remove {{仮リンク|...|...|...}} markup
    text = re.sub(r"\{\{.*?\|.*?\|.{2}\|", "", text)
    # Remove {{...}} markup
    text = re.sub(r"\{\{.*?\}\}", "", text)
    # Remove stray }}
    text = re.sub(r"\}\}", "", text)
    return text

def extract_infobox_fields(article_text):
    pattern = r'\{\{基礎情報.*?\n(.*?)\n\}\}'
    match = re.search(pattern, article_text, re.DOTALL)
    if not match:
        return {}

    fields_text = match.group(1)
    field_pattern = r'\|\s*(.*?)\s*=\s*(.*?)\s*(?=\n\||\n$)'
    fields = re.findall(field_pattern, fields_text, re.DOTALL)
    return {field[0]: clean_markup(field[1].strip()) for field in fields}

# ファイルのパスを指定
file_path = 'jawiki-country.json/jawiki-country.json'

# 「イギリス」に関する記事を抽出
uk_article = extract_uk_article(file_path)

# 結果を表示
if uk_article:
    article_text = uk_article.get('text', '')
    
    # 基礎情報のフィールド名と値
    infobox = extract_infobox_fields(article_text)
    print("\n基礎情報:")
    for key, value in infobox.items():
        print(f"{key}: {value}")
else:
    print("イギリスの記事が見つかりませんでした。")
