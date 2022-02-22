import time
import pyfiglet
import locale

def date(form='%Y %d %b, %A', font='graceful'):
    return pyfiglet.figlet_format(time.strftime(form, time.gmtime()), font)

def main():
    locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
    import sys
    if len(sys.argv) == 1:
        print(date())
    elif len(sys.argv) == 2:
        print(date(sys.argv[1]))
    elif len(sys.argv) == 3:
        print(date(sys.argv[1], sys.argv[2]))
        
if __name__ == '__main__':
    sys.exit(main())
