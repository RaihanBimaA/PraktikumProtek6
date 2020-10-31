def faktorial(n) :
    faktorialAwal = 1
    while(n > 0) :
        faktorialAwal = faktorialAwal * n
        n -= 1
    return faktorialAwal


def kombinasi(a,b) :
    c = a - b
    
    hasil = faktorial(a) / (faktorial(b) * faktorial(c))
    print(hasil)

def permutasi(a,b) :
    c = a - b

    hasil = faktorial(a) / faktorial(c)
    print(hasil)
    
# C = kombinasi

a = 5
b = 3
kombinasi(a,b)

# P = permutasi

x = 10
y = 7
permutasi(x,y)



    




