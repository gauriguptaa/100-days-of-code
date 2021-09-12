#  Filter Even numbers using list comprehension

if __name__ == '__main__':
    numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    even_list = [num for num in numbers if num % 2 == 0]
    print(even_list)

    # OUTPUT :- [2, 8, 34]
