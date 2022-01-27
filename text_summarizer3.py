import nltk
import numpy as np
from sklearn import feature_extraction

def generate_wordfreq(words, stopWords):
    freqTable = dict()
    for word in words:
        word = word.lower()
        if word in stopWords:
            continue
        if word in freqTable:
            freqTable[word] += 1
        else:
            freqTable[word] = 1
    return freqTable
   
def summarize(text, language="english"):
    stopWords = set(nltk.corpus.stopwords.words(language))
    sentences = nltk.tokenize.sent_tokenize(text)
    print(sentences)

    vectorizer = feature_extraction.text.TfidfVectorizer(stop_words = stopWords).fit(sentences)
    tfidf_matrix = vectorizer.transform(sentences)
    print(vectorizer.get_feature_names_out())
    print(tfidf_matrix)
    means = np.mean(tfidf_matrix, axis=1)
    print(means)

    threshold = np.mean(means) * 1.0
    summary = []
    for i, sentence in enumerate(sentences):
        if means[i] >= threshold:
            words = nltk.tokenize.word_tokenize(sentence)
            summary.append(" ".join(words))
    return summary
    

with open("./tmp.txt", "r") as f:
    text = f.read()
    print(f"pre: \n{text}\n")
    summary = summarize(text)
    print(f"after: \n{summary}\n")