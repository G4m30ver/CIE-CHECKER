###########################
#        Author           #
#     BY: G4M30VER        #
#     01/Dec/2020         #
###########################
import argparse
import random
import os,sys

class Color:
    #Git shell coloring
    #https://gist.github.com/vratiu/9780109
    red = "\033[0;31m"          # Red
    green = "\033[0;32m"        # Green

class Checker:
    def __init__(self,cie):
        self.cie = cie
        self.cie_numbers = []
        self.verify = 0

        self.even = []
        self.odd = []

    #First step, organize the differents numbers to begin to the calc
    def organize(self):
        #1- Separate numbers and add in the list
        for numbers in self.cie:
            self.cie_numbers.append(int(numbers))
        
        #2- Extract the last number and remove to the list
        self.verify = self.cie_numbers[-1]
        self.cie_numbers.pop(-1)

        #3 - Extract the position numbers, even and odd later append to the other list
        for position in range(len(self.cie_numbers)):
            if position%2 == 0:
                self.odd.append(self.cie_numbers[position])
            else:
                self.even.append(self.cie_numbers[position])
    
        #4- Select the even position numbers and multiply them by 2
        #The Numbers to word would be the even numbers, but the list begin with 0
        #seria algo como
        #1 2 3 4 5 6 7 8 9 10
        #0 1 2 3 4 5 6 7 8 9
        #posicion con 10 - 2 4 6 8 10
        #posicion sin 10 - 1 3 5 7 9
        even_position = [i*2 for i in self.even]

        #5- Identify numbers with 2 or more digits and adds them
        for numbers in range (len(even_position)):
            if len(str(even_position[numbers])) == 2:
                number = int(str(even_position[numbers])[0])+int(str(even_position[numbers])[1])
                even_position[numbers] = number

        return even_position

    #Second step, calculate all numbers, in this case (even_solved and even list)
    def calculate(self, even_solved):
        calc = str(sum(even_solved)+sum(self.odd))
        if int(calc[-1]) == self.verify:
            print(Color.green+'{} : is valid'.format(self.cie))
        else:
            print(Color.red+'{} : is not valid'.format(self.cie))
        
    
class Generate:
    def __init__(self, quantity=10):
        self.quantity = quantity
        for i in range(self.quantity):
            ced = random.randint(40200000000, 40249999999)
            gen = Checker(str(ced))
            gen.calculate(gen.organize())

if __name__ == "__main__":
    option = argparse.ArgumentParser(
    description='Dominican Cedula Checker and Generator',
    epilog='python3 {} -C XXXXXXXXXXX '.format(os.path.basename(__file__)))

    option.add_argument('-G', '--generate',  help='Generate random Dominican Cedula (10 Default)', action='store_true')
    option.add_argument('-Q', '--quantity', type=int, default=10, help='Quantity of Cedula to generate')
    option.add_argument('-C', '--check', help='Check Cedula')
    args = option.parse_args()

    if args.generate:
        Generate(args.quantity)
    elif args.check:
        cie = Checker(args.check)
        cie.calculate(cie.organize())

    
    if len(sys.argv) <= 1:
        option.print_help()
            
