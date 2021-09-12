#  square the number using list comprehension

if __name__ == '__main__':
    numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    squared_list = [num*num for num in numbers]
    print(squared_list)
