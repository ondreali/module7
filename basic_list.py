"""
program: basic_list
Author: Ondrea Li
Last date modfied: 06/20/20

The purpose of this program is to write the function to input
and print user input as a list.
"""

# this function will get one input and return it
def get_input():
    """
    Use reST style
    :param enter_number: represents user input for number
    :return: returns a string
    :raises keyError: raises an exception
    """
    enter_number = int(input("Enter a number:"))
    return enter_number
        #return a string

# this function will return a list of input
def make_list():
    """
    Use reST style
    :param x: this calls function get_input as integer
    :return: retuns a list
    :raises keyError: raises an exception
    """
    list = []
    #declare a list variable
    #call get input,
    try:
        for n in range(0,3):
            x = int(get_input())
            list.append(x)
        return list
    except ValueError as err:
        print("Value Error!", err)
        raise ValueError


if __name__ == '__main__':
    a = make_list()
    print(a)

