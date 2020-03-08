import hashlib
from termcolor import colored
hashfile = raw_input("Enter The SHA256 Hash :")
wordlistname = raw_input("Enter Wordlist file name:")

HTBhash = hashfile.strip()
wordlist = open(wordlistname,"r")
wordlistline = ''
wordlistlineencode = ''
while wordlistlineencode != HTBhash:
    wordlistline = wordlist.readline()
    wordlistlineencode = hashlib.sha256(b"%s"%wordlistline.strip()).hexdigest()
    print colored("[password] ==>"+wordlistline,'yellow'),colored("[wrong]","red"),("hash ==>"+wordlistlineencode)

print colored("password is ========>",'red'),colored(wordlistline,'red')
print colored("########################   THANK U :)    ########################",'red')
