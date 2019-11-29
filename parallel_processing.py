import sys
from datetime import datetime

start = datetime.now()

range_start = int(sys.argv[1])
range_end = int(sys.argv[2])

for i in range(range_start, range_end+1):
    if i%10**7==0:
        print(' %.0f%%'% ((i-range_start)/(range_end-range_start)*100))

print('%s-%s took %.0f seconds'%(range_start, range_end, (datetime.now()-start).total_seconds()))
