# Take a look inside file1.txt and file2.txt. They each contain a bunch of numbers, each number on a new line.

#  You are going to create a list called result which contains the numbers that are common in both files.
import pandas
if __name__ == '__main__':
    new_list = [int(num) for num in open("file1.txt") if num in open("file2.txt")]
    print(new_list)
