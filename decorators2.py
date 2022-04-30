
def surprise_decorator(function):
    """
    This is the decorator that calls the wrapper which call the function that prints "Surprise".
    :param function: the function we want to call (in this case- surprise()).
    :return: the value of the wrapper which is the function that prints "Surprise".
    """
    def surprise_wrapper():
        """
        This wrapper calls (when returning) the function we passed which in this case is surprise().
        :return: the function which in this case is surprise().
        """
        return function()
    return surprise_wrapper


@surprise_decorator
def surprise() -> None:
    """
    This function prints "Surprise" to the terminal.
    """
    print("Surprise!")


if __name__ == '__main__':
    surprise()
