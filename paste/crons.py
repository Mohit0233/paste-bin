# import threading
# import time
#
# from asgiref.sync import async_to_sync
#
#
# def print_square(nums):
#     while True:
#         time.sleep(1)
#         print("hello")
#
#
#
# def this_is_me_cron():
#     t1 = threading.Thread(target=print_square, args=(10,))
#
#     t1.start()
#     t1.join()
#     print("done")