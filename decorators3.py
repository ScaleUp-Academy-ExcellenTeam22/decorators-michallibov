import decorator


@decorator.decorator
def execute_twice_decorator(function: callable, *args):
    """
    This decorator gets a function and executes it twice.
    :param function: the function we want to execute twice.
    :return: the function we passed from the main. In the first time
    it will just call it, but in the second execution it will return it.
    """
    function(*args)
    return function(*args)


@execute_twice_decorator
def print_hello(name=None) -> None:
    """
    This function prints "Hello!" to the terminal.
    """
    print("Hello " + name + "!") if name else print("Hello!")


if __name__ == '__main__':
    print_hello("name")
