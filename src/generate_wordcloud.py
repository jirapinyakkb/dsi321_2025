from wordcloud import WordCloud  # นำเข้าจากไลบรารี wordcloud แทน
import matplotlib.pyplot as plt
import pandas as pd

# โหลดข้อมูล
df = pd.read_csv("data/testv1_scraped.csv")

# รวมข้อความ title ทั้งหมด
text = ' '.join(df['title'].dropna().astype(str))

# สร้าง word cloud
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

# แสดงผล
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title("📰 Word Cloud from News Titles")
plt.show()
