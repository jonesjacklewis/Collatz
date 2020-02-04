def collatz(val):
    count = 0
    if val == 1:  # if val is one
        print("It is already one")
    while val != 1:  # while val isn't one
        if val % 2 == 0:  # If val is even
            val /= 2  # Halve val
            count += 1  # Increment Count
        else:
            val *= 3  # Triple val
            val += 1  # Increment val by one
            count += 1  # Increment count by one
    return count


n = int(input("Enter a number greater than 1"))
col_val = str(collatz(n))  # Converts collatz to string
n = str(n)  # Converts n to string
print(" It will take %s turns for %s to reach one. " % (col_val, n))
