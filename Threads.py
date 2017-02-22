__author__ = 'PrasantJillella'
import threading

class prasantmessenger(threading.Thread):

    def run(self):
        for _ in range(10):
            print(threading.currentThread().getName())
        ''' def prasant(self):  print("------------Hi i am prasant-------------")'''
thread1=prasantmessenger(name="sending a message")
thread2=prasantmessenger(name="receiving a message")
thread2.start()
thread1.start()
'''thread1.prasant() thread2.prasant()'''
