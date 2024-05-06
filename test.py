from main import friendly_bytes

def test_friendly_bytes():
    assert friendly_bytes(102) == '102 B'
    assert friendly_bytes(1111111111, binary=True) == '1.03 GiB'
    assert friendly_bytes(1111111111, decimals=3) == '1.111 GB'
    assert friendly_bytes(1111111111, decimals=3, binary=True) == '1.035 GiB'
    assert friendly_bytes(1234567890) == '1.23 GB'


if __name__ == "__main__":
   test_friendly_bytes()
   print("SUCCESS!")

