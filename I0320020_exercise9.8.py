import array
#Mengkonversi string ke array.array
li = [10,20,30,40,50]
C = array.array('i')
C.fromlist(li)
type(C)

for karakter in C:
    print("%d" % karakter, end=' ')