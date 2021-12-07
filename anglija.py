def dalitaji(num, d1, d2):
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
        if d[0] == 0 and d[1] == 0:
            if num > 0:
                print(dalitaji(num, -num, num))
            else:
                print(dalitaji(num, num, -num))
        else:
            if d[0] < d[1]:
                print(dalitaji(num, d[0], d[1]))
            else:
                print(dalitaji(num, d[1], d[0]))
    except:
        print('ERROR WRONG NUMBER INPUT')
    

dio()
