import decorator


@decorator.decorator
def execute_twice_decorator(function):
    """
    This decorator gets a function and executes it twice.
    :param function: the function we want to execute twice.
    :return: the function we passed from the main. In the first time
    it will just call it, but in the second execution it will return it.
    """
    function()
    return function()


@execute_twice_decorator
def print_hello() -> None:
    """
    This function prints "Hello!" to the terminal.
    """
    print("Hello!")


if __name__ == '__main__':
    print_hello()
