def pfix(exq):
    ta = []
    ops = set(['+', '-', '*', '/', '%', '^'])
    to = exq.split()

    for t1 in reversed(to):
        if t1.isdigit():
            ta.append(int(t1))
        elif t1 in ops:
            if len(ta) < 2:
                return "expression is not complete or invalid"
            op1 = ta.pop()
            op2 = ta.pop()

            if t1 == '^':
                ta.append(op1 ** op2)
            elif t1 == '/':
                if op2 == 0:
                    return "expression is not complete or invalid"
                ta.append(op1 // op2)
            elif t1 == '%':
                if op2 == 0:
                    return "expression is not complete or invalid"
                ta.append(op1 % op2)
            elif t1 == '+':
                ta.append(op1 + op2)
            elif t1 == '-':
                ta.append(op1 - op2)
            elif t1 == '*':
                ta.append(op1 * op2)
        else:
            return "expression is not complete or invalid"

    if len(ta) == 1:
        return ta[0]
    else:
        return "expression is not complete or invalid"


dn2 = {
    "one": 1, "two": 2,
    "three": 3, "four": 4,
    "five": 5, "six": 6,
    "seven": 7, "eight": 8,
    "nine": 9, "zero": 0
}

do1 = {
    "add": '+', "sub": '-',
    "mul": '*', "rem": '%',
    "pow": '^'
}

def conv(s):
    a1 = s.split('c')
    nx = 0
    for i in a1:
        if i in dn2:
            nx = nx * 10 + dn2[i]
        else:
            return "-1"
    return str(nx)

s = input().strip().lower()  
lee = s.split()
st = ""
flag = False

for i in lee:
    if i not in do1:
        jik = conv(i)
        if jik == "-1":
            flag = True
            print("expression evaluation stopped invalid words present", end='')
            break
        st += jik + ' '
    else:
        st += do1[i] + ' '

if not flag:
    print(pfix(st.strip()), end='')
