
if __name__ == '__main__':
    # Adding the numbers using list comprehension
    old_list = [1, 2, 3]
    new_list = [num + 1 for num in old_list]
    print(new_list)

    # OUTPUT :- [2, 3, 4]

    # Looping through a string in list
    name = "Gauri"
    str_list = [letter for letter in name]
    print(str_list)

    # OUTPUT :- ['G', 'a', 'u', 'r', 'i']

    # Looping through a range and double the integer

    double_int_list = [ 2 *i for i in range(0, 5)]
    print(double_int_list)

    # OUTPUT :- [0, 2, 4, 6, 8]

    #  Print the names with length 4 or less then 4 and print them in uppercase

    name_list = ['Alex', 'Beth', 'Shamali', 'Gauri', 'Tina', 'Ira']
    short_name_list = [name.upper() for name in name_list if len(name) <= 4]
    print(short_name_list)

    # OUTPUT :- ['ALEX', 'BETH', 'TINA', 'IRA']
