def OS2IP(X):
    """Return the integer primitive x for the octet-string X."""
    # the sum below is the same as: int.from_bytes(X, byteorder = 'big')
    return sum([x * 256**i for i, x in enumerate(X[::-1])])
    

def I2OSP(x, xLen):
    """Map an integer x to an octet-string X of length xLen."""
    assert x < 256**xLen, "integer too large"
    # below is the same as: return x.to_bytes(xLen, byteorder = 'big')
    if x == 0:
        return b'\x00'
    bs = b''
    while x:
        bs += (x % 256).to_bytes(1, byteorder = 'big')
        x //= 256
    return b'\x00' * (xLen - len(bs)) + bs[::-1]
    
