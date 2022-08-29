from machine import Pin as pin
from utime import sleep as pausa, sleep_ms as pausam, sleep_us as pausau
puerto=[13,12,14,27,26,25,33,22]
t=[]
boton1=pin(5,pin.IN,pin.PULL_UP)
boton2=pin(4,pin.IN,pin.PULL_UP)
boton3=pin(19,pin.IN,pin.PULL_UP)
boton4=pin(21,pin.IN,pin.PULL_UP)
botonV1=pin(2,pin.IN,pin.PULL_UP)
botonV2=pin(18,pin.IN,pin.PULL_UP)
ob=pin(0)

pausar=150
pausaA=150

for i in puerto:
    t.append (pin(i,pin.OUT))
print(t)

def speed():
        if (not botonV1.value()):
            global pausaA
            if(pausaA<450):
                pausaA+=30
                pausam(int(pausaA))
            else:
                pausaA=150
                pausam(int(pausaA))
        if (not botonV2.value()):
            global pausar
            if (pausar>0):
                pausar-=1
                pausam(int(pausar))
            else:
                pausar=150
                pausam(int(pausar))
        else:
            pausam(150)

def pattern1():
    for i in (t):
        for j in range(9):
            i.value(not i.value())
        speed()
        
def pattern2():
    for i in reversed(t):
        for j in range(9):
            i.value(not i.value())
        speed()

def pattern3():
    for i in t:
        indice=t.index(i)   
        for j in range(9):
            if (indice%2):
                i.value(not i.value())
            else:
                i.value(i.value())
        speed()
        
def pattern4():
    for i in reversed (t):
        indice=t.index(i)   
        for j in range(9):
            if (indice%2):
                i.value(not i.value())
            else:
                i.value(i.value())
        speed()
        
def pattern5():
    for i in t:
        indice=t.index(i)   
        for j in range(9):
            if (not indice%2):
                i.value(not i.value())
            else:
                i.value(i.value())
        speed()
   
def pattern6():
    for i in reversed (t):
        indice=t.index(i)   
        for j in range(9):
            if (not indice%2):
                i.value(not i.value())
            else:
                i.value(i.value())
        speed()
        
def pattern7():
    for i in t:
        indice=t.index(i)   
        for j in range(9):
            if (indice%3):
                i.value(not i.value())
            else:
                i.value(i.value())
        speed()
        
def pattern8():
    for i in reversed (t):
        indice=t.index(i)   
        for j in range(9):
            if (indice%3):
                i.value(not i.value())
            else:
                i.value(i.value())
        speed()

def pattern9():
    for i in t:
        indice=t.index(i)   
        for j in range(9):
            if (not indice%3):
                i.value(not i.value())
            else:
                i.value(i.value())
        speed()
        
def pattern10():
    for i in reversed (t):
        indice=t.index(i)   
        for j in range(9):
            if (not indice%3):
                i.value(not i.value())
            else:
                i.value(i.value())
        speed()
        
def pattern11():
    for i in t:
        indice=t.index(i)   
        for j in range(9):
            if (indice%4):
                i.value(not i.value())
            else:
                i.value(i.value())
        speed()
        
def pattern12():
    for i in reversed (t):
        indice=t.index(i)   
        for j in range(9):
            if (indice%4):
                i.value(not i.value())
            else:
                i.value(i.value())
        speed()
        
def pattern13():
    for i in t:
        indice=t.index(i)   
        for j in range(9):
            if (not indice%4):
                i.value(not i.value())
            else:
                i.value(i.value())
        speed()
        
def pattern14():
    for i in reversed (t):
        indice=t.index(i)   
        for j in range(9):
            if (not indice%4):
                i.value(not i.value())
            else:
                i.value(i.value())
        speed()
        
def pattern15():
    for i in t:
        indice=t.index(i)   
        for j in range(9):
            if (indice%2):
                i.value(i.value())
            else:
                i.value(not i.value())
        speed()
        
def pattern16():
    for i in reversed (t):
        indice=t.index(i)   
        for j in range(9):
            if (indice%2):
                i.value(i.value())
            else:
                i.value(not i.value())
        
        
while True:
    
        if (not boton1.value()):
            pattern1()                                                                                                                                                                                                                                               
            print ("Secuencia 1")
        if (not boton2.value()):
            pattern2()                                                                                                                                                                                                                                               
            print ("Secuencia 2")
        if (not boton3.value()):
            pattern3()
            print("Secuencia 3")
        if (not boton4.value()):
            pattern4()
            print("Secuencia 4")
        if(not boton1.value() and not boton2.value()):
            pattern5()
            print("Secuencia 5")
        if(not boton2.value() and not boton3.value()):
            pattern6()
            print("Secuencia 6")
        if(not boton2.value() and not boton4.value()):
            pattern7()
            print("Secuencia 7")
        if (not boton3.value() and not boton4.value()):
            pattern8()
            print("Secuencia 8")
        if (not boton1.value() and not boton4.value()):
            pattern9()
            print("Secuencia 9")
        if (not boton1.value() and not boton3.value()):
            pattern10()
            print("Secuencia 10")
        if (not boton2.value() and not boton3.value()):
            pattern11()
            print("Secuencia 11")
        if (not boton1.value() and not boton2.value() and not boton3.value()):
            pattern12()
            print("Secuencia 12")
        if (not boton1.value() and not boton3.value() and not boton4.value()):
            pattern13()
            print("Secuencia 13")
        if (not boton1.value() and not boton2.value() and not boton4.value()):
            pattern14()
            print("Secuencia 14")
        if (not boton2.value() and not boton3.value() and not boton4.value()):
            pattern15()
            print("Secuencia 15")
        if (not boton1.value() and not boton2.value() and not boton3.value() and not boton4.value()):
            pattern16()
            print("Secuencia 16")