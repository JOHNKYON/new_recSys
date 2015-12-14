# -*- coding: utf-8 -*-


import segment
import pg
import codecs
import topic_model

output_file = codecs.open("data/doc_vec.txt", 'wb', encoding='utf-8')
pg.pg_init()


doc_vec = [topic_model._build_corpus(x) for x in segment.seg(pg.get_edu())]

for people in topic_model.corpus:
    for attr in people:
        for vec in attr:
            output_file.write(str(vec))
            output_file.write(' ')
        output_file.write('\t')
    output_file.write('\n')

'''for ele in topic_model.dictionary.token2id:
    output_file.write(ele+' ')'''

output_file.close()
