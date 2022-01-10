import multiprocessing,random
import datetime,time

def process_demo(sec):
    time.sleep(sec)
    print('waiting {} seconds, Current time is {}'.format(sec,time.strftime("%H:%M:%S", time.localtime())))
    
    
if __name__ == "__main__":
    p1 = multiprocessing.Process(target=process_demo, args=(random.randint(0,5),))
    p2 = multiprocessing.Process(target=process_demo, args=(random.randint(0,5),))
    p3 = multiprocessing.Process(target=process_demo, args=(random.randint(0,5),))
    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()
    
    print('Done!')