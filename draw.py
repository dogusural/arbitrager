from tabulate import tabulate
import sys


class console_drawer:
    
    @staticmethod
    def draw(text:str,file:str=None):
        table = [[text]]
        output = tabulate(table, tablefmt='fancy_grid')
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
    @staticmethod
    def indent(txt, spaces=40):
        return "\n".join(" "*spaces + ln for ln in txt.splitlines())
    @staticmethod
    def draw_header(header0:str,header1:str):

        W  = '\033[0m'  # white (normal)
        R  = '\033[31m' # red
        G  = '\033[32m' # green
        O  = '\033[33m' # orange
        B  = '\033[34m' # blue
        P  = '\033[35m' # purple
        print(console_drawer.indent(tabulate([[G + header0 +'      '+ R + header1 + W ]] ,tablefmt='fancy_grid' )))
