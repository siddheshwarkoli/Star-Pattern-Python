row = int(input("Enter a row"))
for i in range(1, row+1):
    for j in range(i-1):
        print(' ', end='')
    for j in range(2*(row-i)+1):
        print('*', end='')
    print()