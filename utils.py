import regex as re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.snowball import SnowballStemmer
from nltk.stem.wordnet import WordNetLemmatizer

# Define the function to preprocess text
def remove_and_convert(text):
    # Remove all special characters
    text = re.sub(r'[^a-zA-Z\s]', '', text)

    # Remove numbers
    text = re.sub(r'\d', '', text)

    # Remove all single characters
    text = re.sub(r'\b\w\b', '', text)

    # Remove single characters from the start
    text = re.sub(r'^\w\s', '', text)

    # Substitute multiple spaces with single space
    text = re.sub(r'\s+', ' ', text)

    # Convert to Lowercase
    text = text.lower()

    return text

# Define the function to remove all stopwords


def remove_stopwords(text):
    stop_words = stopwords.words('english')
    text = ' '.join([word for word in text.split() if word not in stop_words])
    return text


# tokenize, lowercase, remove punctuation
def tokenizer(text):
    return word_tokenize(text)


# Define the function to stem words
def stem_words(text):
    stemmer = SnowballStemmer('english')
    # use: text = ' '.join([stemmer.stem(word) for word in text.split()]) if
    # not tokenized
    text = ' '.join([stemmer.stem(word) for word in text])
    return text


# Define the function to lemmatize words
def lemmatize_words(text):
    lemmatizer = WordNetLemmatizer()
    # use: text = ' '.join([lemmatizer.lemmatize(word) for word in
    # text.split()]) if not tokenized
    text = ' '.join([lemmatizer.lemmatize(word) for word in text])
    return text
