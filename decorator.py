

def dec(func):
    def wraper():
        print("start")
        func()
        print("stop")
    return wraper

@dec
def helo():
    print("Helloworld")

helo()
#
# # Step 1: Define a simple decorator
# def my_decorator(func):
#     def wrapper():
#         print("Before the function runs")
#         func()
#         print("After the function runs")
#     return wrapper
#
# # Step 2: Apply the decorator to a function
# @my_decorator
# def say_hello():
#     print("Hello!")
#
# # Step 3: Call the decorated function
# say_hello()
