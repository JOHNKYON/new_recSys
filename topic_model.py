# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals
import gensim
import conf

dictionary = None
corpus = None
model = None
index = None


def _build_corpus(doc_col):
    """
    建立词袋和文档向量
    :param doc_col:
    :return:
    """
    global dictionary, corpus
    # 抽取词袋
    dictionary = gensim.corpora.Dictionary(doc_col)
    # 建立用词频表示的文档向量
    corpus = [dictionary.doc2bow(text) for text in doc_col]


def _build_tfidf():
    """
    建立TF-IDF模型
    :return:
    """
    tfidf = gensim.models.TfidfModel(corpus)
    return tfidf


def build_vsm(doc_col):
    """
    建立VSM模型
    :param doc_col:
    :return:
    """
    global model
    _build_corpus(doc_col)
    model = _build_vsm()
    # logger.log.info("vsm model has been generated.")


def _build_vsm():
    """
    建立VSM模型
    :return:
    """
    tfidf = _build_tfidf()
    global index
    # 建立相似度索引
    # index = gensim.similarities.MatrixSimilarity(tfidf[corpus])
    index = gensim.similarities.Similarity("vsm_index", tfidf[corpus], num_features=tfidf.num_docs,
                                           num_best=conf.SIM_DOC_TOTAL)
    return tfidf


def build_lsi(doc_col):
    """
    建立LSI模型
    :param doc_col:
    :return:
    """
    global model
    _build_corpus(doc_col)
    model = _build_lsi()
    # logger.log.info("lsi model was generated.")


def _build_lsi():
    """
    建立LSI模型
    :return:
    """
    tfidf = _build_tfidf()
    global index
    # 建立LSI模型
    lsi = gensim.models.LsiModel(tfidf[corpus], id2word=dictionary, num_topics=20)
    # 建立相似度索引
    index = gensim.similarities.MatrixSimilarity(lsi[corpus])
    # index = gensim.similarities.Similarity("lsi_index", lsi[corpus], num_features=lsi.num_topics)
    return lsi


def build_lda(doc_col):
    """
    建立LDA模型
    :param doc_col:
    :return:
    """
    global model
    _build_corpus(doc_col)
    model = _build_lda()
    # logger.log.info("lda model was generated.")


def _build_lda():
    """
    建立LDA模型
    :return:
    """
    global index
    # 建立LDA模型
    # lda = gensim.models.LdaModel(corpus, id2word=dictionary, num_topics=100, passes=30)
    lda = gensim.models.LdaMulticore(corpus, id2word=dictionary, num_topics=100, passes=30)
    # 建立相似度索引
    # index = gensim.similarities.MatrixSimilarity(lda[corpus])
    index = gensim.similarities.Similarity("lda_index", lda[corpus], num_features=lda.num_topics,
                                           num_best=conf.SIM_DOC_TOTAL)
    return lda
