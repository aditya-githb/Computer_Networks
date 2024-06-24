def counter_generator(start, end, step=1):

  for i in range(start, end + 1, step):
    yield i

if __name__ == "__main__":
  start = int(input("Enter starting value: "))
  end = int(input("Enter ending value (inclusive): "))
  step = int(input("Enter step size (default 1): ") or 1)

  counter = counter_generator(start, end, step)

  for value in counter:
    print(value, end=" ")

  print()
