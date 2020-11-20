#!/usr/bin/env python
"""
Schrijf een programma dat een lijst van getallen neemt (bijvoorbeeld, a = [5, 10, 15, 20, 25]) en maakt een nieuwe lijst
van alleen de eerste en laatste elementen van de gegeven lijst.
Om te oefenen, schrijf deze code waarbij het mogelijk is dat de lijst eerst aan de user wordt gevraagd.
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

Username = input("What is your username?: ")
print("Hello,", Username)

lenghtList = int(input("How long do you want your list to be?: "))
List = []
print("Enter your numbers:")


#              MAIN CODE              #
def main():

    for i in range(lenghtList):                     # Loops the program depending on how long the list has to be
        num = int(input())
        List.append(num)                            # Add the numbers to the list
    print("This is your list", List)
    rest = [List[0], List[-1]]                      # Grabs the first and last values from the list
    print("The first and last items are: ", rest)


if __name__ == '__main__':    #run tests if called from command-line
    main()