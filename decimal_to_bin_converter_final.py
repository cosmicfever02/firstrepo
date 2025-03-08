nums = [0, 1, 3, 5, 6, 7, 8, 10, 11, 13, 25, 69]

for n in nums:

    # Find largest bit needed
    b = 0
    while n - 2**b >= 2**b:
        b += 1

    # Make empty list for forming binary
    bn = ['0'] * (b + 1)

    #Place 1 in appropriate index if number progressively
    #   subtracted by powers of 2 isn't less than 0
    x = b
    temp = n
    for i in range(0, b + 1):
        
        if temp - 2**x < 0:
            x -= 1
            continue
        else:
            temp = temp - 2**x
            x -= 1
            bn[i] = '1'
    
    # Convert list to string
    binary = ""
    for digit in bn:
        binary += digit

    # Output result
    print("Num:", n, ", Binary:", binary)