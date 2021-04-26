import sys
#mendefiniskan array konstan
HARI = ('Minggu', 'Senin', 'Selasa', 'Rabu',
        'Kamis', 'Jumat', 'Sabtu')

def main():
    #meminta user memasukkan nomor hari
    nohari = int(input("Memasukkan nomor hari [1..7]: "))

    if (nohari < 1) or (nohari > 70):
        print("Tidak ada hari ke-%s" % nohari)
        sys.exit()

    print("Hari ke-%d adalah %s" % (nohari, HARI[nohari-1]))

if __name__ == '__main__':
    main()