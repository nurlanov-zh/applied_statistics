from zlib import crc32
import numpy as np

if __name__=='__main__':
    inp = input('enter e-mails in comma-separated-format ("aaaa@bbb,ccc@ddd")\n')
    mails = inp.lower().strip().split(',')
    if len(mails)>3:
        print ('Bad number of e-mails')
        exit(1)
    to_hash = ' '.join(sorted([s.strip().split('@')[0] for s in mails]))
    print ('generating hash for ', [to_hash])
    h = crc32(to_hash.encode('utf-8'))
    seed = h%(2**32-1)
    rs = np.random.RandomState(seed)
    task1 = rs.randint(low=1, high=4)
    task2 = rs.randint(low=4, high=7)
    task3 = rs.randint(low=7, high=10)
    print ('Your tasks are', task1, task2, task3)
