"""
program:File_IO_using_Tuples
Author: Ondrea Li
Last date modfied: 06/21/20
The purpose of this program is o tie together unrelated tuple
and arbitrary argument list to perform file input and output
"""
import os as os

def write_to_file(*args):
    """
    Use reST style
    :param args: for arbitrary input for file
    """
    #Open the file for appending (name your file 'student_info.txt')
    try:
        with open('student_info.txt', 'a') as f:
        #Write the tuple on one line (include any newline characters necessary)
            f.write(str(args) + "\n")
        #close the file
            f.close()
    except IOError:
        print("Error, cannot open file")

def get_student_info():
    """
    Use reST style
    :param student_name: input for name
    :parm score_list: input for list of scores
    :param enter_test_score: to get score input
    :raise ValueError: raises an exception
    """
    student_name = input("Print your name:")
    score_list = []
    enter_test_score = 0
    sentinel_value = -99
    while enter_test_score != sentinel_value:
        try:
            enter_test_score = int(input('Enter test score between 1 and 100, -99 to stop:'))
            if 0<= enter_test_score<= 100  and enter_test_score != -99:
                score_list.append(enter_test_score)

            elif enter_test_score > 100 or enter_test_score < 1 and enter_test_score != -99:
                print("Not in range!")
        except ValueError:
            print("ValueError! Needs to be a number")
            raise ValueError
#Stores the information (name and scores) in a tuple
#Calls the function write_to_file() sending the tuple to be written to the end of the file

    store_info = tuple(score_list)
    write_to_file(student_name, store_info)

def read_from_file():
    """
    Use reST style
    :param file_dir: direct file
    :parm file_name: name of file directed
    :return: string with average
    """
    #Reads a file line by line
    # Prints each line to the console
    file_dir = os.path.dirname(__file__)
    file_name = "student_info.txt"
    f = open(os.path.join(file_dir, file_name), "r")
    line = f.read(300)
    print(line)
    f.close()


if __name__ == '__main__':
    # Call the get_student_info() for at least 4 different students.
    # Call read_from_file()
    # Include input('Press any key to end')
    get_student_info()
    read_from_file()
    get_student_info()
    read_from_file()
    get_student_info()
    read_from_file()
    get_student_info()
    read_from_file()
    print(input("Press any key to end"))
