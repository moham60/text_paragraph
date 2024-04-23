import nltk
from nltk.corpus import stopwords
from collections import Counter

# Download NLTK resources (run only once)
nltk.download('punkt')
nltk.download('stopwords')

# File path to the random_paragraphs.txt within the Docker container
file_path = "paragraph.txt"

# Read the contents of the file
with open(file_path, "r") as file:
    text = file.read()

# Tokenize the text into words
words = nltk.word_tokenize(text)

# Remove stop words
stop_words = set(stopwords.words('english'))
filtered_words = [word for word in words if word.lower() not in stop_words]

# Count the frequency of each word
word_frequency = Counter(filtered_words)

# Display word frequency count
for word, freq in word_frequency.items():
    print(f"{word}: {freq}")
