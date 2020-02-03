import sys

reg16 = lambda x : "{0:016b}".format(x)
reg8 = lambda x : "{0:08b}".format(x)

remainder = int(sys.argv[1])
divisor = int(sys.argv[2])


print('Initial status', reg16(remainder))
print('Remainder:', reg16(remainder))
print('Divisor:  ', reg8(divisor))

remainder = remainder << 1
for i in range(8):
    print('Iteration', i + 1)
    print('    Subtraction')
    print('     ', reg16(remainder))
    print('    -', reg8(divisor))

    subresult = (remainder >> 8) - divisor
    if subresult >= 0:
        print('    Remainder >= 0')
        remainder = (subresult << 8) | (remainder & ((1<<8) - 1))
        print('    Remainder before shifting:')
        print('     ', reg16(remainder))
        remainder = (remainder << 1) | 1
    else:
        print('    Remainder < 0')
        print('    Remainder restored:')
        print('     ', reg16(remainder))
        remainder = (remainder << 1) | 0

    print('    Remainder after shifting:')
    print('     ', reg16(remainder))

quotient = remainder & ((1 << 8) - 1)
remainder = remainder >> (8 + 1)

print('Quotient (binary):  ', reg8(quotient))
print('Remainder (binary): ', reg8(remainder))

print('Quotient (decimal): ', quotient)
print('Remainder (decimal): ', remainder)
