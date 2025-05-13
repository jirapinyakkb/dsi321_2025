from prefect import flow, task
import subprocess

@task
def run_scraper():
    subprocess.run(["python", "testv1_scraper.py"], check=True)

@flow(name="News Scraper Flow")
def news_scraper_flow():
    run_scraper()

if __name__ == "__main__":
    news_scraper_flow()
