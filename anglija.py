def realcode(num, d1, d2):
    a = []
    for n in range(d1, d2+1):
        if n != 0:
            if num % n == 0:
                a.append(n)

    return a

def dio():
    print('This is THE ULTIMATE DEVIDER 9000')
    print('Please write in the number that you want to check for deviders')
    try:
        num = int(input())
        print("if you don't care about range, just write 0 and 0")
        d = [int(input('Please write in the starting number of the range of answers you want to see')), int(input('Please write in the ending number of the range of answers you want to see'))]
    except:
        print('ERROR WRONG NUMBER INPUT')
    if d[0] == 0 and d[1] == 0:
        print(realcode(num, -num, num))
    else:
        print(realcode(num, d[0], d[1]))

dio()
