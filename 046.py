from time import sleep

for time in range(10, -1, -1):
    print(f'{time}')
    sleep(1)
print('BOOM!')