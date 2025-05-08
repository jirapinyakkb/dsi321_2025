from wordcloud import WordCloud  # นำเข้าจากไลบรารี wordcloud แทน
import matplotlib.pyplot as plt
import pandas as pd

# โหลดข้อมูล
df = pd.read_csv("data/testv1_scraped.csv")

# รวมข้อความ title ทั้งหมด
text = ' '.join(df['title'].dropna().astype(str))

# สร้าง word cloud พร้อมจำกัดคำที่แสดงแค่ 15 คำ
wordcloud = WordCloud(width=800, height=400, background_color='white', max_words=15).generate(text)

# แสดงผล
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title("📰 Word Cloud from Top 15 News Titles")
plt.show()
