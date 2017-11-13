#1
def verbing(s):
    if len(s)>=3 and s[-3:]=="ing" :
        s=s+"ly"
    elif len(s)>=3:
        s=s+"ing"

    return s

print(verbing("increasing"))
print(verbing("print"))
print(verbing("an"))
#2
def not_bad(s):
    c=s.find("bad")
    d=s.find("not")
    if c > d:
        a=s[0:d] + "good" + s[c+3:]
        return a


print(not_bad("dinner is not that bad!"))
#3
def front_back(a,b):
    if len(a)%2==0:
        v=int(len(a)/2)

    else:
        v = int(len(a) / 2)+1

    a_front = a[:v]

    a_back = a[v:]


    if len(b)%2==0:
        n=int(len(b)/2)
    else:
        n= int(len(b) / 2)+1
    b_front = b[:n]

    b_back = b[n:]
    string = a_front + b_front + a_back + b_back
    return string
print(front_back("strings","angle"))
#4
def test(got, expected):
    if got == expected:
        prefix="ok"
    else:
        prefix="x"
    print("got : expected ", prefix )
#5
def main():
    test(front_back("strings","angle"),"striangngsle")
    test(not_bad('This movie is not so bad'), 'This movie is good')
    test(verbing('hail'), 'hailing')
main()


