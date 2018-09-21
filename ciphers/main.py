from ceaser import Ceaser

# c = Ceaser('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz ', 3)
c = Ceaser('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz ', 4)

a = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
print(a)
a = ''.join(c.encode(a))
print(a)

b = 'So does this really work'
print(b)
b = ''.join(c.encode(b))
print(b)
b = ''.join(c.decode(b))
print(b)
