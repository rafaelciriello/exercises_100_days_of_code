"""prompts the user to provide a two-digit coordinate and marks an "X" 
at a given position."""

# prints the map with 3 rows and 3 columns
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
treasure_map = [row1, row2, row3]
print(f'{row1}\n{row2}\n{row3}')

# asks the user for coordinates
print('Where do you want to put the treasure?')
position = (input('Enter two digits, the first for column and the second for the row: '))

# transform the received string into coordinates and apply to the map
horizontal = int(position[0])
vertical = int(position[1])
selected_row = treasure_map[vertical -1]
selected_row[horizontal -1] = ' X  '

# print the map with the marking at the location selected by the user
print(f'{row1}\n{row2}\n{row3}')
