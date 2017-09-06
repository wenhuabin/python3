from multiprocessing import Pool, Process
import os, time, random
import subprocess

#print('Process (%s) start...' % os.getpid())
#
#pid = os.fork()
#if pid == 0:
#    print('I am child process (%s) and my parent is %s.' %(os.getpid(), pid))
#else:
#    print('I (%s) just create a child process (%s).' %(os.getpid(), pid))

def run_proc(name):
    print('Run child process %s (%s).' % (name, os.getpid()))

def long_time_task(name):
    print('Run task %s (%s)...' %(name, os.getpid()))
    start = time.time()
    time.sleep(random.random()*3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' %(name, (end-start)))


def run_process():
    print('Parent process (%s).' % os.getpid())
    p = Process(target=run_proc, args=('test',))
    print('child process will start.')
    p.start()
    p.join()
    print('child process end.')

def run_pool():
    print('Parent process (%s).' % os.getpid())
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args=(i, ))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('all process done.')

def run_subproc():
    print('$ nslookup www.python.org')
    r = subprocess.call(['nslookup', 'www.python.org'])
    print('Exit code:', r)

def run_subproc_com():
    print('$ nslookup')
    p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, 
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE)
    output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
    print(output.decode('utf-8'))
    print('Exit code:', p.returncode)

if __name__ == '__main__':
    #run_pool()
    #run_subproc()
    run_subproc_com()

