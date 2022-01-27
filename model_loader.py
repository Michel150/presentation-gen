import gensim.downloader as api

model = 0
def get_model():
    global model
    if model != 0:
        return model
    model = api.load('glove-wiki-gigaword-100')
    return model
