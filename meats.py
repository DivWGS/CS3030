# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 11:55:46 2016

@author: dillon divich
"""

import random
import time

"""
USER HELP FOR INTERACTIVE CONSOLE
var = MSafe('S',1,0,32, 10) object creation
var.setMtemp(val) setters
var.getMtemp() getter
var.setout(val) useful methods
var.getDet() return all values

USER HELP FOR MEAT SAFETY
~~ -> general system info, operation success
## -> prompt info and help
** -> system error
"""

class MSafe:
    def __init__(self, mtype, mtemp, stemp, rtemp, weight):
        self.mtype = mtype
        self.mtemp = int(mtemp)
        self.stemp = int(stemp)
        self.rtemp = int(rtemp)
        self.weight = int(weight)
        self.safe = False
        self.to = 0
        self.dp = 0
        self.timethaw = 0
        self.refoz = False
        self.i = 0
        
    def setMtemp(self, val):
        self.mtemp = val
        
    def getMtemp(self):
        return self.mtemp
        
    def setWeight(self, val):
        self.weight = val
        
    def getWeight(self):
        return self.weight
        
    def setMtype(self, val):
        self.mtype = val
        
    def getMtype(self):
        return self.mtype
         
    def setStemp(self, val):
        self.stemp = val
        
    def getStemp(self):
        return self.stemp
        
    def setRtemp(self, val):
        self.rtemp = val
        
    def getRtemp(self):
        return self.rtemp        
        
    def setTo(self, val):
        self.to = val
        
    def getTo(self):
        return self.to
        
    def setDp(self, val):
        self.dp = val
        
    def getDp(self):
        return self.dp
        
    def setSafe(self, bool):
        self.safe = bool
        
    def getSafe(self):
        return self.safe
        
    def getDet(self):
        if str(self.mtype) == 'S':
            print("\nMeat Type: Steak")
        if str(self.mtype) == 'T':
            print("\nMeat Type: Turkey")
        print("Meat Temp: " + str(self.mtemp))
        print("Stored Temp: " + str(self.stemp))
        print("Room Temp: " + str(self.rtemp))
        print("Meat Weight: " + str(self.weight))
        print("Reforzen: " + str(self.refoz))
        print("Time Thawed: " + str(self.i) + " hours")
        print("Number of Times Thawed: " + str(self.timethaw))
        print("Safe to Cook: " + str(self.safe))
        print("Danger Points: " + str(self.dp))
        
    def setout(self, val):
        temp = 0
        self.i = 1
        self.to = val
        if self.to > 120 and self.mtemp > 50:
            self.safe = False
        while self.i < self.to:
            if self.mtemp >= self.rtemp:
                break
            else:
                self.safe = True
            if self.mtemp > 60:
                self.safe = False
            if str(self.mtype) == 'T':
                temp = random.random()+1
                if self.weight > 0 and self.weight < 6:
                    et = 1
                if self.weight >= 6 and self.weight < 12:
                    et = .45
                if self.weight >= 12 and self.weight <= 18:
                    et = .28
            if str(self.mtype) == 'S':
                temp = random.random()+1
                if self.weight > 0 and self.weight < 5:
                    et = 2
                if self.weight >= 5 and self.weight <= 15:
                    et = .45
            if self.refoz == True:
                self.dp += 2
            else:
                self.dp += 1
            self.i+=1
            self.mtemp += temp*et
        if self.mtemp > self.rtemp:
            self.mtemp -= temp * et
            self.i -= 1
            self.dp -= 1
        self.dp += 1
        self.timethaw += 1
                
                
    def setin(self, val):
        temp = 0
        self.i = 1
        self.to = val
        if self.to > 120 and self.mtemp > 50:
            self.safe = False
        while self.i < self.to and self.mtemp > self.stemp:
            temp = random.random()+4
            if self.mtemp > self.stemp:
                self.mtemp -= temp
            else:
                break
            self.i += 1
        self.to = 0
        self.refoz = True
    
    
class Unit():
    def chRan():
        if random.random() > 0 and random.random() < 1:
            print("PASS")
        else:
            print("FAIL")
                
    def chOut():
        meat = MSafe('S',0,0,32,10)
        meat.setout(60)
        if meat.refoz == False and meat.safe == True and meat.mtemp < meat.rtemp and meat.timethaw == 1:
            print("PASS")
        else:
            print("FAIL")
        meat = MSafe('T',0,0,32,10)
        meat.setout(60)
        if meat.refoz == False and meat.safe == True and meat.mtemp < meat.rtemp and meat.timethaw == 1 and meat.to == 60:
            print("PASS")
        else:
            print("FAIL")
            
    def chIn():
        meat = MSafe('S',0,0,10,5)
        meat.setout(60)
        meat.setin(60)
        if meat.refoz == True and meat.timethaw == 1 and meat.to == 0 and meat.mtemp < 0:
            print("PASS")
        else:
            print("FAIL")


print("\n\n\n")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("|Welcome to the Meat Safety Checker|")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
time.sleep(2)
meats = [None, None, None]
print("\n")
print("######################")
print("#1: Add a meat       #")
print("#2: Delete a meat    #")
print("#3: Set out to thaw  #")
print("#4: Refreeze         #")
print("#5: Get meat info    #")
print("#0: Quit             #")
print("######################")

uc = str(input("What would you like to do: "))

if uc == '1' or uc == '2' or uc == '0' or uc == '3' or uc == '4' or uc == '5':
    vc = True
else:
    vc = False
    
while vc == False:
    print("***********************")
    print("*ERROR: INVALID INPUT *")
    print("*1: Add a meat        *")
    print("*2: Delete a meat     *")
    print("*3: Set out to thaw   *")
    print("*4: Refreeze          *")
    print("*5: Get meat info     *")
    print("*0: Quit              *")
    print("***********************")
    uc = str(input("What would you like to do: "))
    if uc == '1' or uc == '2' or uc == '0' or uc == '3' or uc == '4' or uc == '5':
        vc = True
    
while vc == True and uc != '0':
    MeatType = 'S'
    MeatTemp = 0
    StoredTemp = 0
    RoomTemp = 0
    MeatWeight = 0
    
    if str(uc) == '1':
        i = 0
        if meats[0] != None and meats[1] != None and meats[2] != None:
            print("****************************")
            print("*ERROR: NO ROOM TO ADD MEAT*")
            print("****************************\n")
        else:
            MeatType = str(input("ENTER the type of meat (S or T): "))
            while str(MeatType) != 'S' and str(MeatType) != 'T':
                print("**********************")
                print("*ERROR: INVALID INPUT*")
                print("**********************")
                MeatType = str(input("ENTER the type of meat ('S','T'): "))
                
            MeatTemp = int(input("ENTER the temp of the meat (>50): "))
            while int(MeatTemp) > 50:
                print("**********************")
                print("*ERROR: INVALID INPUT*")
                print("**********************")
                MeatTemp = int(input("ENTER the temp of the meat: "))
                
            StoredTemp = int(input("ENTER the temp of the meat storage (>50): "))
            while int(StoredTemp) > 50:
                print("**********************")
                print("*ERROR: INVALID INPUT*")
                print("**********************")
                StoredTemp = int(input("ENTER the temp of the meat: "))
                
            RoomTemp = input("ENTER the temp of the thaw room : ")
            while type(RoomTemp) is int == False:
                print("**********************")
                print("*ERROR: INVALID INPUT*")
                print("**********************")
                RoomTemp = input("ENTER the temp of the meat: ")
                
            MeatWeight = input("ENTER the weight of the meat : ")
            if str(MeatType) == 'S':
                while int(MeatWeight) > 18 or int(MeatWeight) < 0:
                    print("**********************")
                    print("*ERROR: INVALID INPUT*")
                    print("**********************")
                    MeatWeight = int(input("ENTER the weight of meat: "))
            if str(MeatType) == 'T':
                while int(MeatWeight) > 15 or int(MeatWeight) < 0:
                    print("**********************")
                    print("*ERROR: INVALID INPUT*")
                    print("**********************")
                    MeatWeight = int(input("ENTER the weight of meat: "))
        
            while i < 3 and meats[0] == None or meats[1] == None or meats[2] == None:
            
                if meats[i] == None:
                    if i == 0:   
                        meatone = MSafe(MeatType, MeatTemp, StoredTemp, RoomTemp, MeatWeight)
                        meats[i] = meatone
                        print("~~~~~~~~~~~~~~~~~~~~~~~~~")
                        print("|Meat successfully added|")
                        print("~~~~~~~~~~~~~~~~~~~~~~~~~\n")
                    if i == 1:
                        meattwo = MSafe(MeatType, MeatTemp, StoredTemp, RoomTemp, MeatWeight)
                        meats[i] = meattwo
                        print("~~~~~~~~~~~~~~~~~~~~~~~~~")
                        print("|Meat successfully added|")
                        print("~~~~~~~~~~~~~~~~~~~~~~~~~\n")
                    if i == 2:
                        meatthree = MSafe(MeatType, MeatTemp, StoredTemp, RoomTemp, MeatWeight)
                        meats[i] = meatthree
                        print("~~~~~~~~~~~~~~~~~~~~~~~~~")
                        print("|Meat successfully added|")
                        print("~~~~~~~~~~~~~~~~~~~~~~~~~\n")
                    break
                else:
                    i+=1
        
    if str(uc) == '2':
        if meats[0] == None and meats[1] == None and meats[2] == None:
            print("**************************")
            print("*ERROR: NO MEAT TO DELETE*")
            print("**************************\n")
        else:
            print("~~~~~~~~~~~~~~~~~~~")
            print("|Slot availability|")
            if meats[0] != None:
                print("|1: Meat One      |")
            if meats[1] != None:
                print("|2: Meat Two      |")
            if meats[2] != None:
                print("|3: Meat Three    |")
            print("~~~~~~~~~~~~~~~~~~~")
            delt = int(input("What meat do you want to delete: "))
            while delt > 3 or delt < 0:
                print("**********************")
                print("*ERROR: INVALID INPUT*")
                print("**********************")
                delt = int(input("What meat do you want to delete: "))
            if meats[delt-1] != None:
                meats[delt-1] = None
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("|Meat successfully deleted|")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
            else:
                print("**************************")
                print("*ERROR: NO MEAT TO DELETE*")
                print("**************************\n")
                      
    if str(uc) == '3':
        if meats[0] == None and meats[1] == None and meats[2] == None:
            print("************************")
            print("*ERROR: NO MEAT TO THAW*")
            print("************************\n")
            
        else:
            print("~~~~~~~~~~~~~~~~~~~")
            print("|Slot availability|")
            if meats[0] != None:
                print("|1: Meat One      |")
            if meats[1] != None:
                print("|2: Meat Two      |")
            if meats[2] != None:
                print("|3: Meat Three    |")
            print("~~~~~~~~~~~~~~~~~~~")
            thaw = int(input("What meat do you want to thaw: "))
            while thaw > 3 or thaw < 0:
                print("**********************")
                print("*ERROR: INVALID INPUT*")
                print("**********************")
                thaw = int(input("What meat do you want to thaw: "))
            thawtime = int(input("ENTER how long to thaw: "))
            
            while type(thawtime) is int == False:
                print("**********************")
                print("*ERROR: INVALID INPUT*")
                print("**********************")
                thawtime = input("ENTER how long to thaw: ")
            
            if meats[thaw-1] != None:
                if thaw-1 == 0:
                    meatone.setout(thawtime)
                if thaw-1 == 1:
                    meattwo.setout(thawtime)
                if thaw-1 == 2:
                    meatthree.setout(thawtime)
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("|Meat successfully thawed|")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
            else:
                print("************************")
                print("*ERROR: NO MEAT TO THAW*")
                print("************************\n")
                
    if str(uc) == '4':
        if meats[0] == None and meats[1] == None and meats[2] == None:
            print("****************************")
            print("*ERROR: NO MEAT TO REFREEZE*")
            print("****************************\n")
        else:
            print("~~~~~~~~~~~~~~~~~~~")
            print("|Slot availability|")
            if meats[0] != None:
                print("|1: Meat One      |")
            if meats[1] != None:
                print("|2: Meat Two      |")
            if meats[2] != None:
                print("|3: Meat Three    |")
            print("~~~~~~~~~~~~~~~~~~~")
            freeze = int(input("What meat do you want to refreeze: "))
            while freeze > 3 or freeze < 0:
                print("**********************")
                print("*ERROR: INVALID INPUT*")
                print("**********************")
                freeze = int(input("What meat do you want to refreeze: "))
            freezetime = int(input("ENTER how long to thaw: "))
            
            while type(freezetime) is int == False:
                print("**********************")
                print("*ERROR: INVALID INPUT*")
                print("**********************")
                freezetime = input("ENTER how long to refreeze: ")
            
            if meats[freeze-1] != None:
                if freeze-1 == 0:
                    meatone.setin(freezetime)
                if freeze-1 == 1:
                    meattwo.setin(freezetime)
                if freeze-1 == 2:
                    meatthree.setin(freezetime)
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("|Meat successfully refreezed|")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
            else:
                print("****************************")
                print("*ERROR: NO MEAT TO REFREEZE*")
                print("****************************\n")
                
    if str(uc) == '5':
        if meats[0] == None and meats[1] == None and meats[2] == None:
            print("****************************")
            print("*ERROR: NO MEAT TO GET INFO*")
            print("****************************")
        else:
            print("~~~~~~~~~~~~~~~~~~~")
            print("|Slot availability|")
            if meats[0] != None:
                print("|1: Meat One      |")
            if meats[1] != None:
                print("|2: Meat Two      |")
            if meats[2] != None:
                print("|3: Meat Three    |")
            print("~~~~~~~~~~~~~~~~~~~")
            info = int(input("What meat do you want the info for: "))
            while info > 3 or info < 0:
                print("**********************")
                print("*ERROR: IVALID INPUT*")
                print("**********************")
                info = int(input("What meat do you want the info for : "))
            
            if meats[info-1] != None:
                if info-1 == 0:
                    meatone.getDet()
                if info-1 == 1:
                    meattwo.getDet()
                if info-1 == 2:
                    meatthree.getDet()
                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("|Meat info successfully shown|")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
            else:
                print("***************************")
                print("*ERROR:MEAT INFO NOT SHOWN*")
                print("***************************\n")

    print("######################")
    print("#1: Add a meat       #")
    print("#2: Delete a meat    #")
    print("#3: Set out to thaw  #")
    print("#4: Refreeze         #")
    print("#5: Get meat info    #")
    print("#0: Quit             #")
    print("######################")
    uc = str(input("What would you like to do: "))
    if uc == '1' or uc == '2' or uc == '0' or uc == '3' or uc == '4' or uc == '5':
        vc = True
    else:
        vc = False
    
    while vc == False:
        print("***********************")
        print("ERROR: INVALID INPUT  *")
        print("1: Add a meat         *")
        print("2: Delete a meat      *")
        print("3: Set out to thaw    *")
        print("4: Refreeze           *")
        print("5: Get meat info      *")
        print("0: Quit               *")
        print("***********************")
        uc = str(input("What would you like to do: "))
        if uc == '1' or uc == '2' or uc == '0' or uc == '3' or uc == '4':
            vc = True
        

if uc == '0':
    print("~~~~~~~~~")
    print("|Goodbye|")
    print("~~~~~~~~~")
    time.sleep(3)
    quit()
else:
    print("**************")
    print("*ERROR: FATAL*")
    print("**************")
    time.sleep(3)
    quit()

