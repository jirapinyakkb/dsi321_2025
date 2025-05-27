# DSI321_BT_Materials
    This project tracks real-time news on sustainable construction materials using a scheduled scraping pipeline and visualizes the results via a Streamlit dashboard.

- `Key Features`
Automated Scraping: Fetches news every 15 minutes using feedparser + Prefect 2.0.
Data Storage: Stores structured, partitioned Parquet files in a version-controlled lakeFS data lake.
Visualization: Word Cloud & topic trends via Streamlit dashboard.
Text Processing: Uses re, nltk, and pandas for title cleaning and transformation.
Environment: Docker Compose setup with Prefect Server, PostgreSQL, lakeFS.
Version Control: Git & GitHub with >15 commits over 3 weeks.

- `Benefits`
    Real-time insights into green building trends, materials, and supply chain.
Supports decision-making for procurement, ESG reporting, and R&D.
Easy access to clean, versioned, and reproducible news data.

`Tools & Stack`

    feedparser, pandas, nltk, re, lakeFS, Prefect 2.0, Streamlit, Docker Compose

# Prepare & Run the Project
---
# File Structure
       
    .
    ├── README.md
    ├── data
    │   └── testv1_scraped.csv
    ├── image
    │   └── wordcloud.jpg
    ├── requirements.txt
    └── src
        ├── Dockerfile.cli
        ├── __pycache__
        │   ├── flow.cpython-313.pyc
        │   └── generate_wordcloud.cpython-313.pyc
        ├── check_duplicates.py
        ├── config_path.py
        ├── docker-compose.yml
        ├── generate_wordcloud.py
        ├── main.py
        ├── minmax_publish.py
        ├── pyproject.toml
        ├── removestopword.py
        ├── start.sh
        └── streamlis.py
        └── venv
    
    
    
# Requirements

Make sure you have **Python 3.7+** installed, then install the following packages:

- `pandas`
- `requests`
- `beautifulsoup4`
- `selenium`
- `webdriver-manager`
- `feedparser`
- `wordcloud`
- `matplotlib`
- `prefect>=2.0`
- `streamlit`
- `nltk`


Install them via:

    pip install -r requirements.txt

# Usage

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/dsi321_2025.git
    cd dsi321_2025
    ```

2. Create a virtual environment 
    ```bash
    python3 -m venv venv
    ```

    and activate it:

    ```bash
    source venv/bin/activate
    ```

3. Run for scraping
    ```bash
    python src/main.py
    ```

4. Git Push Example

    ```bash
    git add .
    git commit -m "your comment"
    git push
    ```


# First Run

5. The script will fetch news articles based on these keywords:
    ```bash
     search_keywords = [
    "sustainable construction materials",
    "eco friendly building materials",
    "alternative construction methods",
    "green building materials"
    ]

6. All results will be automatically saved to:
    ```bash
    data/testv1_scraped.csv

The script ensures there are no duplicate links, even when running multiple times.

7. Check for Duplicates
    To verify if there are any duplicate news entries (based on both title and link), you can run:
    ```bash
    python src/check_duplicates.py


# This script will read from:

    data/testv1_scraped.csv

and show how many duplicates exist, if any.

The check is based on (title, link) pairs.
It helps ensure your dataset is clean and ready for further analysis or visualization.

# Second Run

8. Add the script will fetch news articles based on these keywords:
    ```bash

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
    ]

# Third Run

9. Add the script will fetch news articles based on these keywords:
    ```bash

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

# How to run for create WORDCLOUD   

10. ```bash
    python src/generate_wordcloud.py
    ```


###  Word Cloud from News title


![Word Cloud](image/wordcloud.jpg)



11. how to check min_max_publish

    ```bash
    python src/minmax_publish.py
    ```


# Output

The output 

1. `testv1_scraped.csv ` file includes the following columns:

   - title: News title
   - link: Direct URL to the news
   - published: Published date
   - fetched_at: The timestamp the data was fetched
   - keyword: The search keyword that matched the article

2. Wordcloud form `src/generate_wordcloud.py`

3. Git Push Example

    ```bash
    git add .
    git commit -m "your comment"
    git push

# Running with Docker and Prefect (for scheduling and orchestration)

1. Start Docker Services (Prefect + lakeFS + DB)
    ```bash
    docker compose --profile server up -d     # Start Prefect server & database
    docker compose --profile worker up -d     # Start Prefect worker
    docker compose --profile cli run cli      # (Optional) Get a shell in CLI container

2. Deploy or Run the Scraping Flow
    To deploy the Prefect flow that runs every 15 minutes:

    ```bash
    python src/main_2.py

    Or to run it manually (once):

    ```bash
    python src/main_2.py

3. Launch the Streamlit Dashboard

    ```bash    
    streamlit run src/streamlit.py

4. View Prefect UI Open your browser and go to:

    ```bash
    http://localhost:4200

You can monitor scheduled runs and logs from the Prefect UI here.

# Author
    
    6524651186 Jirapinya Thanansophon