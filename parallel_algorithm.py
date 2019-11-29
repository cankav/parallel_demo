THREAD_NUM=4
MAX=10**8
import multiprocessing

def f(tid, range_start, range_end):
    for i in range(range_start, range_end+1):
        if i%10**7==0:
            print('tid %s: %.0f%%'% (tid, (i-range_start)/(range_end-range_start)*100))

processes=[]
for i in range(THREAD_NUM):
    processes.append(
        multiprocessing.Process(
            target=f,
            args=(i, int(i*MAX/THREAD_NUM), int((i+1)*MAX/THREAD_NUM) )
        )
)

for p in processes:
    p.start()

for p in processes:
    p.join()

print('main thread done')
