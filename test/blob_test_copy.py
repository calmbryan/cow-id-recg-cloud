from azure.storage.blob import BlockBlobService, ContentSettings
from concurrent import futures
from concurrent.futures import ThreadPoolExecutor
import time
import cv2 as cv
import os
import hashlib
import numpy as np



account_name = "cowstoragecloud"
account_key = "wySJgs4UvJqhZUjubvX7lgSiU6/k5qSxUbee2K5hzVPnUq7HsI358u7wzVLQv50b2Kcy66oeIUBB8qESg2C4Tg=="

block_blob_service = BlockBlobService(
    account_name=account_name,
    account_key=account_key
)

account_name_2 = "cowstoragecloud2"
account_key_2 = "/KyJKsNRXaqKm36AAIBKAUl3c7MlhqPGQ827gVLOJ3JN9Fly4XbEV16Kgw6fwBN9vVEp006zSe9yjp9AQ6KFjw=="

block_blob_service_2 = BlockBlobService(
    account_name=account_name_2,
    account_key=account_key_2
)

account_name_3 = "cseastus100320004340a6cd"
account_key_3 = "jiupwk/mcgmaqrO6MyzwWiOlPedVA1YWzGEI3E4vG5qJN7AuvrXei+dcoREWMENvaa8r/gXlFQX3JQU+1pzVAw=="

block_blob_service_3 = BlockBlobService(
    account_name=account_name_3,
    account_key=account_key_3
)

account_name_4 = "storageaccountcowkubadf"
account_key_4 = "zk506xxbZ6NtEPBeCc226+vdnWG//RGTjd1Dq6dc2wgKDY83wGpicQvgr/SGtBXfrDMk7U7zz4dqWXvC3Kf2KQ=="

block_blob_service_4 = BlockBlobService(
    account_name=account_name_4,
    account_key=account_key_4
)

def process_single_file(filename,  dirname="", index=""):

    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")


    print(f'{dirname}/{filename}')
    push_start = time.time()
    # hashVal = hashlib.sha256(filename.encode()) 
    account_id = (index)%4 + 1
    if account_id == 1:
        block_blob_service.create_blob_from_path(f'test1',
                                                f'{filename + "x"}',
                                                f'{dirname}/{filename}',
                                                content_settings=ContentSettings(content_type='image/jpeg'))
                                                
        push_end = time.time()
        print("push blob time: {} sec".format(push_end-push_start))
    elif account_id == 2:
        block_blob_service_2.create_blob_from_path(f'test1',
                                                f'{filename + "x"}',
                                                f'{dirname}/{filename}',
                                                content_settings=ContentSettings(content_type='image/jpeg'))
                                                
        push_end = time.time()
        print("push blob time: {} sec".format(push_end-push_start))
    elif account_id == 3:
        block_blob_service_3.create_blob_from_path(f'test1',
                                                f'{filename + "x"}',
                                                f'{dirname}/{filename}',
                                                content_settings=ContentSettings(content_type='image/jpeg'))
                                                
        push_end = time.time()
        print("push blob time: {} sec".format(push_end-push_start))
    elif account_id == 4:
        block_blob_service_4.create_blob_from_path(f'test1',
                                                f'{filename + "x"}',
                                                f'{dirname}/{filename}',
                                                content_settings=ContentSettings(content_type='image/jpeg'))
                                                
        push_end = time.time()
        print("push blob time: {} sec".format(push_end-push_start))


def upload(path_output_dir):

    count = 1

    with ThreadPoolExecutor(10) as executor:
        jobs = []
        results_done = []

        files = os.listdir(path_output_dir)
        for i, f in enumerate(files):
            # image = image.tobytes()
            kw = {"filename": f, "dirname":path_output_dir, "index":i}
            jobs.append(executor.submit(process_single_file, **kw))
            count += 1
        
    for job in futures.as_completed(jobs):
            # Read result from future
            result_done = job.result()
            # Append to the list of results
            results_done.append(result_done)


tik = time.time()
upload("./sample_image")
tok = time.time()
print("Running time: ", tok-tik)