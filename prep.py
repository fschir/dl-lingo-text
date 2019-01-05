import multiprocessing
import os, json, requests
import re
import nltk
import gensim.models.word2vec as w2v
import sklearn.manifold
import pandas as pd
import seaborn as sns
import tensorflow as tf
from tensorflow.contrib.tensorboard.plugins import projector

nltk.download("punkt")
nltk.download("stopwords")

sentences = []
raw_sentences = []


def sentence_to_wordlist(raw):
    clean = re.sub("[a-zA-Z]", " ", raw)
    words = clean.split()
    return map(lambda x: x.lower(), words)


# KJV Bible
with open('corpus/kjv.txt') as corpus_raw:
    corpus_raw.read()

for raw_sentence in raw_sentences:
    if len(raw_sentence) > 0:
        sentences.append(sentence_to_wordlist(raw_sentence))

