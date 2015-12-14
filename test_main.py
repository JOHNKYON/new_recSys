# -*- coding: utf-8 -*-

from __future__ import absolute_import

import codecs
import segment
import pg

output_file = codecs.open("data/seg_data.txt", 'wb', encoding='utf-8')
pg.pg_init()

# print segment.seg(pg.get_edu())
for mlist in segment.seg(pg.get_edu()):
    for ele in mlist:
        for x in ele:
            output_file.write(x+' ')
        output_file.write('\t')
    output_file.write('\n')

output_file.close()


# [[map(lambda x: output_file.write(x), ele) for ele in mlist] for mlist in segment.seg(pg.get_edu())]
# output_file.write(segment.seg(pg.get_edu()))
