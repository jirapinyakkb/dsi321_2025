import csv
from collections import Counter

csv_path = "data/testv1_scraped.csv"
title_link_pairs = []

with open(csv_path, mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    if reader.fieldnames and "title" in reader.fieldnames and "link" in reader.fieldnames:
        for row in reader:
            title_link_pairs.append((row["title"], row["link"]))
    else:
        print("❌ ไม่พบ field 'title' หรือ 'link' ในไฟล์")

# นับจำนวน (title, link) ที่ซ้ำกัน
pair_counts = Counter(title_link_pairs)
duplicates = {pair: count for pair, count in pair_counts.items() if count > 1}

if duplicates:
    print(f"❗ พบข้อมูลซ้ำทั้งหมด {len(duplicates)} รายการ:")
    for (title, link), count in duplicates.items():
        print(f"Title: {title}\nLink: {link}\nซ้ำ {count} ครั้ง\n")
else:
    print("✅ ไม่พบข้อมูลซ้ำใน (title, link)")
