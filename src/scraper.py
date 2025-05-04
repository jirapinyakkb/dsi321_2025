import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime
import os

# ฟังก์ชันดึง URL จริงจาก DuckDuckGo (ปลดรหัส)
def decode_duckduckgo_url(url):
    from urllib.parse import urlparse, parse_qs, unquote
    if "uddg=" in url:
        # ตัด prefix ที่ไม่ใช่ลิงก์จริงออก
        parts = url.split("uddg=")
        decoded_url = unquote(parts[1].split("&")[0])
        return decoded_url
    return url

# ฟังก์ชันหลักในการดึงข้อมูลและบันทึก
def fetch_duckduckgo_news(query, max_results=50):
    url = f'https://duckduckgo.com/html/?q={query}'
    response = requests.get(url)

    if response.status_code == 200:
        print("✅ สำเร็จในการดึงข้อมูล")

        soup = BeautifulSoup(response.text, 'html.parser')
        results = soup.find_all('a', {'class': 'result__a'})

        data = []
        timestamp = datetime.now().isoformat()

        for idx, result in enumerate(results):
            title = result.get_text()
            raw_url = result['href']
            clean_url = decode_duckduckgo_url(raw_url)
            print(f"{idx+1}. {title}")
            print(f"   URL: {clean_url}")
            data.append([title, clean_url, timestamp])


    #     # เขียนลง CSV
    #     with open("data/scraped_results.csv", mode="a", newline="", encoding="utf-8") as file:
    #         writer = csv.writer(file)
            
    #         # ถ้าไฟล์ยังไม่มี header
    #         if os.stat("data/scraped_results.csv").st_size == 0:
    #             writer.writerow(["title", "url", "timestamp"])

    #         writer.writerows(data)

    #     print(f"📁 บันทึก {len(data)} รายการลง data/scraped_results.csv เรียบร้อยแล้ว")
    # else:
    #     print(f"❌ เกิดข้อผิดพลาด: {response.status_code}")

# เรียกใช้งาน
fetch_duckduckgo_news("sustainable construction materials")
