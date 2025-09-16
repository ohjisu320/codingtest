changes = [500, 100, 50, 10, 5, 1]
price = 1000 - int(input())
cnt = 0

for change in changes :
    cnt += price // change
    price = price % change

print(cnt)