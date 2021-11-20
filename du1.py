#načtení potřebných knihoven
import turtle
from math import sqrt
t = turtle.Turtle()

#volitelná délka hrany čtverce:
#X = int(input("Zadejte délku strany čtverce:"))
#while X < 0:
   #X = int(input('Neplatný zápis. Zadejte znovu délku strany čtverce:'))
delka_strany=40            #délka strany čtverce 

#definování funkce pro vykreslení kolečka
def draw_circle(r):
    t.pencolor('red')
    t.circle(r)


#definování funkce pro vykreslení křížku 
def draw_cross(u): 
    t.pencolor('blue')
    t.left(45)
    t.forward(u)
    t.right(180)
    t.forward(u/2)
    t.left(90)
    t.forward(u/2)
    t.right(180)
    t.forward(u)

#nastavení počtu sloupců a řádků hrací čtvercové sítě
sloupec = int(input('Zadejte počet sloupců mřížky:'))
while sloupec <= 0:
    sloupec = int(input('Neplatný zápis. Zadejte znovu počet sloupců mřížky:'))
radek = int(input('Zadejte počet řádků mřížky:'))
while radek <= 0:
    radek = int(input('Neplatný zápis. Zadejte znovu počet řádků mřížky:'))

t.speed(0)      #nastavení rychlosti želvy
#vykreslení čtvercové sítě 
for _ in range(radek):
    for _ in range(sloupec):
        for _ in range(4):
            t.forward(delka_strany)
            t.left(90)
        t.forward(delka_strany)
    t.left(180)
    t.forward(delka_strany*sloupec)  
    t.right(90)
    t.forward(delka_strany)
    t.right(90)
t.penup()

#výpočet počtu tahů ve hře
pocet_policek = radek * sloupec
cross_player = True

#cyklus střídání hráčů X a O
for _ in range (pocet_policek):    
    #první hraje X hráč
    if cross_player == True:
        hrac_x = int(input("X hráči, zadej x-ovou souřadnici: ")) 
        while hrac_x <= 0 or hrac_x > sloupec:
            hrac_x = int(input("Chybný zápis, zadejte znovu souřadnice pro X: "))
        hrac_y = int(input("X hráči, zadej y-ovou souřadnici: "))
        while hrac_y <= 0 or hrac_y > radek:
            hrac_y = int(input("Chybný zápis, zadejte znovu souřadnice pro Y: ")) 
        t.setpos(hrac_x*delka_strany-delka_strany,hrac_y*delka_strany-delka_strany)
        t.pendown()
        draw_cross(sqrt(2*(delka_strany**2)))
        t.right(135)
        t.penup()
    else:
        hrac_x = int(input("O hráči, zadej x-ovou souřadnici: "))  
        while hrac_x <= 0 or hrac_x > sloupec:
            hrac_x = int(input("Chybný zápis, zadejte znovu souřadnice pro X: "))
        hrac_y = int(input("O hráči, zadej y-ovou souřadnici: "))     
        while hrac_y <= 0 or hrac_y > radek:
            hrac_y = int(input("Chybný zápis, zadejte znovu souřadnice pro Y: "))
        hrac_x = hrac_x*delka_strany
        hrac_y = hrac_y*delka_strany
        t.setpos(hrac_x-(delka_strany/2),hrac_y-delka_strany)
        t.pendown()
        draw_circle(delka_strany/2)
        t.penup()
    cross_player = not cross_player     #dochází zde k negaci původní hodnoty cross_player a for cyklus tak střídá mezi oběma hráči 
print("GAME OVER!")
turtle.exitonclick()