from email import iterators
from tkinter import W
import nltk
from gensim.corpora import Dictionary
from gensim.models import TfidfModel
from gensim.similarities import SparseTermSimilarityMatrix, WordEmbeddingSimilarityIndex
import model_loader
import itertools
import numpy as np

def preprocess(sentence, stop_words):
    return [w for w in sentence.lower().split() if w not in stop_words]

def train(sentences):
    dictionary = Dictionary(sentences)
    sentences_bow = [dictionary.doc2bow(s) for s in sentences]
    tfidf = TfidfModel(sentences_bow)
    sentences_tfidf = [tfidf[s] for s in sentences_bow]
    termsim_index = WordEmbeddingSimilarityIndex(model_loader.get_model())
    termsim_matrix = SparseTermSimilarityMatrix(termsim_index, dictionary, tfidf)
    return (sentences_tfidf, termsim_matrix)

def find_best_idx(sntnc_sim, num_sntnc):
    list_idxs = np.array(list(itertools.combinations(
        range(sntnc_sim.shape[0]), num_sntnc)))
    ratings = np.zeros(list_idxs.shape[0])
    for i in range(0, num_sntnc - 1):
        for j in range(i + 1, num_sntnc):
            ratings += sntnc_sim[list_idxs[:,i],list_idxs[:,j]]
    min = ratings.argmin()
    return list_idxs[min]

def summarize(text, num_sntnc = 3, language="english"):
    stop_words = set(nltk.corpus.stopwords.words(language))
    sentences_raw = nltk.tokenize.sent_tokenize(text)
    sentences = [preprocess(s, stop_words) for s in sentences_raw]
    N = len(sentences)
    if num_sntnc > N:
        num_sntnc = N / 2

    sntnc_tfidfs, termsim_matrix = train(sentences)

    sntnc_sim = np.eye(N)
    for i in range(N):
        for j in range(i + 1, N):
            sntnc_sim[i,j] = termsim_matrix.inner_product(
                sntnc_tfidfs[i], sntnc_tfidfs[j], normalized=(True, True))

    lowest_sim = find_best_idx(sntnc_sim, num_sntnc)

    summary = []
    for i in lowest_sim:
        summary.append(sentences_raw[i])
    return summary