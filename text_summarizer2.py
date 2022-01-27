import nltk
import numpy as np

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
    words = nltk.tokenize.word_tokenize(text)

    freqTable = generate_wordfreq(words, stopWords)
    
    sentences = nltk.tokenize.sent_tokenize(text)
    sentences_l = [s.lower().split() for s in sentences]
    sentenceValue = np.zeros(len(sentences_l))
    
    for i, sentence_l in enumerate(sentences_l):
        print(sentence_l)
        for word, freq in freqTable.items():
            if word in sentence_l:
                sentenceValue[i] += freq
    
    average = np.mean(sentenceValue)
    
    # Storing sentences into our summary.
    summary = ''
    for i, sentence in enumerate(sentences):
        if sentenceValue[i] > (1.2 * average):
            summary += " " + sentence
    return summary

with open("./tmp.txt", "r") as f:
    text = f.read()
    print(f"pre: \n{text}\n")
    summary = summarize(text)
    print(f"after: \n{summary}\n")