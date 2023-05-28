from numsys import rebase


def calculate(data):
    def sign(a, b):
        if a[0] != '-' and b[0] != '-':
            return a, b, 1
        elif a[0] == '-' and b[0] != '-':
            a = a[1:]
            return a, b, 2
        elif a[0] != '-' and b[0] == '-':
            b = b[1:]
            return a, b, 3
        else:
            a = a[1:]
            b = b[1:]
            return a, b, 4

    def whoisbigger(a, b):
        i = 0
        while i < len(a) - 1 and a[i] == b[i] or a[i] == '.' or b[i] == '.':
            i += 1
        if symtonum(a[i]) > symtonum(b[i]):
            return 1
        elif symtonum(a[i]) < symtonum(b[i]):
            return 2
        else:
            return 3

    def beautynum(res):
        while res[0] == '0' and (res[1] == '0' or res[1] != '.'):
            res = res[1:]
        if res[0] == '-':
            while res[1] == '0' and res[2] != '.':
                res = '-' + res[2:]
        if res == '-0' or res == '':
            res = '0'
        if res.find('.') != -1 and res[-1] == '0':
            while res[-1] == '0':
                res = res[:-1]
        if res[-1] == '.':
            res = res[:-1]
        return res

    def symtonum(g):
        numbers = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        return numbers.find(g)

    def numtosym(u):
        numbers = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        return numbers[u]

    def fill(a, b):
        if a.find('.') != -1 and b.find('.') != -1:
            sa = len(a[: a.find('.')])
            ea = len(a[a.find('.') + 1:])
            sb = len(b[: b.find('.')])
            eb = len(b[b.find('.') + 1:])
        elif a.find('.') == -1 and b.find('.') != -1:
            sa = len(a)
            ea = -1
            sb = len(b[: b.find('.')])
            eb = len(b[b.find('.') + 1:])
        elif a.find('.') != -1 and b.find('.') == -1:
            sa = len(a[: a.find('.')])
            ea = len(a[a.find('.') + 1:])
            sb = len(b)
            eb = -1
        else:
            sa = len(a)
            ea = 0
            sb = len(b)
            eb = 0
        if sa == sb:
            a = '0' + a
            b = '0' + b
        elif sa > sb:
            b = '0' * (sa - sb + 1) + b
            a = '0' + a
        else:
            a = '0' * (sb - sa + 1) + a
            b = '0' + b
        if ea > eb:
            b = b + '0' * (ea - eb)
        else:
            a = a + '0' * (eb - ea)
        if a.find('.') == -1 and b.find('.') != -1:
            a = zerotodot(a, b.find('.'))
        elif a.find('.') != -1 and b.find('.') == -1:
            b = zerotodot(b, a.find('.'))
        return a, b

    def zerotodot(string, num):
        return string[:num] + '.' + string[num + 1:]

    def dotpos(a, b):
        pos = 0
        if '.' in a or '.' in b:
            if '.' in a:
                pos += len(a[a.find('.') + 1:])
            if '.' in b:
                pos += len(b[b.find('.') + 1:])
        else:
            pos = -1
        return pos

    def addition(a, b):
        f = 0
        res = ''
        for i in range(len(b) - 1, -1, -1):
            if a[i] != '.' and b[i] != '.':
                t = symtonum(a[i]) + symtonum(b[i]) + f
                if t >= c:
                    f = 1
                    t -= c
                    res += str(numtosym(t))
                else:
                    f = 0
                    res += str(numtosym(t))
            else:
                res += '.'
        return res[::-1]

    def subtraction(a, b):
        if whoisbigger(a, b) == 3:
            return '0'
        else:
            f = 0
            res = '0'
            for i in range(len(a) - 1, -1, -1):
                if a[i] != '.' and b[i] != '.':
                    if whoisbigger(a, b) == 1:
                        t = symtonum(a[i]) - symtonum(b[i]) - f
                    else:
                        t = symtonum(b[i]) - symtonum(a[i]) - f
                    if t < 0:
                        f = 1
                        t += c
                        res += str(numtosym(t))
                    else:
                        f = 0
                        res += str(numtosym(t))
                else:
                    res += '.'
            if whoisbigger(a, b) == 1:
                return res[::-1]
            else:
                return '-' + res[::-1]

    def multiplication(a, b):
        itog = ''
        if whoisbigger(a, b) == 2:
            a, b = b, a
        a, b = a[::-1], b[::-1]
        z = 0
        k = max(len(a), len(b))
        for i in range(len(b)):
            res = ''
            f = 0
            if b[i] != '.':
                sa = symtonum(b[i])
                for j in range(len(a)):
                    if a[j] != '.':
                        sb = symtonum(a[j])
                        t = sa * sb + f
                        f = t // c
                        res = numtosym(t % c) + res
                if a.find('.') != -1 and b.find('.') != -1:
                    res = '0' * k + res
                    k -= 1
                res += '0' * z
                z += 1
                res = res[:(len(res) - pos)] + '.' + res[(len(res) - pos):]
                res, itog = fill(res, itog)
                itog = addition(res, itog)
        return itog

    def division(a, b):
        a = float(rebase(a, c, 10))
        b = 1 / float(rebase(b, c, 10))
        return rebase(a * b, 10, c)

    c = int(data['СС'])
    a = data['a'].replace(',', '.').upper()
    b = data['b'].replace(',', '.').upper()
    d = data['Д']

    a, b, s = sign(a, b)
    a, b = fill(a, b)
    print(a, b)
    pos = dotpos(a, b)

    match d:
        case '+':
            match s:
                case 1:
                    res = addition(a, b)
                case 2:
                    res = subtraction(b, a)
                case 3:
                    res = subtraction(a, b)
                case 4:
                    res = '-' + addition(a, b)
        case '-':
            match s:
                case 1:
                    res = subtraction(a, b)
                case 2:
                    res = '-' + addition(a, b)
                case 3:
                    res = addition(a, b)
                case 4:
                    res = subtraction(b, a)
        case '*':
            match s:
                case 1 | 4:
                    res = multiplication(a, b)
                case 2 | 3:
                    res = '-' + multiplication(a, b)
        case '/':
            match s:
                case 1 | 4:
                    res = division(a, b)
                case 2 | 3:
                    res = '-' + division(a, b)
    return beautynum(res)


data = {'СС': '10', 'a': '0.312', 'b': '1.2321', 'Д': '+'}
print(calculate(data))