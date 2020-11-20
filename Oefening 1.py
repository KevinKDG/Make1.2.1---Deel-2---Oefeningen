#!/usr/bin/env python
"""
Maak een programma aan dat de gebruiker vraagt om zijn naam en leeftijd in te voeren.
Print een bericht uit dat aan hen is gericht en dat hen het jaar aangeeft dat ze 100 jaar oud worden.
extra:
Voeg aan het vorige programma toe door de gebruiker om een ander nummer te vragen en druk het vorige bericht af
evenveel keer af.
Druk zoveel mogelijk kopieën van het vorige bericht af op aparte regels.
"""


#               IMPORTS               #
import datetime


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

Name = input('What is your name?: ')    # Input will ask the user for their name
Age = int(input('How old are you?: '))  # Input that asks for your age
Year = datetime.datetime.now().year
Age_100 = 100 - Age

#              MAIN CODE              #
def main():
    print("Good day", Name)
    print("You will be 100 years old in this year:", Age_100 + Year)


if __name__ == '__main__':    #run tests if called from command-line
    main()