#
# Your name:Yung-Jui,Chen(Ryan)
#
#

import math
import sys
def menu():
    """ a function that simply prints the menu """
    print
    print "(1) Enter a list"
    print "(2) Predict the next element"
    print "(9) Quit"
    print

def TTS():
  
  nums=[]
  tmp=True
  while tmp:
    print "(0) Input a new list"
    print "(1) Print the current list"
    print "(2) Find the average price"
    print "(3) Find the standard deviation"
    print "(4) Find the min and its day"
    print "(5) Find the max and its day"
    print "(6) Your TT investment plan"
    print "(9) Quit"
    user=input("Enter your choice:")
    if user not in ([0,1,2,3,4,5,6,9]):
     print "Please input a correct number"
    if user==9:
     tmp=False
    if user==0:
     nums=input("Enter a new list of prices:")
    if user==1:
     if len(nums)==0:
       nums=input("Please Enter a new list of prices:")
     else:
      printcurrent(nums)
      
    if user==2:
     if len(nums)==0:
       nums=input("Please Enter a new list of prices:")
     else:
      print("The average price is" "%7.2f"%(avg(nums)))
      
    if user==3:
     if len(nums)==0:
       nums=input("Please Enter a new list of prices:")
     else:
      standard(nums)
      
    if user==4:
     if len(nums)==0:
       nums=input("Please Enter a new list of prices:")
     else:
      mini(nums)
    if user==5:
     if len(nums)==0:
       nums=input("Please Enter a new list of prices:")
     else:
      maxi(nums)
    if user==6:
     if len(nums)==0:
       nums=input("Please Enter a new list of prices:")
     else:
      TT(nums)

def main():
    """ the main user-interaction loop """

    L = [12,22,32]  # an initial list

    while True:     # the user-interaction loop
        print "\nThe list is", L
        menu()
        uc = input( "Choose an option: " )

        if uc == 9: # we want to quit
            break

        elif uc == 1:  # we want to enter a new list
            L = input("Enter a new list: ")

        elif uc == 2:  # predict and add the next element
            n = predict(L)
            L = L + [n]

        else:
            print "That's not on the menu!"

    print
    print "I knew you were going to quit!"
        
def printcurrent(nums):
 print " "   
 print ("DAY  Price")
 print ("---  -----")
 for i in range(len(nums)):
  print(i,"%7.2f"% nums[i])
 print " "


def avg(nums):
 tmp=0
 for a in range(len(nums)):
  tmp+=nums[a]
 
 return tmp/len(nums)

def standard(nums):
 avgtmp=avg(nums)
 tmp=0
 for i in range(len(nums)):
    tmp+=(nums[i]-avgtmp)**2

 print " "
 print("The st. deviation is " "%7.2f"%((tmp/len(nums))**0.5))
 print " "
 return (tmp/len(nums))**0.5
 
 return

def mini(nums):
 small=nums[0]
 day=0
 for i in range(len(nums)):
  if nums[i]<small:
   small=nums[i]
  if small==nums[i]:
    day=i
 print " "
 printstr="The min is "+str(small)+" on day "+str(day)
 print printstr
 print " "
 return small,day

def maxi(nums):
 large=0
 day=0
 for i in range(len(nums)):
  if nums[i]>large:
   large=nums[i]
  if large==nums[i]:
    day=i
 print " "
 printstr="The max is "+str(large)+" on day "+str(day)
 print printstr
 print " "

 return large,day


def TT(nums):
    
 profit=0
 maxprofit=-1
 sell=0
 buy=0
 sellamount=0
 buyamount=0
 for a in range(len(nums)):
  for s in range(a,len(nums)):
    profit=nums[s]-nums[a]
    if profit>maxprofit:
     maxprofit=profit
     sell=a
     buy=s
     sellamount=nums[a]
     buyamount=nums[s]
 printstr="Buy on day "+str(buy)+" at price "+str(buyamount)
 print " "
 print printstr
 printstr="Sell on day "+str(sell)+" at price"+str(sellamount)
 
 print printstr
 printstr="For a total profit of "+str(maxprofit)
 print printstr
 print " "
 return maxprofit,sell,buy
     
     

    
 
