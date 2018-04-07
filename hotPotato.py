from pythonds.basic.queue import Queue

def hotPotato(namelist, num):
    sim_queue = Queue()
    for name in namelist:
        sim_queue.enqueue(name)

    while sim_queue.size() > 1 :
        for i in range(num):
            sim_queue.enqueue(sim_queue.dequeue())
        sim_queue.dequeue()
    return sim_queue.dequeue()

print(hotPotato(['bill', 'david', 'susan', 'jane', 'kent', 'brad'], 7))
