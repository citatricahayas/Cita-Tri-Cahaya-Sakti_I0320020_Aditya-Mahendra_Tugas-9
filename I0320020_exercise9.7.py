
#Mengkonversi string ke array.array
B = bytearray.array('c')
B.fromstring("Python")

for karakter in B:
    print("%c" % karakter, end=' ')