import string
import random
import re


def id_generator(passlength):
    chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
    newpassword = ""

    for i in range(passlength):
        nextchar=random.choice(chars)
        newpassword+=nextchar
    return newpassword

def decrypt_credentials():
    pass

def store_credentials(serviceName, userName, password):
    credentials=open("credentials.txt", "a+")
    credentials.write("{0} {1} {2}\n".format(serviceName, userName, password))
    credentials.close
    return
def encrypt_credentials():
    pass

def genstore(serviceName):

    print("Please enter your username/email for that service")
    userName = input()
    print("Please enter desired password length")
    passlength = int(input())

    password = id_generator(passlength)
    decrypt_credentials()
    store_credentials(serviceName, userName, password)
    encrypt_credentials()

    print("Credentials Logged")

    print ("On {0} for username: {1} the new password is {2}.".format(serviceName, userName, password))

    return


def getcredentials(serviceName):
    lines = ""
    with open ('credentials.txt', 'rt') as in_file:  #
        for line in in_file:
            found = re.search(serviceName,line)

            if found != None:
                lines= lines + line
                break
    logincreds = lines.split()
    serviceName = logincreds[0]
    userName = logincreds[1]
    password = logincreds[2]
    print ("For {0} the username is {1} and the password is {2}".format(serviceName, userName, password))
    return

def main():
    print("enter service name")
    serviceName = input()
    print("Press 1 to generate or store password")
    print("Press 2 to return credentials")
    optionchosen=str(input())

    if optionchosen == "1":
        genstore(serviceName)
    elif optionchosen == "2":
        getcredentials(serviceName)
    else:
        print("Option selected does not exist. Start again")
        main()

if __name__ == "__main__":
    main()
