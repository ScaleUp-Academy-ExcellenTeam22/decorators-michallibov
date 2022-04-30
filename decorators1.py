import functools


def factory(type_argument: type):
    """
    This is the factory function. It receives a type of an argument and calls two
    decorators that will call the function and check the given type.
    :param type_argument: a type that the function gets.
    :return: the result of the function (which is sent from the decorator and the wrapper)
    if the type is correct, or there will be a type exception if the type is wrong.
    """
    def decorator(function: callable):
        """
        This decorator calls the wrapper.
        :param function: the function we passed to the decorator (the function we want to run).
        :return: the result of the wrapper (which is the result of the function), or a type exception
        in case the type that the function received is wrong.
        """
        @functools.wraps(function)
        def wrapper(function_arguments: object):
            """
            The wrapper. It calls the function and checks if the type we sent to the function is
            correct or not. If it's not- it will raise a type exception.
            :param function_arguments: the argument that we sent to the function.
            :return: if the type we sent to the function is correct so it will return the result
            of the function, and if the type is wrong- it will raise a type exception.
            """
            if type(function_arguments) != type_argument:
                raise TypeError("Wrong type!")
            return function(function_arguments)
        return wrapper
    return decorator


@factory(int)
def is_number_positive(number) -> bool:
    """
    This function checks if the number we received is positive.
    :param number: the number we want to check if positive.
    :return: true if the number is positive, or false if the number is negative.
    """
    return number > 0


if __name__ == '__main__':
    is_number_positive("lol")
