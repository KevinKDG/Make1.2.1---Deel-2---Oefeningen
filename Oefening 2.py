#!/usr/bin/env python
"""
Vraag de gebruiker om een nummer.
Afhankelijk van het feit of het nummer even of oneven is, print dan een passend bericht uit naar de gebruiker.
Je maakt geen gebruik van flowcontrol.
"""


#               IMPORTS               #
import time

#          AUTHOR INFORMATION         #  

#        _____
#      .'     `.
#     /  .-=-.  \   \ __
#     | (  C\ \  \_.'')
#     _\  `--' |,'   _/
#    /__`.____.'__.-' The coding snail~

__author__ = "Kevin Vervloet"
__email__ = "kevin.vervloet@student.kdg.be"
__Version__ = "(Code version)"
__status__ = "Finished"

print('~This program will tell you if a number is even or uneven~')


#              MAIN CODE              #
def main():

    Number = int(input('Please enter your number here: '))
    if (Number % 2) ==  0:
        print(Number,'Is an even number!')


    else:
        print(Number,'Is oneven')

    time.sleep(1)
    retry = input('Would you like to pick another number? (y/n)')
    if retry == 'y' or retry == 'yes':
        main()
    if retry == "n" or retry == "no":
        print("See you next time!")


if __name__ == '__main__':    #run tests if called from command-line
    main()