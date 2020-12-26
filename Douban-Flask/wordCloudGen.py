import numpy as np
import sqlite3
import jieba
import matplotlib.pyplot as plt
from PIL import Image
from wordcloud import WordCloud, ImageColorGenerator

db = sqlite3.connect('movie.db')
cur = db.cursor()
sql = "select summ from movie250"
data = cur.execute(sql)
text = ""
for item in data:
    text += item[0]
cur.close()
db.close()

cut = jieba.cut(text)
cut = list(cut)
text = cut[:]
for item in cut:
    if len(item) < 2:
        text.remove(item)
text = ' '.join(text)

img = Image.open(r'static/assets/img/wc-cover.jpg')
arr = np.array(img)
wc = WordCloud(
    scale=4, # Better Resolution
    background_color=None,
    mode="RGBA",
    mask=arr,
    font_path="STZHONGS.TTF",
)
wc.generate_from_text(text)

# plt.figure()
# plt.imshow(wc)
# plt.axis('off')
#
# plt.savefig(r"static/assets/img/wc3.jpg", dpi=500)
wc.to_file(r"static/assets/img/wc4.png")
