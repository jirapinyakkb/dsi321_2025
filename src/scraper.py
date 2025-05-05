'''import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime
import os
import time

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
    
    # เพิ่ม headers เพื่อหลีกเลี่ยงการบล็อค
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Referer': 'https://duckduckgo.com'
}



    # ลองส่ง request 3 ครั้ง
    for attempt in range(3):
        response = requests.get(url, headers=headers)
        print(f"Status Code: {response.status_code}")  # ดู status code ของ response
        if response.status_code == 200:
            print("✅ สำเร็จในการดึงข้อมูล")
            
            # ดู HTML ที่ได้รับ
            soup = BeautifulSoup(response.text, 'html.parser')
            print(soup.prettify())  # แสดง HTML ที่ได้มา

            # ค้นหาผลลัพธ์
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

            # เขียนลง CSV
            os.makedirs("data", exist_ok=True)
            with open("data/scraped_results.csv", mode="a", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                
                # ถ้าไฟล์ยังไม่มี header
                if os.stat("data/scraped_results.csv").st_size == 0:
                    writer.writerow(["title", "url", "timestamp"])

                writer.writerows(data)

            print(f"📁 บันทึก {len(data)} รายการลง data/scraped_results.csv เรียบร้อยแล้ว")
            break
        else:
            print(f"❌ เกิดข้อผิดพลาด: {response.status_code}, พยายามใหม่ครั้งที่ {attempt+1}...")
            time.sleep(3)  # รอ 3 วินาทีก่อนจะลองใหม่
    else:
        print("❌ ไม่สามารถดึงข้อมูลได้หลังจากลอง 3 ครั้ง")


# เรียกใช้งาน
fetch_duckduckgo_news("materials") '''

import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime
import os
import time

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
    
    # เพิ่ม headers เพื่อหลีกเลี่ยงการบล็อค
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    # ลองส่ง request 3 ครั้ง
    for attempt in range(3):
        response = requests.get(url, headers=headers)

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

            # เขียนลง CSV
            os.makedirs("data", exist_ok=True)
            with open("data/scraped_results.csv", mode="a", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                
                # ถ้าไฟล์ยังไม่มี header
                if os.stat("data/scraped_results.csv").st_size == 0:
                    writer.writerow(["title", "url", "timestamp"])

                writer.writerows(data)

            print(f"📁 บันทึก {len(data)} รายการลง data/scraped_results.csv เรียบร้อยแล้ว")
            break
        else:
            print(f"❌ เกิดข้อผิดพลาด: {response.status_code}, พยายามใหม่ครั้งที่ {attempt+1}...")
            time.sleep(3)  # รอ 3 วินาทีก่อนจะลองใหม่
    else:
        print("❌ ไม่สามารถดึงข้อมูลได้หลังจากลอง 3 ครั้ง")

# เรียกใช้งาน
fetch_duckduckgo_news("sustainable construction materials")