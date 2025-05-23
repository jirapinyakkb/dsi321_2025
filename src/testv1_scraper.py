import feedparser
import csv
from datetime import datetime
import os

# คำค้นหาหลายคำที่เกี่ยวกับ alternative construction materials
search_keywords = [
    "sustainable construction materials",
    "eco friendly building materials",
    "alternative construction methods",
    "green building materials",
    "recycled construction materials",
    "low carbon construction materials",
    "biodegradable construction materials",
    "natural building materials",
    "energy efficient building materials",
    "renewable construction resources",
    "zero waste construction materials",
    "earth friendly construction",
    "carbon neutral building materials",
    "hempcrete construction",
    "rammed earth construction",
    "reclaimed wood building materials",
    "innovative sustainable construction",
    "circular economy construction materials",
    "sustainable architecture materials"
]

# โฟลเดอร์และชื่อไฟล์
os.makedirs("data", exist_ok=True)
csv_path = os.path.join("data", "testv1_scraped.csv")
file_exists = os.path.isfile(csv_path)

# โหลดลิงก์ที่เคยบันทึกไว้
existing_links = set()
if file_exists:
    with open(csv_path, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        if reader.fieldnames and "link" in reader.fieldnames:
            for row in reader:
                existing_links.add(row["link"])
        else:
            print("❌ ไม่พบหรือไม่มี field 'link' ในไฟล์ CSV")

# เตรียมเขียน CSV
new_entries = 0
with open(csv_path, mode='a', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)

    # เขียน header ถ้ายังไม่มีไฟล์
    if not file_exists:
        writer.writerow(["title", "link", "published", "fetched_at", "keyword"])

    for keyword in search_keywords:
        rss_url = f"https://news.google.com/rss/search?q={keyword.replace(' ', '+')}"
        feed = feedparser.parse(rss_url)

        for entry in feed.entries:
            if entry.link not in existing_links:
                writer.writerow([
                    entry.title,
                    entry.link,
                    entry.published,
                    datetime.now().isoformat(),
                    keyword
                ])
                existing_links.add(entry.link)
                new_entries += 1

print(f"✅ ดึงข่าวใหม่ {new_entries} รายการจาก {len(search_keywords)} คำค้นและบันทึกลง testv1_scraped.csv แล้ว")
