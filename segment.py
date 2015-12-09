# -*- coding: utf-8 -*-

from __future__ import absolute_import

import gensim
import psycopg2
import codecs
import re
import jieba
import utf8


def __clean_content(raw):
    """
    文本清洗
    :param raw:
    :return:
    """
    # 过滤空白字符
    blank_re = re.compile(r"\s+")
    texts_raw = [blank_re.split(ele["description"]) for ele in raw]

    # 分词
    texts_splited = [reduce(lambda x, y: x + jieba.lcut(y), text, []) for text in texts_raw]

    # 过滤停用词
    texts_filtered = [[word for word in text if word not in utf8.stopwords] for text in texts_splited]

    # 过滤低频词
    # all_words = sum(texts_filtered, [])
    # words_once = {word for word in set(all_words) if all_words.count(word) == 1}
    # texts = [[word for word in text if word not in words_once] for text in texts_filtered]
    return texts_filtered
