print('gen data')
sentence_obama = 'Obama speaks to the media in Illinois'
sentence_president = 'The president greets the press in Chicago'
sentence_orange = 'Oranges are my favorite fruit'

# Import and download stopwords from NLTK.
from nltk.corpus import stopwords
stop_words = stopwords.words('english')

def preprocess(sentence):
    return [w for w in sentence.lower().split() if w not in stop_words]

sentence_obama = preprocess(sentence_obama)
sentence_president = preprocess(sentence_president)
sentence_orange = preprocess(sentence_orange)

print('gen model')

from gensim.corpora import Dictionary
documents = [sentence_obama, sentence_president, sentence_orange]
dictionary = Dictionary(documents)

sentence_obama = dictionary.doc2bow(sentence_obama)
sentence_president = dictionary.doc2bow(sentence_president)
sentence_orange = dictionary.doc2bow(sentence_orange)

from gensim.models import TfidfModel
documents = [sentence_obama, sentence_president, sentence_orange]
tfidf = TfidfModel(documents)

sentence_obama = tfidf[sentence_obama]
sentence_president = tfidf[sentence_president]
sentence_orange = tfidf[sentence_orange]

print('init model')
import gensim.downloader as api
model = api.load('glove-wiki-gigaword-100')

print('train matrix')

from gensim.similarities import SparseTermSimilarityMatrix, WordEmbeddingSimilarityIndex
termsim_index = WordEmbeddingSimilarityIndex(model)
termsim_matrix = SparseTermSimilarityMatrix(termsim_index, dictionary, tfidf)

print(type(termsim_matrix))

