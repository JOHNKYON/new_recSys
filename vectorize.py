# -*- coding: utf-8 -*-


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

raw = map(lambda x: x[0] + x[1], segment.seg(pg.get_edu()))

topic_model.build_lsi(raw)


'''topic_model._build_corpus(raw)

tfidf = topic_model._build_tfidf()
corpus_tfidf = tfidf[topic_model.corpus]

for ele in corpus_tfidf:
    print ele
'''

'''for ele in topic_model.dictionary.token2id:
    output_file.write(ele+' ')'''

test_sample = topic_model.dictionary.doc2bow(raw[0])
print test_sample
print topic_model.model[test_sample]


output_file.close()
