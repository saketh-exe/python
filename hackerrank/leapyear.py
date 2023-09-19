def is_leap(year):
    leap = False
    a = year%4
    b = year%100
    c = year%400
    if a==0 and b!=0:
        leap = True
    elif a==0 and b==0 and c ==0:
        leap=True
    return leap

year = int(input())
print(is_leap(year))