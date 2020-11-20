#!/usr/bin/env python
"""
Maak een programma dat drie variabelen als input neemt en de grootste van de drie teruggeeft.
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

List = []
print("Enter your numbers:")


#              MAIN CODE              #
def main():

    for i in range(3):                     # Loops the program depending on how long the list has to be
        num = int(input())
        List.append(num)                            # Add the numbers to the list
    print("This the highest number from your list", max(List))
    print("This is your full list", List)

if __name__ == '__main__':    #run tests if called from command-line
    main()