"""
Calculate module
"""

def calculate(data):
    def sign(a, b):
        if a[0] != "-" and b[0] != "-":
            return a, b, 1
        elif a[0] == "-" and b[0] != "-":
            a = a[1:]
            return a, b, 2
        elif a[0] != "-" and b[0] == "-":
            b = b[1:]
            return a, b, 3
        else:
            a = a[1:]
            b = b[1:]
            return a, b, 4

    def whoisbigger(a, b):
        i = 0
        while i < len(a) - 1 and a[i] == b[i] or a[i] == "," or b[i] == ",":
            i += 1
        if symtonum(a[i]) > symtonum(b[i]):
            return 1
        elif symtonum(a[i]) < symtonum(b[i]):
            return 2
        else:
            return 3
    
    def beautynum(rez):
        while rez[0] == '0' and len(rez) != 1:
            rez = rez[1:]
        if rez[0] == "-":
            while rez[1] == '0' and len(rez) != 2:
                rez = '-' + rez[2:]
        if rez[:2] == '-0' and len(rez) == 2:
            rez = '0'
        if rez.find(',') != -1 and rez[-1] == '0':
            while rez[-1] == '0':
                rez = rez[:-1]
        if rez[-1] == ',':
            rez = rez[:-1]
        return rez
        
    def symtonum(g):
        numbers = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        return numbers.find(g)

    def numtosym(u):
        numbers = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        return numbers[u]

    def fill(a, b):
        if a.find(',') != -1 and b.find(',') != -1:
            p1 = len(a[:a.find(',')])
            r1 = len(a[a.find(',')+1:])
            p2 = len(b[:b.find(',')])
            r2 = len(b[b.find(',')+1:])
        elif a.find(',') == -1 or b.find(',') == -1:
            if a.find(',') == -1 and b.find(',') != -1:
                p1, p2 = len(a), len(b[:b.find(',')])
                r1, r2 = -1, len(b[b.find(',')+1:])
            elif b.find(',') == -1 and a.find(',')!=-1:
                p2, p1 = len(b), len(a[:a.find(',')])
                r2, r1 = -1, len(a[a.find(',')+1:])
            else:
                p1, p2 = len(a), len(b)
                r1, r2 = 0, 0
        if p1 == p2:
            a = '0' + a
            b = '0' + b
        elif p1 > p2:
            b = '0' * (p1 - p2 + 1) + b
            a = '0' + a
        elif p1 < p2:
            a = '0' * (p2 - p1 + 1) + a
            b = '0' + b
        if r1 > r2:
            b = b + '0' * (r1 - r2)
        else:
            a = a + '0' * (r2 - r1)
        return a, b
  
    def addition(a,b):
        f = 0
        res = ''
        for i in range(len(b) - 1, -1, -1):
            if a[i] != ',' and b[i] != ',':
                n = symtonum(a[i]) + symtonum(b[i]) + f
                if n >= c:
                    f = 1 
                    n -= c
                else:
                    f = 0
                res += str(numtosym(n)) 
            else:
                res += ','
        res = res[::-1]
        return res
    
    def subtraction(a,b):
        if whoisbigger(a, b) == 3:
            return '0'
        elif whoisbigger(a, b) == 1:
            f = 0
            res = ''
            for i in range(len(a)-1, -1, -1):
                if a[i] != ',' and b[i] != ',':
                    t = symtonum(a[i]) - symtonum(b[i]) - f
                    if t < 0:
                        f = 1
                        t += c
                    else:
                        f = 0
                    res += str(numtosym(t))
                else:
                    res += ','
        else:
            f = 0
            res = ''
            for i in range(len(a) - 1, -1, -1):
                if a[i] != ',' and b[i] != ',':
                    t = symtonum(b[i]) - symtonum(a[i]) - f
                    if t < 0:
                        f = 1
                        t += c
                    else:
                        f = 0
                    res += str(numtosym(t))
                else:
                    res += ','
            res= "-" + res
        res = res[::-1]
        return res

    c = int(data['dig'])
    a = data['num1'].replace('.', ',').upper()
    b = data['num2'].replace('.', ',').upper()
    d = data['action']
    a, b, s = sign(a, b)
    a, b = fill(a, b)
    if d == "+":
        if s == 1:
            res = addition(a,b)
        elif s == 2:
            res = subtraction(b,a)
        elif s == 3:
            res = subtraction(a,b)
        else:
            res = addition(a,b)
            res = "-" + res 
    elif d == "-":
        if s == 1:
            res = subtraction(a,b)
        elif s == 2:
            res = addition(a,b)
            res = "-" + res 
        elif s == 3:
            res = addition(a,b)
        else:
            res = subtraction(b,a)
    res = beautynum(res)
    return res
