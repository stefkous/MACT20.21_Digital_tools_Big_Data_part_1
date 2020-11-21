from wordcloud import WordCloud
import matplotlib.pyplot as plt

text = open('../new_data/spatial_dataset').read()
text = text.upper()

# Create the wordcloud object
wordcloud = WordCloud(width=480, height=480, margin=0).generate(text)

# Display the generated image:
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.margins(x=0, y=0)
plt.show()
