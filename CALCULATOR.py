# -*- coding: utf-8 -*-

# програма Калькулятор

print "Вітаємо!"

loop = 1



choice = 0

 

while loop == 1:


    print "Vuberit diy:"

    print "1) Dodavannya"

    print "2) Vidnimannya"

    print "3) Mnojennya"

    print "4) Dilennya"

    print "5) Zakrutu kalkulyator"



    choice = input("Oberit vashy diy: ")

    if choice == 1: 

        num1 = input("Dodatu ce chuslo: ")

        num2 = input("Do cyogo: ")

 

    

        print num1, " + ", num2, " = ", num1 + num2

    elif choice == 2: 

        num1 = input("Vidnimaemo chuslo: ")

        num2 = input("vid: ")

        print num2, " - ", num1, " = ", num2 - num1

    elif choice == 3:

        num1 = input("Mnojumo: ")

        num2 = input("na: ")

        print num1, " * ", num2, " = ", num1 * num2

    elif choice == 4: 

        num1 = input("Dilumo chuslo: ")

        num2 = input("na: ")

        print num1, " / ", num2, " %= ", num1 / num2

    elif choice == 5: 

        loop = 0

 



print "The end"
