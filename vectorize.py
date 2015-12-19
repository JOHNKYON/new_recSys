# -*- coding: utf-8 -*-

from __future__ import absolute_import

import segment
import pg
import codecs
import topic_model
import gensim

output_file = codecs.open("data/doc_vec.txt", 'wb', encoding='utf-8')
pg.pg_init()

# 将教育经历的两个属性合并
'''for ele in segment.seg(pg.get_edu()):
    print len(ele)'''
# 测试
'''for mlist in segment.seg(pg.get_edu()):
    for ele in mlist:
        for x in ele:
            output_file.write(x+' ')
        output_file.write('\t||\t')
    output_file.write('\n')
'''
raw = list()
people = pg.get_edu(0, 0)
raw = map(lambda x: x[0] + x[1], segment.seg(people))

topic_model.build_lsi(raw)


'''topic_model._build_corpus(raw)

tfidf = topic_model._build_tfidf()
corpus_tfidf = tfidf[topic_model.corpus]

for ele in corpus_tfidf:
    print ele
'''

'''for ele in topic_model.dictionary.token2id:
    output_file.write(ele+' ')'''

# print raw[0]
# raw_edu = map(lambda x: x[0:2], raw)
for ele in raw:
    test_sample = topic_model.dictionary.doc2bow(ele)
    # print test_sample
    query_lsi = topic_model.model[test_sample]
    # print query_lsi
    sims = topic_model.index[query_lsi]
    sorted_sims = sorted(list(enumerate(sims)), key=lambda item: -item[1])
    for x in sorted_sims:
        if x[1] > 0.9:
            for attr in people[x[0]]:
                if type(attr) is long:
                    output_file.write(str(attr))
                else:
                    attr = attr.decode("utf-8")
                    output_file.write(attr+' ')
                output_file.write('\t')
            output_file.write('\n')
        else:
            output_file.write('\n\n')
            break


output_file.close()
