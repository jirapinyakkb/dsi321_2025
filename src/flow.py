from prefect import flow, task
import subprocess

@task
def run_scraper():
    try:
        # เรียกไฟล์ scraper.py ด้วย subprocess
        result = subprocess.run(
            ["python", "/Users/jirapinya1/Desktop/dsi321_2025/src/testv1_scraper.py"],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        # ส่งผลลัพธ์ stdout กลับจาก task นี้
        return result.stdout.decode()
    except subprocess.CalledProcessError as e:
        # แสดงข้อความจาก stderr ถ้ามีข้อผิดพลาด
        return f"Error occurred: {e.stderr.decode()}"

@flow(name="News Scraper Flow")
def news_scraper_flow():
    # เรียกใช้งาน run_scraper และเก็บผลลัพธ์ไว้
    result = run_scraper()
    print(f"Scraper Output: {result}")

if __name__ == "__main__":
    news_scraper_flow()

