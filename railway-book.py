import os

DB_DIR = r'C:\Users\sushil\Documents\mypython\examples'
RAIL_DB = {}
VALID_COACHES = ['ac1','ac2','ac3','s1']
VALID_SEAT_PREF = ['L','M','U','N']
PNR = 1

def print_header():
    print '-'*50
    print "       WELCOME TO INDIAN RAILWAYS"
    print '-'*50

def first_screen():
    print "\n"
    print "Enter your choice:-"
    print r'(1) Register'
    print r'(2) Login'
    valid_choices = [1,2]
    choice = int(raw_input("choice : "))
    if choice not in valid_choices:
        print '\n'
        print "Please Enter a valid choice only"
        first_screen()
    else:
        return choice

