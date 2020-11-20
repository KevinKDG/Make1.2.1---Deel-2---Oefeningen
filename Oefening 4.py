#!/usr/bin/env python
"""
Maak een programma waarbij je de gebruiker vraagt om 2 dingen in te geven nl. zijn naam en geboortedatum.
Je script geeft in een volledige zin deze 2 waarden terug.
"""


#               IMPORTS               #


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
__status__ = "Development"

Name = input("What is your first & last name?: ")
Birthday = input("Whats your date of birth dd/mm/yy?: ")


#              MAIN CODE              #
def main():
    print("Your name is", Name, "and you were born on", Birthday, """
    I also heard that this person was really kind to everyone
    
    """)


if __name__ == '__main__':    #run tests if called from command-line
    main()