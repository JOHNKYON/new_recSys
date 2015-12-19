# -*- coding: utf-8 -*-

from __future__ import absolute_import

import codecs
import segment
import pg

output_file = codecs.open("data/seg_data1.txt", 'wb', encoding='utf-8')
pg.pg_init()

# print segment.seg(pg.get_edu())
bias = 1000
counter = 0
raw = '1'
while len(raw) != 0:
    raw = pg.get_edu(bias, counter)
    for mlist in segment.seg(raw):
        for ele in mlist:
            for x in ele:
                output_file.write(x+' ')
            output_file.write('\t')
        output_file.write('\n')
    counter += 1

'''raw = pg.get_edu(bias, counter)
for mlist in segment.seg(raw):
    for ele in mlist:
        for x in ele:
            output_file.write(x+' ')
        output_file.write('\t||\t')
    output_file.write('\n')'''

output_file.close()


# [[map(lambda x: output_file.write(x), ele) for ele in mlist] for mlist in segment.seg(pg.get_edu())]
# output_file.write(segment.seg(pg.get_edu()))
