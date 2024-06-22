k = [input() for _ in range(3)]

for idx, i in enumerate(k):
  if i.isdigit():
    r=int(i)+ 3-idx

if r%3==0 and r%5==0:
  print("FizzBuzz")
elif r%3==0:
  print("Fizz")
elif r%5==0:
  print("Buzz")
else:
  print(r)