
from azure.storage.queue import QueueService, QueueMessageFormat
import base64
import time
import threading
queue = QueueService(connection_string="")
queue.encode_function = QueueMessageFormat.text_base64encode

def send():
    for k in range(1):
        for i in range(1, 16):
            queue.put_message("xxx", "https://cowstoragecloud.blob.core.windows.net/cow-images/%s.jpg"%(i))
            print("epoch: %s and send %s message"%(k, i))
        #time.sleep()

threadpool = []
for i in range(1):
    threadpool.append(threading.Thread(target=send))
    threadpool[i].start()

for i in range(1):
    threadpool[i].join()
