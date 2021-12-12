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
            
            print(sum(dalitaji(num, 0, num)))
        else:
            if d[0] < d[1]:
                t = 0
                seen = []
                for n in range(d[0], d[1]+1):
                    for n1 in dalitaji(n, 0, d[1]):
                        if not n1 in seen:
                            t+= n1
                            seen.append(n1)
                print(t)
                print(seen)
            else:
                t = 0
                seen = []
                for n in range(d[1], d[0]+1):
                    for n1 in dalitaji(n, 0, d[1]):
                        if not n1 in seen:
                            t+= n1
                            seen.append(n1)
                print(t)
                print(seen)
    except:
        print('ERROR WRONG NUMBER INPUT')
    

dio()
