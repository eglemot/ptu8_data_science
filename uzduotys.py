# def ieskom():
#     with open("gen_failui/generatoriui.txt", "r") as failas:
#         while True:
#             for eilute in failas:
#                 yield eilute

# bandom = ieskom()

# for rezultatas in bandom:
#     print(rezultatas)


# from time import time
# def performance(fn):
#     def wrapper(*args, **kwargs):
#         t1 = time()
#         result = fn(*args, **kwargs)
#         t2 = time()
#         diff = t2 - t1
#         # print(f"It took {diff}")
#         return result, diff
#     return wrapper

# import requests  
# from time import time 

# start_time = time()  
# r = requests.get('http://www.cnn.com')  
# print(r.status_code)  # spausdiname status code (200 = OK, 404 = Not Found, ir t.t. galima pasiguglinti http status codes)
# end_time = time()  
# print(end_time - start_time)  # atspausdiname laiką, per kurį gaovme atsakymą