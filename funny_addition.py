def checkio(data):
    """Return the sum of two integer elements"""
    a, b = data
    xor = a ^ b
    carry = a & b
    while carry:
        xor2 = xor
        carry <<= 1
        xor ^= carry
        carry &= xor2
    return xor

if __name__ == '__main__':
    assert checkio([5, 5]) == 10, 'First'
    assert checkio([7, 1]) == 8, 'Second'
    print('All ok')
