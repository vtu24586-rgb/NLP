import numpy as np
import nltk
import spacy

from nltk.tokenize import word_tokenize
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Download resources
nltk.download("punkt")
nltk.download("punkt_tab")
spacy.cli.download("en_core_web_sm")

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Corpus
corpus = """
One disadvantage of using 'Best Of' sampling is that it may lead to limited
exploration of the model's knowledge and creativity. By focusing on the most
probable next words, the model might generate responses that are safe and
conventional, potentially missing out on more diverse and innovative outputs.
The lack of exploration could result in repetitive or less imaginative responses,
especially in situations where novel and unconventional ideas are desired.

To address this limitation, other sampling strategies like temperature-based
sampling or top-p (nucleus) sampling can be employed to introduce more randomness
and encourage the model to explore a broader range of possibilities. However,
it's essential to carefully balance exploration and exploitation based on the
specific requirements of the task or application.
"""

# Tokenize corpus
tokens = word_tokenize(corpus.lower())

# Lemmatize tokens
doc = nlp(corpus.lower())
lemmatized_tokens = [
    token.lemma_
    for token in doc
    if not token.is_space
]

# Choose ONE representation for training.
# Using the original tokens is preferable for a simple language model.
all_tokens = tokens

# Convert tokens to a single text sequence
text = " ".join(all_tokens)

# Create tokenizer
tokenizer = Tokenizer()
tokenizer.fit_on_texts([text])

total_words = len(tokenizer.word_index) + 1

# Convert entire corpus to integer sequence
token_list = tokenizer.texts_to_sequences([text])[0]

# Create n-gram sequences
input_sequences = []

for i in range(1, len(token_list)):
    n_gram_sequence = token_list[:i + 1]
    input_sequences.append(n_gram_sequence)

# Find maximum sequence length
max_sequence_length = max(len(seq) for seq in input_sequences)

# Pad sequences
input_sequences = pad_sequences(
    input_sequences,
    maxlen=max_sequence_length,
    padding="pre"
)

# Split into input and target
X = input_sequences[:, :-1]
y = input_sequences[:, -1]

# Build model
model = Sequential([
    Embedding(
        input_dim=total_words,
        output_dim=100,
        input_length=max_sequence_length - 1
    ),
    LSTM(100),
    Dense(total_words, activation="softmax")
])

# Compile
model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)

# Train
model.fit(
    X,
    y,
    epochs=10,
    verbose=1
)
