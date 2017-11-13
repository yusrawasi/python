#1
def donuts(count):
  if count<10:
      st="Number of donuts: " + str(count)

  else:
      st = "Number of donuts: Many"
  return st
print(donuts(8))

#2
def both_ends(s):
    if len(s)>=2:
        str= s[:2]+s[-2:]

    else:
        str=" "
    return str

print(both_ends("stable"))

#3
def fix_start(se):
    a=se[1:].replace(se[0],"*")
    a=se[0]+a
    return a

print(fix_start("papperiz"))

#4
def mix_up(a, b):

    l=b[0:2] + a[2:]+ " " + a[0:2]+b[2:]



    return l


print(mix_up("mix","pop"))

#5
def test(got, expected):
    if got == expected:
        prefix="ok"
    else:
        prefix="x"
    print(prefix," got:",got, " expected:", expected  )


#6
def main():
    print("Donuts")
    lo="Number of donuts: 8"
  # Each line calls donuts, compares its result to the expected for that call.
    test(donuts(8),lo)
    test(both_ends("spring"), "spng")
    test(fix_start('babble'), 'ba**le')
    test(mix_up('mix', 'pod'), 'pox mid')



main()


