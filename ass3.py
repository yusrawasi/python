#1
def match_ends(words):
    count=0
    for word in words:
        if len(word)>=2 and word[0]==word[-1]:
            count+=1

    return count

print(match_ends(["string","appla","ends","pap","opo","p"]))
#2
def front_x(words):
    list1=[]
    list2=[]
    for word in words:
        if word[0]=='x':
            list1.append(word)
        else:
            list2.append(word)
    list1.sort()

    list2.sort()


    return list1 + list2


print(front_x(["mix", "xyz", "apple", "xanadu", "aardvark"]))
#3
def sort_last(tuples):
  tuples=sorted(tuples, key=lambda tuples:tuples[-1])
  return tuples

def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))


# Calls the above functions with interesting inputs.
def main():
    print('match_ends')
    test(match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']), 3)
    test(match_ends(['', 'x', 'xy', 'xyx', 'xx']), 2)
    test(match_ends(['aaa', 'be', 'abc', 'hello']), 1)

    print
    print('front_x')
    test(front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa']),
         ['xaa', 'xzz', 'axx', 'bbb', 'ccc'])
    test(front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']),
         ['xaa', 'xcc', 'aaa', 'bbb', 'ccc'])
    test(front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']),
         ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'])

    print
    print('sort_last')
    test(sort_last([(1, 3), (3, 2), (2, 1)]),
         [(2, 1), (3, 2), (1, 3)])
    test(sort_last([(2, 3), (1, 2), (3, 1)]),
         [(3, 1), (1, 2), (2, 3)])
    test(sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)]),
         [(2, 2), (1, 3), (3, 4, 5), (1, 7)])

if __name__ == '__main__':
  main()