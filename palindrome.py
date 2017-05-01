def palindrome(num):
    print(num)
    if num < 10:
        return True
    else:
        cont = 0
        copia_num = num
        while copia_num >= 10:
            cont += 1
            copia_num //= 10

        primer = num // (10 ** cont)
        ultimo = num % 10

        if primer != ultimo:
            return False
        else:
            num_parcial = num % (10 ** cont)
            num_parcial //= 10
            return palindrome(num_parcial)

print(palindrome(1143211))
