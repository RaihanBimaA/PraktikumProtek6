# Latihan membuat function starFormation 1

def starFormation1(n) :
    kolom = 0
    baris = n
    
    i = 0
    while(i <= n):
        j = 0
        while(j < kolom) :
            print('* ' , end=' ')
            j += 1
        print(' ')
        i += 1
        kolom += 1


#Latihan membuat function starFormation 2

def starFormation2(n) :
    kolom = n
    baris = n

    i = 0
    while(i <= n) :
        j = 0
        while(j < kolom) :
            print('* ', end=' ')
            j += 1
        print(' ')
        i += 1
        kolom -= 1


#Latihan membuat function starFormation 3

def starFormation3(n) :
    kolom = 0
    baris = n
    puncak = (n + 1) / 2
    
    i = 0
    while(i <= n):
        j = 0
        while(j < kolom) :
            print('* ' , end=' ')
            j += 1
        print()
        i += 1
        kolom += 1
        
        if(kolom == puncak) :

            i = 0
            while(i <= n) :
                j = 1
                while(j <= kolom) :
                    print('* ', end=' ')
                    j += 1
                print()
                i += 1
                kolom -= 1

print('starFormation1')
starFormation1(4)
print()
print('starFormation2')
starFormation2(4)
print('starFormation3')
starFormation3(7)




    
