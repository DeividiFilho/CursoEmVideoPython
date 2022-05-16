tab = 0

while True:
  n = int(input("Quer ver a tabuada de qual número?  "))
  if n < 0:
    break
  for i in range(1,11):
    print(f"{n} x {i} = {n*i}")