"""
program:sort_and_search_arry
Author: Ondrea Li
Last date modfied: 06/21/20
The purpose of this program is to write two functions
that sort and search arrrays
print index and sorted list
"""
import array as arr
number_list = [1.2, 2.3, 3.4, 4.6, 5.1, 6.9, 7.2]
a = arr.array('d', [1.2, 2.3, 3.4, 4.6, 5.1, 6.9, 7.2])
def search_array(number):
    """
    Use reST style
    :param vegetable represents the user input of number
    :return: return the index of the object in the list
    :raises keyError: raises an exception
    """
    #will return the index of the object in the list
    #or a -1 if the item is not found

    try:
        x = a.index(number)
        return x
    except ValueError as err:
        print('-1', err)
        raise ValueError

def sort_array():
    """
    Use reST style
    :return: no return key
    :raise keyError: raises an exception
    """
    number_list.sort()
    #no return because number_list.sort() returns the list that is sorted out


if __name__ == '__main__':
    search_number = search_array(6.9)
    print(search_number)

    sort_array()
    print(number_list)
