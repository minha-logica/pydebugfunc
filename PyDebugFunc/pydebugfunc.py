from functools import wraps
def debug(input_function):
    '''A simple decorator to debug functions'''
    @wraps(input_function)
    def output_function(*args, **kwds):
        try:
            input_function(*args, **kwds)
        except Exception as error:
            name = input_function.__name__
            msg = f"Function error '{name}()': {error}"           
            print(msg)      
    return output_function
