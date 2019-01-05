import params
import prep

import gensim.models.word2vec as w2v
import os

model2vec = w2v.Word2Vec(
    sg=1,
    seed=params.seed,
    workers=params.num_workers,
    size=params.num_features,
    min_count=params.min_word_count,
    window=params.context_size,
    sample=params.downsampling
)

model2vec.build_vocab(prep.sentences)
model2vec.train(prep.sentences, total_examples=model2vec.corpus_count, epochs=100)

if not os.path.exists(os.path.join("trained", 'sample')):
    os.makedirs(os.path.join("trained", 'sample'))

model2vec.save(os.path.join("trained", 'sample', ".w2v"))

model2vec.most_similar("lord")
