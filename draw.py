from tabulate import tabulate
import sys


class console_drawer:
    @staticmethod
    def draw(text:str,file:str=None):
        table = [[text]]
        output = tabulate(table, tablefmt='grid')
        console_drawer.smart_print(output,file)
    @staticmethod
    def smart_print(text:str,filename:str=None):
        if filename and filename != '-':
            fh = open(filename, 'w')
        else:
            fh = sys.stdout

        try:
            print(text, file=fh) # Python 3.x
        finally:
            if fh is not sys.stdout:
                fh.close()