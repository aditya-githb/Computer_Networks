def parity(data, even):
  count = 0
  while data:
    count += data & 1
    data >>= 1
  return (even and (count % 2 == 0)) or (not even and (count % 2 == 1))

def main():
  data = int(input("Enter data word (binary): "), 2)
  even = int(input("Enter parity type received (0: Even, 1: Odd): "))

  expected_parity = parity(data >> 1, even) 
  received_parity = data & 1

  if expected_parity == received_parity:
    print("Parity OK")
  else:
    print("Parity Error!")

if __name__ == "__main__":
  main()
