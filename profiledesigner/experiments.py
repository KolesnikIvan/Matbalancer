import numpy as np
import random

# a = np.ndarray(random.randint(1,10)*10)
# b = np.arange(1,100,7)
# c = np.linspace(1,100,7)

# def f(i,j):
#     return (i+j) / 2

# d = np.fromfunction(f,(4, 3))

# N, n = 1101, 5
# def f2(i):
#     return i % n == 0

# comb =np.fromfunction(f2, (N,), dtype=int)

# npstr = np.dtype('f8')
# free = np.empty((3,7))


# if __name__ == "__main__":
#     # print(a)
#     print(d)
#     print(comb)

# import pika
# connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=49153, credentials=pika.credentials.Credentials()))
# channel = connection.channel()
# channel.queue_declare(queue="ivan1")
# channel.basic_publish(
#     exchange='',
#     routing_key='invan1',
#     body='hello from python',
# )
# connection.close()


#shoelace algorithm
#-------------------------------------------------------------------------
# import numpy as np

# dt = np.dtype([('x','float'),('y','float')])
# N = 10

# x = np.random.randint(-10,10,N)
# y = np.random.randint(-10,10,N)

# coord = np.array([(X, Y) for X,Y in zip(x,y)],dtype=dt)
#---------------------------------------------------------------------------

