# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import unicode_literals


import gensim
import psycopg2
import codecs
import re
import jieba
import data
import nltk


def __clean_content(raw):
    """
    文本清洗
    :param raw:
    :return:
    """
    # 过滤空白字符
    # print raw
    blank_re = re.compile(r"\s+")
    temp_raw = map(lambda x: x[1:], raw)
    # print temp_raw
    texts_raw = [map(lambda x: blank_re.split(x), ele) for ele in temp_raw]
    # return texts_raw

    # 分词
    texts_splited = [[reduce(lambda x, y: x + jieba.lcut(y), text, []) for text in temp_list] for temp_list in texts_raw]

    # 过滤停用词
    texts_filtered = [[[word for word in text if word not in data.stopwords] for text in temp_filt] for temp_filt in texts_splited]

    # 过滤低频词
    # all_words = sum(texts_filtered, [])
    # words_once = {word for word in set(all_words) if all_words.count(word) == 1}
    # texts = [[word for word in text if word not in words_once] for text in texts_filtered]
    return texts_filtered
    # return texts_raw


# 测试分词
def seg(raw):
    """
    返回的结果是一个三层list,第一层为单条记录的list，第二层为记录中的属性的list，第三层为每个属性的分词结果的list
    :rtype : object
    """
    return __clean_content(raw)
