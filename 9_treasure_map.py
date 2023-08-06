# 

row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]

map = [row1, row2, row3]
print(f'{row1}\n{row2}\n{row3}')
print('Where do you want to put the treasure?')
position = (input('Enter two digits, the first for the horizontal column and the second for the vertical: '))

horizontal = int(position[0])
vertical = int(position[1])

selected_row = map[vertical -1]
selected_row[horizontal -1] = ' X  '

print(f'{row1}\n{row2}\n{row3}')
