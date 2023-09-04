# load pretrained word2vec embeddings

from gensim.models import KeyedVectors
word2vec_vectors = KeyedVectors.load("/content/drive/MyDrive/Colab Notebooks/dementia/English//Pitt/word2vec_embeddings/word2vec.wordvectors", mmap='r')