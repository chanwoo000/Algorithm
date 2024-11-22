a = int(input())
remain = 1000-a
cnt = 0
while remain != 0:
     if remain - 500 >= 0:
        cnt+=1
        remain-=500
        continue
     elif remain - 100 >= 0:
         cnt += 1
         remain -= 100
         continue
     elif remain - 50 >= 0:
         cnt += 1
         remain -= 50
         continue
     elif remain - 10 >= 0:
         cnt += 1
         remain -= 10
         continue
     elif remain - 5 >= 0:
         cnt += 1
         remain -= 5
         continue
     elif remain - 1 >= 0:
         cnt += 1
         remain -= 1
         continue

print(cnt)
