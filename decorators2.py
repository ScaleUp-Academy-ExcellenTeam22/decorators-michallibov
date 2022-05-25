from functools import wraps


def surprise_decorator(function):
    """
    This is the decorator that calls the wrapper which call the function that prints "Surprise".
    :param function: the function we want to call (in this case- surprise()).
    :return: the execution of the wrapper. The wrapper prints "Surprise!".
    """
    @wraps(function)
    def surprise_wrapper() -> None:
        """
        This wrapper prints "Surprise!"
        """
        print("Surprise!")
    return surprise_wrapper


@surprise_decorator
def surprise() -> None:
    """
    This function is not reachable.
    """
    print("This function is not reachable.")


if __name__ == '__main__':
    surprise()
