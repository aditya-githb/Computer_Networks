def parity(data, even):
    count = 0
    while data:
        count += data & 1
        data >>= 1
    return (even and (count % 2 == 0)) or (not even and (count % 2 == 1))

def main():
    data = input("Enter data word (binary): ")
    try:
        int_data = int(data, 2)
    except ValueError:
        print("Invalid binary input.")
        return
    
    even = int(input("Enter parity type (0: Even, 1: Odd): "))
    
    if even not in [0, 1]:
        print("Invalid parity type. Enter 0 for Even or 1 for Odd.")
        return

    is_even_parity = parity(int_data, even)
    
    if is_even_parity:
        data_with_parity = (int_data << 1) | 1
    else:
        data_with_parity = (int_data << 1) | 0
    
    print("Data word with parity bit:", bin(data_with_parity)[2:])

if __name__ == "__main__":
    main()
