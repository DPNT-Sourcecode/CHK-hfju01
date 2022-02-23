# noinspection PyUnusedLocal
# friend_name = unicode string
def hello(friend_name):
    """
    Return a string
    - param[0] = a String. Ignore for now.
    - @return = a String containing a message
    """
    if not isinstance(friend_name, str):
        return "Try again"

    response = "Hello, " + friend_name + "!"
    return response



    


