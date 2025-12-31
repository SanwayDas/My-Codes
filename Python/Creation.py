## pyright: reportUndefinedVariable = false         
import math as m                # Library Imports
import numpy as np              # (from math import *)
import sympy as sp
import scipy as sci
import pandas as pa
import random as rd
import statistics as stat
from sympy.abc import x, y, z
import calendar as cal 
from datetime import datetime as dt
import string as strg
from collections import namedtuple
from time import *              # Only sleep is Accessed
import os
import sys

                                # Add/Remove Only One HashFrom Line 1 To Hide/Unhide Undefined_Variable Reports Respectively
BOLD = '\033[1m'                # Text Style Formatters
DIM = '\033[2m'                 # MAKE A FUNCTION SHORTENING THESE (UNSUCESSFUL)
ITALIC = '\033[3m'
UNDERLINE = '\033[4m'
BLINK = '\033[5m'
FAST_BLINK = '\033[6m'
INVERT = '\033[7m'
HIDDEN = '\033[8m'
STRIKETHROUGH = '\033[9m'
DOUBLE_UNDERLINE = '\033[21m'
END = '\033[0m'                 # Resets all formatting

BLACK_DF = '\033[30m'           # Colour Style Formatters
RED_DF = '\033[31m'
GREEN_DF = '\033[32m'
YELLOW_DF = '\033[33m'
BLUE_DF = '\033[34m'
MAGENTA_DF = '\033[35m'
CYAN_DF = '\033[36m'
WHITE_DF = '\033[37m'

BLACK_DB = '\033[40m'
RED_DB = '\033[41m'
GREEN_DB = '\033[42m'
YELLOW_DB = '\033[43m'
BLUE_DB = '\033[44m'
MAGENTA_DB = '\033[45m'
CYAN_DB = '\033[46m'
WHITE_DB = '\033[47m'

BLACK_BF = '\033[90m'
RED_BF = '\033[91m'
GREEN_BF = '\033[92m'
YELLOW_BF = '\033[93m'
BLUE_BF = '\033[94m'
MAGENTA_BF = '\033[95m'
CYAN_BF = '\033[96m'
WHITE_BF = '\033[97m'

BLACK_BB = '\033[100m'
RED_BB = '\033[101m'
GREEN_BB = '\033[102m'
YELLOW_BB = '\033[103m'
BLUE_BB = '\033[104m'
MAGENTA_BB = '\033[105m'
CYAN_BB = '\033[106m'
WHITE_BB = '\033[107m' 


LIST_DISPLAY_TIME = 5               # Literals
ADMIN_LOAD = (10)
LOAD_DISPLAY = (4,4,4)              #               Disable 4 as 1 or 0 while editing to save time (DEFAULT IS (4,4,4)!)
FLAG = True                         # Dummy Flag
PATH = ("& "+sys.executable+" "+os.path.abspath(__file__)).replace("\\","/")      # CHANGE THESE WHENEVER YOU CHANGE THE PROGRAM'S NAME (NOT ANYMORE!)
CD = "D:\\Codes\\Directories"
MESSAGE = ["YOU", "CAN'T", "STOP", "NOW"]
SCREEN_LENGTH = 149
FILE_BORDER_LENGTH = 110            # Change length later to 100ish?
CURRENT_TIME_FILE = lambda dis = True, milli = True : dt.now().strftime(f"On The %d Of %B, %Y, At %I:%M %p.\t (%d.%m.%Y, %H:%M:%S{f":%f" if milli else ""})")
COMING_SOON = lambda : print(END+BOLD+WHITE_BB+BLACK_BF+" COMING SOON! ".center(SCREEN_LENGTH,'*')+END)
ENCRYPTOR = lambda l : " ".join(str(ord(x)) for x in l)
DECRYPTOR = lambda l : "".join(chr(x) for x in l)
PASSWORD = DECRYPTOR([80, 97, 115, 115])                # PASSWORD = [ord(c) for c in "Pass"]  
ADMIN_PASSWORD = DECRYPTOR([72, 101, 108, 108, 111, 32, 87, 111, 114, 108, 100, 33])  
ALL_PASSWORDS = [PASSWORD, ADMIN_PASSWORD]


TEXT_FORMATS=["END","BOLD","DIM","ITALIC","UNDERLINE","BLINK","FAST_BLINK","INVERT","HIDDEN","STRIKETHROUGH"]
TEXT_COLOURS=["BLACK","RED","GREEN","YELLOW","BLUE","MAGENTA","CYAN","WHITE"]
FORMAT_CODES={"":0,"_DF":30,"_DB":40,"_BF":90,"_BB":100}


def ansivars(title:str="TEXT",suffix:str="",start:int=0,conlist : list[str]=TEXT_FORMATS) -> dict :     # A very useless function
    textvar=globals()["".join([title,suffix])]={}
    for code,name in enumerate(conlist): globals()[name+suffix]=textvar[name+suffix]=f'\033[{start+code}m'
    return textvar
    pass
for i,j in FORMAT_CODES.items(): ansivars(title=("TEXT_COLOURS" if i else "TEXT_FORMATS_NAMES"),suffix=i,start=j,conlist=(TEXT_COLOURS if i else TEXT_FORMATS))
# ALL_TEXT_FORMATS=[TEXT_FORMATS_NAMES,TEXT_COLOURS_DF,TEXT_COLOURS_DB,TEXT_COLOURS_BF,TEXT_COLOURS_BB]
# for hard in ALL_TEXT_FORMATS: print(hard)
MAIN_MENU = {           # Change choice 2 to 1.1 1.2 and so on for better keys?
                1:  {"Progression And Series":
                        {
                            1:"Arithmetic Progression (AP)",
                            2:"Geometric Progression (GP)",
                            3:"Harmonic Progression (HP)",
                            4:"Arithmetic-Geometric Progression (AGP)",
                            5:"My Saved Progressions"
                        }
                   
                    },
                2:  {"Matrix Operations":
                        {
                            1:"...",
                            2:"...",
                            3:"...",
                            4:"...",
                            5:"..."
                        }
                    },
                3:  {"Random Number Generator":
                        {
                            1:"Coin Toss",
                            2:"Dice Roll",
                            3:"Rock-Paper-Scissors",
                            4:"Generate Random Series",
                            5:"Randomly Display A Saved Progression"
                        }
                    },
                4:  {"Cryptography":
                        {
                            1:"Pig Latin Encryption",
                            2:"Caesar Ciphers",
                            3:"ASCII Conversions",
                            4:"Number System Conversions",
                            5:"..."
                        }
                    },
                5:  {"My Saves":
                        {
                            1:"My Saved Creations",
                            2:"...",
                            3:"...",
                            4:"...",
                            5:"..."
                        }
                    },
                6:  {"...":
                        {
                            1:"...",
                            2:"...",
                            3:"...",
                            4:"...",
                            5:"..."
                        }
                    },
                7:  {"Admin Settings":
                        {
                            1:"Clock Settings",
                            2:"Abouts",
                            3:"...",
                            4:"...",
                            5:"..."
                        }
                    }
            }


def inp():
    print(f"{ITALIC}{GREEN_BF}\n")
    print(f" MAIN MENU ".center(25,'='))
    for i,j in MAIN_MENU.items():
        if i == len(MAIN_MENU): print(f"{BOLD}{MAGENTA_BF}",end='')
        print(f"{i}. {list(j.keys())[0]}")
        sleep(1/len(MAIN_MENU))
    print(f"{END}{ITALIC}{DIM}{GREEN_DF}(Press 0 To Terminate The Program.){END}")
    choice=int(input(f"{CYAN_BF}Enter Your Choice From The Above: {YELLOW_BF}")) ; print(END,end='')
    return choice , (list(MAIN_MENU[choice].keys())[0] if choice in MAIN_MENU else '')
    pass


def inp1(choice,cname='',bf=GREEN_BF,df=GREEN_DF):
    n=cd=t=0
    cr,choice1=1,''
    loading()
    if list(MAIN_MENU[choice].keys())[0] == list(MAIN_MENU[len(MAIN_MENU)].keys())[0]: bf,df=MAGENTA_BF,MAGENTA_DF
    print(f"{ITALIC}{bf}")
    for i,j in MAIN_MENU[choice].items():
        print(f" {list(MAIN_MENU[choice].keys())[0].upper()} ".center(30,'='))
        #if list(MAIN_MENU[choice].keys())[0] == list(MAIN_MENU[len(MAIN_MENU)].keys())[0]: print(f"{BOLD}{MAGENTA_BF}",end='')
        for i in MAIN_MENU[choice].values():
            for j,k in i.items(): print(f"{j}. {k}") ; sleep(1/len(i))
    print(f"{DIM}{df}(Press 0 To Go Back.){END}")
    choice1=int(input(f"{CYAN_BF}Enter Your Choice From The Above: {YELLOW_BF}")) ; print(END,end='')
    # range(MAIN_MENU[choice][cname])
    if choice1 in range(1,(5 if choice == 1 else (5 if choice == 3 else 1))) :
        sleep(0.75)
        if choice == 1 :
            n=float(input(f"\n{CYAN_BF}Enter The First Number: {YELLOW_BF}"))
            sleep(0.75)
            if choice1 == 1 or choice1 == 3 or choice1 == 4: cd=float(input(f"{CYAN_BF}Enter The Common Difference: {YELLOW_BF}"))
            if choice1 == 4: sleep(0.75)
            if choice1 == 2 or choice1 == 4: cr=float(input(f"{CYAN_BF}Enter The Common Ratio: {YELLOW_BF}"))
            sleep(0.75)
            t=int(input(f"{CYAN_BF}Enter The Number Of Terms: {YELLOW_BF}"))
    elif choice1 == 5:                    # SHIFT THIS TO A NEW SECTION IN MAIN MENU OR ADMIN??
        loading()
        if choice == 1 : dissave(progsaves,'Creation')               # 'Progression'         
        elif choice == 2 : 
            pass #DO SOMETHING!
    elif choice1 == 0:
        print(f"{df}Going Back...{END}")
        loading(t=2)
    elif choice1 not in list(MAIN_MENU[3].values())[0].keys():
        print(f"{RED_DF}Wrong Option! Choose Again!{END}\n")
        return inp1(choice,cname,bf,df)
    # print(choice1)
    return choice1, n, t, choice, cd, cr
    pass


def settings():         # WHAT TO DISPLAY????
    #time duration
    #clock settings
    pass


def piglatin(text,convert=None):            # Cannot Decrypt ATM
    text=list(text.split(" "))
    text1=[]
    for i in text:
        loc=-1
        t=''
        voc=False if i[0] in strg.ascii_lowercase else True
        for j in i:
            if j in "AEIOUaeiou" :
                loc=i.index(j)   
                break 
        if i[-1] in "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ " : t = i[-1]
        new=((i[loc:]+(i[:loc] if loc else "w")+"ay").replace(t,"")+t)
        new=new.title() if voc else new
        text1.append(new) 
    # text=" ".join(text)
    return (" ".join(text1))
    pass


def codenames(choice1:int,choice=3):
    convert, confirm = True, False
    if choice1 != 1 :               # convert = True when Encryption(original to code) and False when Decryption(code to original)
        if not yesorno(message=f"{BLUE_DF}Encryption{CYAN_BF} Or {GREEN_DF}Decryption",choices={"E":"Encryption", "D": "Decryption"}) : convert = False
    sleep(1)
    while not confirm : 
        if choice1 == 3 and not convert :
            sleep(1)
            sep=input(f"{CYAN_BF}Enter A Separator For Your Integer Inputs: {YELLOW_BF}").strip() ; print(END,end='')
            if not sep : print(f"{RED_DF}Converting To Default Whitespace Separator!\n{END}") ; sep = " "
            while True :
                try : float(sep) ; print(f"{RED_DF}Please Enter Non-Integer Separators!\n{END}")
                except ValueError : break
            loading(t=2)
        text=input(f"{CYAN_BF}Enter The Text To {(typ := f"{BLUE_DF}Encrypt" if convert else f"{GREEN_DF}Decrypt")} {CYAN_BF}: {BOLD}{UNDERLINE}{YELLOW_BF}\n") ; print(END)
        sleep(1.5)
        print(f"{GREEN_DF}The Inputted Text Is \"{BOLD}{UNDERLINE}{CYAN_BF}{text}{END}{GREEN_DF}\"{f" With \"{BOLD}{UNDERLINE}{CYAN_BF}{sep}{END}{GREEN_DF}\" As The Assigned Separator" if choice1 == 3 and not convert else ""}.\n")
        sleep(1.5)
        if choice1 == 3 and not convert :
            try : text = map(int, text.split(sep))
            except ValueError : 
                print(f"{RED_DF}Non-Integer Characters Cannot Be Converted In This Method!\n{typ}ion {RED_DF}Cancelled!{END}") 
                loading(t=1)
                return codenames(choice1,choice)
        if yesorno(f"Can You Confirm For Conversion") : print(f"{MAGENTA_BF}\nExecuting {UNDERLINE}{typ}ion{END} {MAGENTA_BF}...\n{END}") ; confirm = True
        else : print(f"{RED_DF}\nThen Please Re-Enter Your Inputted Text!\n{END}") ; sleep(1)
    textmod = ''
    if choice1 == 1 : textmod = piglatin(text) ; print(f"{YELLOW_DF}The Given Text Converted In Simple {UNDERLINE}{GREEN_DF}Pig Latin{END}{YELLOW_DF} Is: {END}")
    elif choice1 == 2 : pass
    elif choice1 == 3 : textmod = ENCRYPTOR(text) if convert else DECRYPTOR(text)
    elif choice1 == 4 : pass
    loading()
    # hacking = any(textmod == password or text == password for password in ALL_PASSWORDS)
    print(f"{GREEN_DF}Output: {BOLD+UNDERLINE}{(CYAN_BF+textmod) if not (hacking := any(textmod == password or text == password for password in ALL_PASSWORDS)) else (STRIKETHROUGH+RED_BF+"REDACTED")}{END}{GREEN_DF} .",flush=True)
    sleep(1)
    if hacking : 
        print(f"{RED_BF}I Know What You Are Trying To Do!") 
        # ENTER A FILE HANDLED WARNING HERE! (done!)
        savetxt.writelines(f"\t\tLOG RECORD : Input Text {"Encryption" if convert else "Decryption"} Rejected While Attempting To Hack Access In Passwords Database! \n\t\t\t\t->\t{CURRENT_TIME_FILE()}\n\n")
        sleep(1)
    pass


def rantoss(choice1,choice=3,p=None):
    if p == None :
        term=''
        ll=ul=0
        if choice1 == 1: 
            term="Coin Tosses"
            ll=0
            ul=1
        elif choice1 == 2 : 
            term="Die Rolls"
            ll=1
            ul=6
        t=int(input(f"{CYAN_BF}Enter The Number Of {term}: {YELLOW_BF}"))
    else:
        ll=ul=t=H=T=n=0
        die=DIEp={1:0,2:0,3:0,4:0,5:0,6:0}
        colour={1:RED_DF,2:GREEN_DF,3:YELLOW_DF,4:BLUE_DF,5:MAGENTA_DF,6:CYAN_DF}
        sleep(2)
        if (n := len(p)) != 0 :             # ADJUSTMENTS??
            if choice1 == 4 : return ll,ul,t,choice,0,1,choice1
            if choice1 == 1 : 
                if yesorno(f"\n{"Is The Coin" if n == 1 else "Are The Coins"} {RED_DF}Biased{CYAN_BF} Or {GREEN_DF}Unbiased"): pass
                H = p.count("Heads")
                T = p.count("Tails")
                print(f"\n\n{MAGENTA_BF}A Simultaneous Tossing Of {YELLOW_BF}{n}{MAGENTA_BF} Coins Have Resulted In {UNDERLINE}{CYAN_DF}{H}{END} {YELLOW_BF}\"Heads\"{MAGENTA_BF} And {UNDERLINE}{CYAN_DF}{T}{END} {GREEN_BF}\"Tails\"{MAGENTA_BF} .{END}")
            elif choice1 == 2 :
                for i in p: die[i] = p.count(i)
                print(f"\n{MAGENTA_BF}A Simultaneous Tossing Of {YELLOW_BF}{n}{MAGENTA_BF} Di{"e" if len(p) == 1 else "ce"} Have Resulted In:\n{END}")
                for l in range(1,len(die)+1):
                    print(f"{UNDERLINE}{MAGENTA_BF}{die[l]}{END}",end='')
                    print(f"{colour[l]}\" {l}{"\'s" if die[l] != 1 else ""} \"".center(20,' '))
                    sleep(0.5)
        sleep(2)                            # change Heads and Tails Colour codes! done!
        try:
            Hp=(H/n)*100
            Tp=(T/n)*100 
            for l in range(1,7): DIEp[l] = (die[l]/n)*100
        except ZeroDivisionError as e: DIEp=Hp=Tp=0
        if choice1 == 1 : print(f"\n\n{MAGENTA_BF}Out Of {YELLOW_BF}{n}{MAGENTA_BF} Coin Tosses, {UNDERLINE}{CYAN_DF}{Hp:5f}%{END}{MAGENTA_BF} Of Tosses Were {YELLOW_BF}\"Heads\"{MAGENTA_BF} And {UNDERLINE}{CYAN_DF}{Tp:5f}%{END}{MAGENTA_BF} Of Tosses Were {GREEN_BF}\"Tails\"{MAGENTA_BF} .{END}")
        elif choice1 == 2 :                             # {UNDERLINE}{CYAN_DF}{n}{END}{MAGENTA_BF}
            print(f"\n\n{MAGENTA_BF}Out Of {YELLOW_BF}{n}{MAGENTA_BF} Di{"e" if len(p) == 1 else "ce"} Rolls:\n{END}")
            for l in range(1,len(die)+1): 
                print(f"{UNDERLINE}{CYAN_DF}{DIEp[l]:5f}%{END}{MAGENTA_BF} Of Rolls Were {YELLOW_BF}{colour[l]}{l}\'{"\'s" if die[l] != 1 else ""} \"")
                sleep(0.5)
        print()         # Ending Line
    return ll,ul,t,choice,0,1,choice1   #def listmaker(r,n,t,choice,cd=0,cr=1,r3=''):
    pass


def rangame(choice1,choice=3,games=0,reweights={"Y":1,"N":1},RPSweights={"Rock": 1, "Paper": 1, "Scissors": 1}):
    myc=yourc=''
    correct=0
    counts={}
    clist=["Rock","Paper","Scissors"]
    winrules={"Rock": "Scissors","Paper": "Rock","Scissors": "Paper"}       # 1st vs 2nd will make 1st win
    RPScolour={"Rock": RED_BF,"Paper": GREEN_BF,"Scissors": BLUE_BF}
    loading(t=2)
    while "Stop" not in yourc.title() :                        # PROM(STOP)
        # for i,j in enumerate(clist,start=1): print(f"{ITALIC}{GREEN_BF}{i}. {j}{END}")
        while correct != 1 :
            print()
            listdis(clist,"no RPS",(0.5*3))
            sleep(0.5)
            print(f"{END}{ITALIC}{DIM}{GREEN_DF}(Type \"STOP\" Or \"0\" To Stop Playing.)\n{END}")
            sleep(0.5)
            yourc=input(f"\n{CYAN_BF}Make Your Choice: {YELLOW_BF}").title().replace(" ","") ; print(END,end='')        # User Choice  (.split()[0] for 1st one only)
            try:
                yourc = int(yourc)-1
                # print(yourc)
                if -1 < yourc < len(clist) : yourc=clist[yourc]
                elif yourc == -1 : yourc = "Stop" ; break
                else : 
                    print(f"{RED_DF}Enter Value Out Of The Selected Range Of Options!{END}")
                    return rangame(choice1,choice,games,reweights,RPSweights)
            except ValueError: yourc = str(yourc)           # pass
            counts={word : (yourc.lower()).count(word.lower()) for word in clist} ; correct=sum(counts.values())
            # print(counts,correct)       # cut it off later
            sleep(1)
            if not correct : print(f"{RED_DF}That Is Not A Valid Choice In This Game!{END}")
            elif correct > 1 : 
                maxc = [k for k , v in counts.items() if v == (maxima := max(counts.values()))]
                print(f"{GREEN_DF}You Gave: ")
                for l in maxc : 
                    # print(maxc,l,maxc[l],maxima)
                    print(f"{UNDERLINE}{CYAN_DF}{maxima}{END}{CYAN_DF}\t->\t{RPScolour[l]}\"{l}\"")
                    sleep(0.5)
                if len(maxc) == 1 :
                    if yesorno(f"As {RPScolour[maxc[0]]}{maxc[0]}{CYAN_BF} Is The Single Highest Occurence, Being {YELLOW_BF}{maxima}{CYAN_BF} Times, Did You Mean To Input {RPScolour[maxc[0]]}{maxc[0]}{CYAN_BF} As Your Choice") : 
                        yourc=maxc[0].title()
                        correct = 1
                        print(f"{BLUE_DF}Finally...",end=' ')
                    else : 
                        print(f"{RED_DF}Then Choose Some Valid Choice, Please!\nYou Are Confusing Everything.")
                        sleep(1)
                        print(f"{RED_DF}Who Will Understand If You Input {" And ".join(maxc)} Altogether, That Too With Exactly {maxima} Occurence{"s" if maxima > 1 else ""} For Each??")
                else : print(f"{RED_DF}This Is All Messy! Make Up Your Mind!{END}")
        # print(yourc)
        print(f"{BLUE_DF}You Chose {(yourcol := UNDERLINE+RPScolour[yourc]+yourc+END)}{BLUE_DF} .")
        myc=rd.choices(population=clist,weights=list(RPSweights.values()),k=1)[0]         # Computer Choice
        print(f"{GREEN_DF}I Choose {(mycol := UNDERLINE+RPScolour[myc]+myc+END)}{GREEN_DF} !")
        print(f"{yourcol} {YELLOW_BF}VS {mycol}{YELLOW_BF} ...")
        loading(t=1)
        if winrules[yourc] == myc : print(f"{GREEN_DF}You Win As {yourcol}{GREEN_DF}!") ; reweights["Y"] += 1
        elif winrules[myc] == yourc : print(f"{GREEN_DF}I Win As {mycol}{GREEN_DF}!") ; reweights["N"] += 1
        elif myc == yourc : print(f"{GREEN_DF}We End In A Draw With {yourcol}{GREEN_DF} VS {mycol}{GREEN_BF}!")
        sleep(1)
        print()
        games += 1
        reproc=rd.choices(population=["Y","N"],weights=list(reweights.values()),k=1)[0]            # More Chance To Replay If YOU Win
        if reproc == "Y" : 
            print(f"{GREEN_DF}Let Us Have A Rematch!")
            return rangame(choice1,choice,games,reweights,RPSweights)
        elif reproc == "N" : 
            if yesorno("Do You Want A Rematch") : 
                print(f"{GREEN_DF} Alright! Another Rematch!")
                return rangame(choice1,choice,games,reweights,RPSweights)
            else : 
                print(f"{GREEN_DF}Okay! Exiting The Game Then...")
                yourc = "Stop"
    print(f"{GREEN_DF}Terminating The Game...{END}")
    pass


def rangen(choice1,choice=3):
    fi=''
    if choice1 == 4 :
        ll=float(input(f"\n{CYAN_BF}Enter The Lower Limit: {YELLOW_BF}"))        # float?
        sleep(0.75)
        ul=float(input(f"{CYAN_BF}Enter The Upper Limit: {YELLOW_BF}"))          # float?
        sleep(0.75)
        n=int(input(f"{CYAN_BF}Enter The Number Of Terms: {YELLOW_BF}"))
    if n and (ll != ul) : #(ll or ul)
        if yesorno(f"Generate {UNDERLINE}{ITALIC}{MAGENTA_BF}Float{END}{CYAN_BF} Numbers Or {UNDERLINE}{ITALIC}{MAGENTA_BF}Integer{END}{CYAN_BF} Numbers",choices={"F":"Float","I":"Int"}): fi="Float"
        else: fi,ll,ul="Int",int(ll),int(ul)
        print(f"{GREEN_DF}Generating {YELLOW_BF}{n}{GREEN_DF} Random Number{"s" if n else ""} From {YELLOW_BF}{ll}{GREEN_DF} To {YELLOW_BF}{ul}{GREEN_DF} In {UNDERLINE}{ITALIC}{MAGENTA_BF}<{fi}>{END}{GREEN_DF} ...{END}")
    return ll,ul,n,choice,(1 if fi=="Float" else (0 if fi=="Int" else 0)),1,choice1
    pass


def listmaker(choice1,n,t:int,choice,cd=0,cr=1,r3=''): #return ll,ul,t,choice,(1 if fi=="Float" else (0 if fi=="Int" else 0))
    p=[]
    text=" "
    if t < 0 :
        sleep(1)
        print(f"{RED_DF}\nIt Is Not Possible To Display A Negative Number Of Terms!{END}")
        if yesorno(f"Do You Want To Display {YELLOW_BF}{-1*t}{CYAN_BF} Terms Instead") : t = abs(t)
        else : 
            loading(t=1)
            t = int(input(f"{CYAN_BF}Please Enter The Number Of Terms (In Positive Value): {YELLOW_BF}"))
            return listmaker(choice1,n,t,choice,cd,cr,r3)
    for i in range(t):
        if choice == 1 :
            if choice1 == 1:
                text="Arithmetic"
                p.append(n+(cd*i))
            elif choice1 == 2:
                text="Geometric"
                p.append(n*(cr**i))
            elif choice1 == 3:
                text="Harmonic"
                p.append(1/(n+(cd*i)))
            elif choice1 == 4:
                text="Arithmetic-Geometric"
                p.append((n+(cd*i))*(cr**i))
            elif choice1 == 0: break
        elif choice == 3 :
            if cd == 0 : 
                if int(r3) == 1: 
                    coin=["Heads","Tails"]
                    p.append(rd.choices(coin)[0])
                    text="List Of Coin Tosses"
                elif int(r3) in [2,4]: 
                    p.append(rd.randrange(int(choice1),int(n+1),cr))
                    if int(r3) == 2 : text="List Of Dice Rolls"
            elif cd == 1 : p.append(rd.uniform(choice1,n))
            if int(r3) == 4 : text="Randomly Generated List"
            '''len(set(p)) to finding number of different entries'''
    return p,(r3 if choice==3 else choice1),("Empty List" if t == 0 else ("Homogeneous "+text if all(ele==p[0] for ele in p) else (text if choice==3 else (text+" Progression")))),choice1,n       #choice1 is (4 if choice==3 else choice1)
    pass


def listdis(p,text='',t=LIST_DISPLAY_TIME):
    colour={1:RED_DF,2:GREEN_DF,3:YELLOW_DF,4:BLUE_DF,5:MAGENTA_DF,6:CYAN_DF}
    HTcolour={"Heads" : YELLOW_BF, "Tails" : GREEN_BF}
    RPScolour={"Rock": RED_BF,"Paper": GREEN_BF,"Scissors": BLUE_BF}
    if "Empty List" not in text :
        if 'no' not in text.lower(): loading()
        else: 
            if 'RPS' not in text.upper(): sleep(1)
        if text != '' and 'no' not in text.lower() : print(f"{GREEN_DF}The Created {text} Is:{END}\n")
        for ii, i in enumerate(p,start=1):
            sleep(t/len(p))
            print(f"{ITALIC}{BLUE_DF}{ii}.\t {END}",end='')
            if type(i) == str: print(f"{HTcolour[i] if i in HTcolour else(RPScolour[i] if i in RPScolour else WHITE_BF)}{BLACK_DB} {i:s} {END}".strip().center((5 if i in RPScolour else 20),' '))
            #elif type(i) == int: print(f"{WHITE_BF}{BLACK_DB}{i:d}{END}".center(20,' '))   # maybe add for ints as well??
            else: 
                if text == "List Of Dice Rolls" : print(f"{colour[i]}{BLACK_DB}{i:d}{END}".center(20,' '))
                else: print(f"{WHITE_BF}{BLACK_DB}{i:f}{END}".center(20,' '))
        if "Homogeneous" in text : print(f"{RED_DF}All The Terms In The Created List Are {YELLOW_BF}\"{p[0]}\"{RED_DF} !{END}")
    else: sleep(1) ; print(f"{RED_DF}There Are No Terms In The List Since You Entered {YELLOW_BF}\"0\"{RED_DF} Number Of Terms.{END}")
    pass


def listcalc(p,text='',ll=0,ul=0):
    s=n=am=em=var=random=None
    if "Randomly Generated List" in text or "List Of Dice Rolls" in text : random = True
    CALCULATIONS =  {          # IMPROVE THIS!      (ADD EXPECTANCY BEFORE EXPECTED MEAN)
                        "Summation" : (s := (sum(p)) if (n := len(p)) else "Not Defined"), 
                        "Arithmetic Mean" : (am := (s/n) if n else "Not Defined"), 
                        "Expected Mean" : (em := ((ll + ul)/2) if random else "Not Defined"), 
                        "Variance" : (var := ((ul - ll)**2/12) if random else "Not Defined"),
                        "Standard Deviation" : (sd := (m.sqrt(var)) if random else "Not Defined") 
                    }
    sleep(2)
    if "Homogeneous" in text and not(pivot := int(p[0])): print(f"\n{ITALIC}{DIM}{MAGENTA_BF}Since All Elements In The List Are {pivot}{"" if pivot else "(Zero)"}, All Calculations Will Lead To {pivot}{"" if pivot else "(Zero)"} As Well.{END}") ; text = "Homogeneous Empty List"
    elif "Empty" not in text :
        for calc,value in CALCULATIONS.items():
            if value != "Not Defined" : sleep(2) ; print(f"\n\n{MAGENTA_BF}The {UNDERLINE+MAGENTA_DF+calc+END+MAGENTA_BF} Of {"All"if n!=1 else"Only"} {YELLOW_BF}{n}{MAGENTA_BF} Term{'s'if n!=1 else''} In The {text} Is: {UNDERLINE}{CYAN_DF}{value:f}{END}")
    else: print(f"\n{ITALIC}{DIM}{MAGENTA_BF}{"Also, " if not any(p) else ""}No Calculations Could Be Formed On Empty Lists.{END}")
    print()         # Ending Line
    return CALCULATIONS
    pass


def saviour(saves,calc,p,t):
    if t == "Empty List" : return saves         # should we disable saving empty lists??
    if yesorno(f"Do You Want To Save This {t}"): 
        savename=input(f"{CYAN_BF}Name Your Saved List: {YELLOW_BF}") ; print(END,end='')       # List or t ?
        saves[savename]=p
        savetxt.writelines(f"{len(saves)}. {savename}: \t{p}\n")
        savetxt.writelines(f"\tAll Calculations: \t{calc}\n\n")
        loading(t=2)
        print(f"{BLUE_BF}Your Created {t} Has Been Saved As {YELLOW_BF}\"{savename}\"{BLUE_BF} !{END}")
        sleep(0.5)
        return saves
    else: print(f"{RED_DF}{t} Remains Unsaved!{END}") ; return saves
    pass


def dissave(saves,t):           #add a loop?
    l=len(saves)
    print(f"{BLUE_BF}You Have Saved {UNDERLINE}{CYAN_DF}{l}{END} {BLUE_BF}{t}{'s' if l != 1 else ''}.{END}\n")
    if l != 0 :
        sleep(1)
        for ii, i in enumerate(saves,start=1):
            sleep(2/len(saves))
            print(f"{ITALIC}{MAGENTA_DF}{ii}.\t{END}",end='')
            print(f"{YELLOW_DF}{BLACK_DB}{i}{END}".center(20,' '))
        sleep(2/len(saves))
        print(f"{CYAN_BF}Enter The Serial Number Or The Name To Display The Entire {t}: ")
        print(f"{ITALIC}{DIM}{CYAN_DF}(Or Type {YELLOW_BF}\"ALL\"{CYAN_DF} To Display All Saved {t}s.){END}")
        r=input(f"{ITALIC}{DIM}{CYAN_DF}(Or Type {YELLOW_BF}\"RANDOM\"{CYAN_DF} To Randomly Display Saved {t}s.){END}{YELLOW_BF}\n") ; print(END,end='')
        try:
            r=int(r)
            if r in range(1,l+1): 
                savelist=list(saves.values())
                print(f"{BLUE_BF}The Saved {t} Of Serial Number {YELLOW_BF}\"{r}\"{BLUE_BF} Is :\n")    #mention name in brackets??
                listdis(savelist[r-1],'no')
            else : print(f"{RED_DF}Serial Number {YELLOW_BF}\"{r}\"{RED_DF} Is Out Of Range!{END}")
        except ValueError:     #Problem here
            if r in saves: 
                print(f"{BLUE_BF}The Saved {t} Of Name {YELLOW_BF}\"{r}\"{BLUE_BF} Is :\n")
                listdis(saves[r],'no')
            elif 'all' in r.lower():
                print(f"{BLUE_BF}Printing {BOLD}{UNDERLINE}All{END}{BLUE_BF} Saved {t}s...{END}")           #"\n"
                loading()
                print()
                for ii, i in enumerate(saves,start=1):
                    sleep(1)
                    print(f"{ITALIC}{MAGENTA_DF}{ii}.\t{END}",end='')
                    print(f"{YELLOW_DF}{BLACK_DB}{i}{END}".center(20,' '),end='')
                    print(f"{BLUE_DF}\t->\n{END}")
                    listdis(saves[i],'no')               #for j in saves[i]: print(f"{j:f}".center(20,' '))
                    print()
            elif 'random' in r.lower():
                n=int(input(f"{CYAN_BF}Enter The Number Of {t}s To Display Randomly From The List: {YELLOW_BF}"))
                if n > l : print(f"{RED_DF}There {"Are" if l else "Is"} Only {UNDERLINE}\"{l}\"{END}{RED_DF} Saved {t}s In The Database!{END}")
                else:
                    if n == l : print(f"{BLUE_BF}Printing {BOLD}{UNDERLINE}All{END}{BLUE_BF} Saved {t}s...\n{RED_DF}In A Random Order!{END}")
                    else : print(f"{BLUE_BF}Printing {BOLD}{UNDERLINE}{n}{END}{BLUE_BF} Randomly Saved {t}s...{END}")
                    for ii, i in enumerate(rd.sample(list(saves),n),start=1) : 
                        sleep(1)
                        print(f"{ITALIC}{MAGENTA_DF}{ii}.\t{END}",end='')
                        print(f"{YELLOW_DF}{BLACK_DB}{i}{END}".center(20,' '),end='')
                        print(f"{BLUE_DF}\t->\n{END}")
                        listdis(saves[i],'no')               #for j in saves[i]: print(f"{j:f}".center(20,' '))
                        print()
            else : print(f"{RED_DF}There Is No Saved {t} Named {YELLOW_BF}\"{r}\"{RED_DF} In The Database!{END}")
    pass


def yesorno(message=None,restime=2,choices={("Y"):"Yes",("N"):"No"},resmod=YELLOW_BF,askmod=CYAN_BF):  # MESSAGE SHOULD BE BETWEEN CYAN_BF RED_DF WITH NO SPACES AMD NO QUESTION MARK
    sleep(restime)                                                                  # UPPERCASE INITIALS                 
    res=input(f"{askmod}{message}{RED_DF}?\n{resmod}") ; print(END,end='')
    n=iter(choices.keys())
    '''c1,c2=next(n),next(n)
    if any(i in res.upper() for i.upper() in c1) or res == "1": return True
    elif any(i in res.upper() for i.upper() in c2) or res == "0": return False'''
    if (c1 := next(n)) in res.upper() or res == "1": return True           # (c1 := list(choices.keys())[0])
    elif (c2 := next(n)) in res.upper() or res == "0": return False        # (c2 := list(choices.keys())[1])
    else:
        if "?" in res: print(f"{ITALIC}{DIM}{RED_DF}Your Response Must Include A {YELLOW_BF}\"{c1}/{c1.lower()}/1\"{RED_DF} For A {YELLOW_BF}\"{choices[c1]}\"{RED_DF} Or A {YELLOW_BF}\"{c2}/{c2.lower()}/0\"{RED_DF} For A {YELLOW_BF}\"{choices[c2]}\"{RED_DF}.{END}")
        elif "!" in res: print(f"{ITALIC}{DIM}{RED_DF}Your Response Must Include A {YELLOW_BF}\"{c1}/{c1.lower()}/1\"{RED_DF} For A {YELLOW_BF}\"{choices[c1]}\"{RED_DF} Or A {YELLOW_BF}\"{c2}/{c2.lower()}/0\"{RED_DF} For A {YELLOW_BF}\"{choices[c2]}\"{RED_DF}.{END}")     # INCLUDE SOMETHING HERE
        elif PATH in res: scare()           # number of errors in "!"
        else: print(f"{RED_DF}Please Respond In {YELLOW_BF}\"{choices[c1]}\"{RED_DF} Or {YELLOW_BF}\"{choices[c2]}\"{RED_DF}.{END}")
        return yesorno(message,restime,choices,resmod)
    pass


def scare(message=MESSAGE,time=5):
    savetxt.writelines(f"\t\tLOG RECORD : Unsuccessfully Tried Reopening Terminal While Program Is Running! \n\t\t\t\t->\t{CURRENT_TIME_FILE()}\n\n")
    print(f"{BOLD}{RED_BF}")
    for l in message:
        sleep(time/len(message))
        print(f"{l}".center(SCREEN_LENGTH," "))
    print(END,end='') ; sleep(2)
    pass


def locked(key='',type="Password",keycolour=UNDERLINE+BLUE_DF):
    k= PATH if key == '' else ''
    i,j,xcase=1,1,False
    while k != key:
        if i % 3 == 0 and xcase == False or "?" in k or "hint" in k :
            sleep(1.5)
            print(f"{RED_DF}{ITALIC}{DIM}Hint: The {UNDERLINE}{MAGENTA_DF}<ASCII> {END}{ITALIC}{DIM}{RED_DF}Conversion Of The Password Is ->{END}\t{UNDERLINE}{DIM}{CYAN_DF}{ENCRYPTOR(key)}{END}\n") ; sleep(1)
            # for t in key: print(ord(t),end=' ')               # chr(t) for decryption                          
        sleep(0.75)
        if k != PATH : k=input(f"{CYAN_BF}\nEnter The {type}{" In The Correct Cases" if xcase else ""}: {keycolour}") ; print(END,end='')
        if k.lower() == key.lower():
            if k == key: 
                print(f"{GREEN_BF}Correct {type}{" This Time" if xcase else ""}!{END}")            # After i+j-1 incorrect guesses
                if "Admin" in type : savetxt.writelines(f"\t\tLOG RECORD : Successfully Opened Administrative Settings In The Program Terminal After {"A Single Attempt!" if (err := i+j-1) == 1 else f"\"{err}\" Attempts!"} \n\t\t\t\t->\t{CURRENT_TIME_FILE()}\n\n")
            else: 
                print(f"{RED_DF}The {type} Is Case-Sensitive. Please Try Again.{END}")
                j+=1
                xcase=True
        elif k == PATH : terminator(type)
        else: 
            print(f"{RED_DF}Wrong {type}! Please Try Again!{END}\n")
            i+=1
            xcase=False
        if "sanway" in k.lower() or "respector" in k.lower() : sleep(1) ; print(f"{RED_DF}Entering The Creator's Name Does Not Grant Admin Access!{END}\n")
        if key != PASSWORD and k.lower() in [p.lower() for p in ALL_PASSWORDS if p != key]:
            sleep(1)
            if k == PASSWORD : print(f"{RED_DF}Of Course The {type} Would Not Have The Same Password As Before!{END}\n")
            else : print(f"{RED_DF}Even This Wrong Password Is Not In The Correct Case...{END}\n")
    sleep(1)
    print(f"{GREEN_DF}Entering...{END}")
    loading(type=type)
    pass


def loading(type= '', dots=LOAD_DISPLAY[0], loop=LOAD_DISPLAY[1], t=LOAD_DISPLAY[2],style=GREEN_DF):      # Decoration
    if "Quick" in type : t=1                # dots=LOAD_DISPLAY[0], loop=LOAD_DISPLAY[1], t=LOAD_DISPLAY[2]
    if "Password" in type:
        for i in range(100):
            print(BOLD+ITALIC+(BLUE_BF if "Admin" in type else style)+str(i+1),"%...",end="\r",flush=True)      # Add Multicolours??!?!!
            sleep((rd.choices(population=[i+1 for i in range(ADMIN_LOAD)],weights=[min(i + 1, ADMIN_LOAD - i) for i in range(ADMIN_LOAD)])[0])/100)
        sleep(0.5)
        print(f"\nDone!{END}",end='')
    else:
        for i in range(loop):
            for j in range(1,dots+1):                                               # USE \r FOR CARRIAGE RETURN
                    print(YELLOW_DF+". "*j,"  "*(dots-j),end="\r",flush=True)       # flush has no visible effects yet
                    sleep((t/dots)/loop)
    print(END)
    pass


def greetcard(username,dialogues,mode=None):
    gcard=[]
    names=[]
    #if any(i in username.title() for j in dialogues for i in j) : 
    for j in dialogues:
        for i in j: 
            if i in username.title(): 
                names.append("/".join(j))
                gcard.append(dialogues[j])
                break
    if 'set' in str(mode).lower(): return set(gcard) , set(" & ".join(names))
    else: return gcard, " & ".join(names)
    pass


def greet():
    dialogues = {
                 ("Sanway","Respector") : "Welcome Back, Creator." ,
                 ("Saikat","Krrish") : "Thanks For Actually Giving Your Name Correctly This Time, Krrish!" ,
                 ("Sriya","Pagli Buri") : "Ayyyyy Pagli Buri!" ,
                 ("Test","Trial") : "Testing Tuples...",
                 ("Username","User") : "How Original...",
                 ("Administrator","Admin") : "We Will See If You Really Are One."
                }                               # Maybe Merge Keys For Same Values ?
    flag, name = False, ''
    username = input(f"{CYAN_BF}\nWhat Is Your Name, User{RED_DF}?\n{BOLD}{UNDERLINE}{BLUE_BF}") ; print(END,end='\n')
    if any(i in username.title() for j in dialogues for i in j) : 
        card , name = greetcard(username,dialogues)
        for i in card: 
            sleep(1/len(card))
            print(f"{ITALIC}{BLUE_BF}{i}{END}")
        '''for j in dialogues:
            for i in j: 
                if i in username.title(): 
                    print(f"{ITALIC}{BLUE_BF}{dialogues[j]}{END}")
                    break'''
    elif username == PATH : locked(key='')        # to terminate with a specific dialogue
    elif username == '': print(f"{BLUE_DF}No Name Then?\nAlright Then, User.{END}")
    elif "?" in username:
        print(f"\n{ITALIC}{DIM}{RED_DF}Your Name Will Be Recorded In The Text File Of Saved Creations.{END}\n")     #Or Mention the path termination as well?
        sleep(2)
        return greet()
    else: 
        if yesorno(f"\nAre You Sure You Want To Save Your Name As {YELLOW_BF}\"{username}\"",restime=0.5): print(f"{BLUE_DF}Greetings, {username}!{END}")
        else:                       # resmod=BOLD+UNDERLINE+BLUE_BF?
            print(f"{RED_DF}Alright! Previous Name Discarded!{END}")
            sleep(1)
            return greet()
    return ("Anonymous" if username == '' else (username+f"\t\t({name})" if name != '' else username))
    pass


def terminator(loc=None):
    if loc == "Admin Password" : 
        print(f"{BOLD}{RED_DF}Only Admins And Permitted Developers Can Have Access!{END}")
        savetxt.writelines(f"\t\tLOG RECORD : Program Terminated While Attempting To Enter Admin Settings! \n\t\t\t\t->\t{CURRENT_TIME_FILE()}\n\n")
    if loc == "Password" : print(f"{BOLD}{RED_DF}You Left Before The Program Has Even Started!{END}")       # add more?
    else:
        savetxt.writelines(f"\n\tTotal Creations Saved: \t{len(progsaves)}\n\n")
        savetxt.writelines(f"\n\t\tEXIT\t->\t{CURRENT_TIME_FILE()}\n") 
        savetxt.writelines(f"="*FILE_BORDER_LENGTH)
        savetxt.writelines(f"\n"*5) 
        savetxt.close()
    if loc != "MAIN" : print(f"{BOLD}{RED_DF}Signing Out...{END}{END} \n")
    loading(type="Quick")
    print(f"{BOLD}{RED_DF}Program Terminated!!{END}")
    sys.exit(0)              #or os._exit()
    pass


#--------------------------------------------------------------------------
# (Testing Area)
'''sleep(2)        # {UNDERLINE+next(CALC)+END+MAGENTA_BF}
    if text != "Empty List":
        s,n=sum(p),len(p)
        print(f"\n\n{MAGENTA_BF}The {UNDERLINE}Summation{END}{MAGENTA_BF} Of {"All"if n!=1 else"Only"} {YELLOW_BF}{n}{MAGENTA_BF} Term{'s'if n!=1 else''} In The {text} Is: {UNDERLINE}{CYAN_DF}{s:f}{END}")
        if text == "Randomly Generated List" or text == "List Of Dice Rolls" :
            sleep(2)
            em=(ll + ul)/2
            print(f"\n\n{MAGENTA_BF}The {UNDERLINE}Expected Mean{END}{MAGENTA_BF} Of {"All"if n!=1 else"Only"} {YELLOW_BF}{n}{MAGENTA_BF} Term{'s'if n!=1 else''} In The {text} Is: {UNDERLINE}{CYAN_DF}{em:f}{END}")
            sleep(2)
            var=(ul - ll)**2/12             # SHIFT THIS SOMEWHERE
            print(f"\n\n{MAGENTA_BF}The {UNDERLINE}Variance{END}{MAGENTA_BF} Of {"All"if n!=1 else"Only"} {YELLOW_BF}{n}{MAGENTA_BF} Term{'s'if n!=1 else''} In The {text} Is: {UNDERLINE}{CYAN_DF}{var:f}{END}")
        sleep(2)
        try: am=s/n
        except ZeroDivisionError as e: am=0
        print(f"\n\n{MAGENTA_BF}The {UNDERLINE}Arithmetic Mean{END}{MAGENTA_BF} Of {"All"if n!=1 else"Only"} {YELLOW_BF}{n}{MAGENTA_BF} Term{'s'if n!=1 else''} In The {text} Is: {UNDERLINE}{CYAN_DF}{am:f}{END}")
        print()         # Ending Line
        # results=[s,em,var,am]
    else: sleep(2) ; print(f"\n{ITALIC}{DIM}{MAGENTA_BF}No Calculations Could Be Formed On Empty Lists.{END}")'''
#--------------------------------------------------------------------------




#MAIN PROGRAM
try: os.chdir(CD)
except FileNotFoundError as o: print(f"{ITALIC}{DIM}{BLACK_DF} A Little Gift For You :){END}")
locked(key=PASSWORD,type="Password")
progsaves={}                                                ## ADD A DIALOG FOR PERMA-SAVE PERMISSIONS
savetxt=open("Saved_Creations.txt","a+")                    # was originally "w" for deleting after every entry
print(f"{BOLD}{RED_BF}\n WELCOME TO MY PROGRAM!{END}")      # ADD TIME CALENDAR AND SAVE
sleep(1)
savetxt.writelines(f"="*FILE_BORDER_LENGTH)
savetxt.writelines(f"\n\t\tENTRY\t->\t{CURRENT_TIME_FILE()}\n") 
savetxt.writelines(f"By {(greet())} \n") 
sleep(1)         #or just user?
while FLAG is True:
    try:
        cname=choice=choice1=''
        choice,cname=inp()
        if choice == 1 :        
            #choice1 = ''
            while choice1 != 0:
                p,choice1,text=listmaker(*inp1(choice,cname))[:3]
                #if choice1 in MAIN_MENU[choice][cname]:
                if choice1 in range(1,5):
                    listdis(p,text)
                    calc=listcalc(p,text)
                    progsaves=saviour(progsaves,calc,p,text)                 # "Progression"
        elif choice == 2 : COMING_SOON()
        elif choice == 3 : #inp1(choice,cname)
            #choice1 = ''                          #return r, n, t, choice, cd, cr
            while choice1 != 0:
                choice1=inp1(choice,cname)[0]
                if choice1 in [1,2,4] :           # here!
                    if choice1 == 4 : p,choice1,text,ll,ul=listmaker(*rangen(choice1,choice))
                    else : p,choice1,text,ll,ul=listmaker(*rantoss(choice1,choice))
                    listdis(p,text) 
                    if choice1 in [2,4] : calc=listcalc(p,text,ll,ul)
                    rantoss(choice1,choice,p)
                    progsaves=saviour(progsaves,calc,p,text)
                elif choice1 == 3 : rangame(choice1,choice)
                '''elif choice1 == 4 :
                    p,choice1,text,ll,ul=listmaker(*rangen(choice1,choice))
                    listdis(p,text)
                    calc=listcalc(p,text,ll,ul)
                    progsaves=saviour(progsaves,calc,p,text)'''
                # elif choice1 == 5 : COMING_SOON()
        elif choice == 4 :                  # COMING_SOON()
            while choice1 != 0 :
                choice1=inp1(choice,cname)[0]
                # print(choice1)
                if choice1 in range(1,4) : codenames(choice1)
        elif choice == 5 : 
            choice1=inp1(choice,cname)[0]
            print("yfkdhdjhd")
            '''if choice1 in MAIN_MENU[choice][cname] : 
                print("HELLO")'''
            loading()
            if choice1 == 1 : dissave(progsaves,'Creation')               # 'Progression' 
            elif choice1 == 2 : pass  
        elif choice == 6 : COMING_SOON()
        elif choice == 7 : 
            locked(key=ADMIN_PASSWORD,type="Admin Password")
            '''for i in range(60):
                print(WHITE_BF+CURRENT_TIME_FILE(milli=False),end="\r")
                sleep(1)'''
            while choice1 != 0 : 
                choice1=inp1(choice,cname)[0]
                print(choice)
                settings()
        elif choice == 0 : terminator("MAIN")
        else: print(f"{RED_DF}Wrong Choice! Please Try Again!{END}\n") ; loading(t=2)
    except ValueError as s:
        e = str(s).split(": ",1)[1].strip("'")
        #print(PATH)
        #print(e)
        if e == PATH : scare()
        else: print(f"{RED_DF}Please Enter An Integer Option From The {ITALIC}Menu{END}{RED_DF} !{END}") ; loading("Quick")

# By Sanway Das, At Tirupati, 02-12-2025

#add colours (done!)     should we remove all END s?
#add dialog for save names
#add matrices
#add random number generators!
#caesar Ciphers and Pig Latins!
## ADD FUNCTION ONLY FOR YES/NO DIALOGUES (DONE)


#HOW TO SHARE UNEDITABLE CODES
# CAN I INCREASE FONT SIZES
# ADD A SETTING MENU TO THE MAIN MENU???        (HALF DONE)
# use enumerate     (DONE)
# use various kinds of random distribution
