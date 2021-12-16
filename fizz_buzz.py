a = 'Fizz'
b = 'Buzz'
sr = 1
er = 100
for i in range(sr,er+1):
      if i % 3 == 0 and i % 5 == 0:
            print(a+b)
      elif i % 3 == 0:
            print(a)
      elif i % 5 ==0:
            print(b)
      else:
            print(i)
