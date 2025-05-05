from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import csv
import os

# ========== ตั้งค่า Selenium ========== #
options = Options()
# ไม่เปิด headless เพื่อหลีกเลี่ยงการโดนบล็อก
# options.add_argument("--headless")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# ========== ไปที่ SCG Home ========== #
search_query = "วัสดุก่อสร้าง"
url = f"https://www.scghome.com/search?q={search_query}"
driver.get(url)
time.sleep(5)  # รอโหลดหน้า

# ========== ดึงข้อมูลสินค้า ========== #
items = driver.find_elements(By.CSS_SELECTOR, "div.card")  # สินค้าแต่ละชิ้น

data = []
timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

for item in items[:10]:  # ดึง 10 ชิ้นพอ
    try:
        title = item.find_element(By.CSS_SELECTOR, ".product-title").text
        price = item.find_element(By.CSS_SELECTOR, ".price-main").text
        link = item.find_element(By.TAG_NAME, "a").get_attribute("href")
        print(f"{title} - {price} - {link}")
        data.append([title, price, link, timestamp])
    except:
        continue  # ข้ามถ้าเจอ error

# ========== บันทึกลง CSV ========== #
os.makedirs("data", exist_ok=True)
filepath = "data/testv1_scraped.csv"

with open(filepath, mode="a", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    if os.stat(filepath).st_size == 0:
        writer.writerow(["Title", "Price", "Link", "Timestamp"])
    writer.writerows(data)

print(f"\n✅ บันทึก {len(data)} รายการลง {filepath}")
driver.quit()
