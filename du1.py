#načtení potřebných knihoven
import turtle
from math import sqrt
t = turtle.Turtle()

#nastavení počtu sloupců a řádků hrací čtvercové sítě
sloupec = int(input('Zadejte počet sloupců mřížky:'))
while sloupec < 0:
    sloupec = int(input('Neplatný zápis. Zadejte znovu počet sloupců mřížky:'))
radek = int(input('Zadejte počet řádků mřížky:'))
while radek < 0:
    radek = int(input('Neplatný zápis. Zadejte znovu počet řádků mřížky:'))

#volitelná délka hrany čtverce:
#X = int(input("Zadejte délku strany čtverce:"))
#while X < 0:
   #X = int(input('Neplatný zápis. Zadejte znovu délku strany čtverce:'))
X=40            #délka strany čtverce 

t.speed(0)      #nastavení rychlosti želvy
#vykreslení čtvercové sítě 
for _ in range(radek):
    for _ in range(sloupec):
        for _ in range(4):
            t.forward(X)
            t.left(90)
        t.forward(X)
    t.left(180)
    t.forward(X*sloupec)  
    t.right(90)
    t.forward(X)
    t.right(90)
t.penup()

#definování funkce pro vykreslení kolečka
def draw_circle():
    r = (X/2)           #výpočet poloměru kruhu (možnost úpravy podle velikosti čtvercové sítě)
    t.pencolor('red')
    t.circle(r)

#definování funkce pro vykreslení křížku 
def draw_cross():
    U = sqrt(2*(X**2))  #přepočet křížku na velikost čtvercové sítě v případě jejího libovolného nastavení 
    t.pencolor('blue')
    t.left(45)
    t.forward(U)
    t.right(180)
    t.forward(U/2)
    t.left(90)
    t.forward(U/2)
    t.right(180)
    t.forward(U)

#výpočet počtu tahů ve hře
pocet_policek = radek * sloupec
cross_player = True

#cyklus střídání hráčů X a O
while pocet_policek > 0:        
    #první hraje X hráč
    if cross_player == True:
        L = int(input("X hráči, zadej x-ovou souřadnici: ")) 
        while L > radek or L < 0:
            L = int(input("Chybný zápis, zadejte znovu souřadnice pro X: "))
        M = int(input("X hráči, zadej y-ovou souřadnici: "))
        while M > sloupec or M < 0:
            M = int(input("Chybný zápis, zadejte znovu souřadnice pro Y: ")) 
        t.setpos(L*X-X,M*X-X)
        t.pendown()
        draw_cross()
        t.penup()
    else:
        N = int(input("O hráči, zadej x-ovou souřadnici: "))  
        while N > radek or N < 0:
            N = int(input("Chybný zápis, zadejte znovu souřadnice pro X: "))
        K = int(input("O hráči, zadej y-ovou souřadnici: "))     
        while K > sloupec or K < 0:
            K = int(input("Chybný zápis, zadejte znovu souřadnice pro Y: "))
        N = N*X
        K = K*X
        t.setpos(N-X/2,K-X)
        t.pendown()
        draw_circle()
        t.penup()
    cross_player = not cross_player     #dochází zde k negaci původní hodnoty cross_player a while cyklus tak střídá mezi oběma hráči 
    pocet_policek = pocet_policek - 1   #odečtením se snižuje počet tahů ve hře
print("GAME OVER!")
turtle.exitonclick()