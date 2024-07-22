def decorator(function_defines_decorator):
    def dataWrapper(*args, **kwargs):
        print("Before the function")
        result = function_defines_decorator(*args, **kwargs)
        print("After function")
        return result
        return dataWrapper
    
    @decorator
    def my_function():
        print("Hello World!")