import os

DB_DIR = r'C:\Users\sushil\Documents\mypython\examples'
RAIL_DB = {}
VALID_COACHES = ['ac1', 'ac2', 'ac3', 's1']
VALID_SEAT_PREF = ['L', 'M', 'U', 'N']
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
    valid_choices = [1, 2]
    choice = int(raw_input("choice : "))
    if choice not in valid_choices:
        print '\n'
        print "Please Enter a valid choice only"
        first_screen()
    else:
        return choice


def input_password(check=True):
    password = raw_input("Enter Password :")
    if check and len(password) == 0:
        print '\n'
        print "Enter password with atleast one char"
        input_password()
    return password


def input_user_name():
    user_name = raw_input("Enter user name :")
    if not user_name:
        print '\n'
        print "Enter valid user name"
        input_user_name()
    return user_name


def register_user():
     user_name = input_user_name()
    password = input_password()
    if check_user_exist(user_name):
        print '\n'
        print "User Already Exists"
        return 1
    else:
        create_user_passwd_file(user_name,password)
        print '\n'
        print "User Registration Successful"

def check_user_exist(user_name):
    user_file = user_name + r'.txt'
    if os.path.exists(os.path.join(DB_DIR,user_file)):
        return True
    else:
        False

def create_user_passwd_file(user_name,password):
    user_file = user_name + r'.txt'
    fd = open(os.path.join(DB_DIR,user_file),'w')
    fd.write(password)
    fd.close()

def verify_password(user_name,password):
    #import pdb ; pdb.set_trace()
    if check_user_exist(user_name):
        user_file = user_name + r'.txt'
        fd = open(os.path.join(DB_DIR,user_file))
        act_paswd = fd.read()
        if act_paswd == password:
            return True
        else:
            return False
    else:
        return False

def init_db(total_seats=42):
     ac3 = {'L':range(1,total_seats,3),
            'M':range(2,total_seats,3),
            'U':range(3,total_seats,3)}

     ac2 = {'L':range(1,total_seats,2),
            'U':range(2,total_seats,3)}

     ac1 = {'L' : range(1,total_seats)}

     s1 = {'L':range(1,total_seats,3),
           'M':range(2,total_seats,3),
           'U':range(3,total_seats,3)}

     RAIL_DB.update({'ac1':ac1,'ac2':ac2,'ac3':ac3,'s1':s1})

def get_vacant_seat(coach,r_nos,seat_pref='L'):
    try:
        if len(RAIL_DB[coach][seat_pref]) >= r_nos:
            print RAIL_DB[coach][seat_pref][:r_nos]#################
            return RAIL_DB[coach][seat_pref][:r_nos]
    except KeyError:
        print "This Berth does not exsist in",coach
    '''else:
        return False'''############################################

def reserve_in_db(coach,seat_pref,seats):
    for seat in seats:
        RAIL_DB[coach][seat_pref].remove(seat)

def print_tkt(source,dest,coach,seat_no):
    global PNR
    

    print '*'*50
    print "PNR    :   0000" + str(PNR)
    print "SOURCE : %s                 DESTINATION : %s" %(source,dest)
    print "COACH : %s" %coach
    print "SEAT NO : %s" %seat_no
    print '*' * 50
    
    PNR +=1


def ticket_booking_screen():
    while True:

        print_header()
        global source
        global dest
        global coach
        
        source = raw_input("Enter Source Location : ")
        dest = raw_input("Enter Destination Location : ")
        while True:
            
            coach = raw_input("Enter the choice of coach(ac1/ac2/ac3/s1): ")
            if coach not in VALID_COACHES:
                print "Please Enter Valid Coach only. \n"
            else:
                break
        r_nos = int(raw_input("Enter number of tickets to book : "))
        while True:
            seat_pref = raw_input("Enter if any seat preference L/M/U/N(no preference) : ")
            if seat_pref not in VALID_SEAT_PREF:
                print "Please ENTER valid seat preference only"
            else:
                break
        if seat_pref != 'N':
            seats = get_vacant_seat(coach,r_nos,seat_pref)
            if not seats :#555555555555555555555555555555555555555555555
                print "%s birth not available" %seat_pref
            else:

                reserve_in_db(coach, seat_pref, seats)
                dbss()
                print_tkt(source, dest, coach, seats)
            e= raw_input(' Press (enter) to book another Ticket or (n + enter) to LOG OUT: ')  
            if e=='n': break 

        else:
            seats = get_vacant_seat(coach,r_nos)
            if not seats :
                print "seats are not available"
            else:
                reserve_in_db(coach, 'L', seats)
                dbss()
                print_tkt(source, dest, coach, seats)  
            e= raw_input(' Press (enter) to book another Ticket or (n + enter) to LOG OUT: ')
            if e==n:break  




def dbss():
    import sqlite3
    dbc_in_file = sqlite3.connect('ethans2') #connect to db
    db_cursor = dbc_in_file.cursor()  # create db cursor
    db_cursor.execute("drop table RAILWAY1")   

    
    db_cursor.execute('create table RAILWAY1 (source char(30), dest char(10), PNR int(10), coach BLOB )')



    
    dbc_in_file.execute("insert into RAILWAY1 (source,dest,PNR,coach) values (?, ?, ?,?)",(source,dest,PNR,coach))
    dbc_in_file.commit()
    dbc_in_file.close()

    dbc_in_file = sqlite3.connect('ethans2') #connect to db
    db_cursor = dbc_in_file.cursor()  # create db cursor

    db_cursor.execute("SELECT source,dest,PNR from RAILWAY1")

    print db_cursor.fetchall()
def main():
    print_header()
    choice = first_screen()
    if choice == 1:
        register_user()
    elif choice == 2:
        user_name = input_user_name()
        password = input_password(check=False)
        if verify_password(user_name,password):
            print '\n'
            print "Login Successful"
            ticket_booking_screen()
            


        else:
            print '\n'
            print "User or Password not valid"

    else:
        print '\n'
        print "Please select valid choice"


init_db(42)
if __name__ == '__main__':
	#import pdb ; pdb.set_trace()
	while True:
		print '\n' * 2
		main()
