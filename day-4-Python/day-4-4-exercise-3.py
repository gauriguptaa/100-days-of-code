row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = int(input("Where do you want to put the treasure? "))
horizontal_column = position % 10
vertical_column = int(position /10)
map[horizontal_column-1][vertical_column-1]='X'
print(f"{row1}\n{row2}\n{row3}")
