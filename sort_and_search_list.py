
"""
program: sort_and_search_list
Author: Ondrea Li
Last date modfied: 06/20/20
The purpose of this program is to
"""
animal_list = ['horse', 'goat', 'llama', 'chicken','cow', 'deer']
def search_list(animal):
    """
    Use reST style
    :param animal: represents user input for animal search
    :return: returns the index of the object
    :raises keyError: raises an exception
    """
    try:
        x = animal_list.index(animal)
        return x
    except ValueError as err:
        print("-1", err)
        raise ValueError

def sort_list():
    """
    Use reST style
    :param enter_number: represents user input for number
    :return: returns a string
    :raises keyError: raises an exception
    """
    animal_list.sort()
    #does not need a return statement because the sort already returns to the sort list

if __name__ == '__main__':
    search_animal = search_list('llama')
    print(search_animal)

    sort_list()
    print(animal_list)

