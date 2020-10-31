#Latihan membuat function pythagoras

def isPythagoras(a, b, c) :
    if((a*a) == (c*c) - (b*b) or (b*b) == (c*c) - (a*a) or (c*c) == (b*b) + (a*a)) :
        print(True)
    else :
        print(False)
#coba a
a = 3
b = 4
c = 5

isPythagoras(a,b,c)
#coba b
a = 5
b = 9
c = 12

isPythagoras(a,b,c)
#coba c
a = 8
b = 6
c = 10

isPythagoras(a,b,c)
#coba d
a = 7
b = 8
c = 11

isPythagoras(a,b,c)
