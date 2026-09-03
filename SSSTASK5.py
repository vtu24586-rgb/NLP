import string
import random
import nltk

from nltk.corpus import stopwords, reuters
from collections import Counter, defaultdict
from nltk import FreqDist, ngrams

# Download required datasets
nltk.download('reuters')
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('punkt_tab')

# Load Reuters sentences
sents = reuters.sents()

# Stopwords
stop_word = set(stopwords.words('english'))

# Punctuation
removal_list = stop_word.union(set(string.punctuation))
removal_list.update(['\t', 'rt'])

# Lists
unigram = []
bigram = []
trigram = []
tokenized_text = []

# Process sentences
for sentence in sents:

    # Convert to lowercase
    sentence = [word.lower() for word in sentence]

    # Remove stopwords and punctuation
    sentence = [
        word for word in sentence
        if word not in removal_list
    ]

    # Store tokens
    unigram.extend(sentence)
    tokenized_text.append(sentence)

    # Generate bigrams
    bigram.extend(
        ngrams(sentence, 2, pad_left=True, pad_right=True)
    )

    # Generate trigrams
    trigram.extend(
        ngrams(sentence, 3, pad_left=True, pad_right=True)
    )

# Frequency distributions
freq_uni = FreqDist(unigram)
freq_bi = FreqDist(bigram)
freq_tri = FreqDist(trigram)

# Create trigram dictionary
d = defaultdict(Counter)

for (a, b, c), count in freq_tri.items():

    if a is not None and b is not None and c is not None:
        d[(a, b)][c] += count

# Random word selection
def pick_word(counter):
    return random.choice(list(counter.elements()))

# Select a prefix that exists
prefix = next(iter(d))

print("Starting words:", " ".join(prefix))

s = " ".join(prefix)

# Generate 19 words
for i in range(19):

    if prefix not in d:
        break

    suffix = pick_word(d[prefix])

    s = s + " " + suffix

    print(s)

    prefix = (prefix[1], suffix)
