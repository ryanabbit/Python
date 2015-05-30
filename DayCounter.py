#
# hw8pr1.py
#
# name: Yung,Jui,Chen(Ryan)
#

class Date:
    """ a user-defined data structure that
        stores and manipulates dates
    """

    # the constructor is always named __init__ !
    def __init__(self, month, day, year):
        """ the constructor for objects of type Date """
        self.month = month
        self.day = day
        self.year = year


    # the "printing" function is always named __repr__ !
    def __repr__(self):
        """ This method returns a string representation for the
            object of type Date that calls it (named self).

             ** Note that this _can_ be called explicitly, but
                it more often is used implicitly via the print
                statement or simply by expressing self's value.
        """
        s =  "%02d/%02d/%04d" % (self.month, self.day, self.year)
        return s


    # here is an example of a "method" of the Date class:
    def isLeapYear(self):
        """ Returns True if the calling object is
            in a leap year; False otherwise. """
        if self.year % 400 == 0: return True
        elif self.year % 100 == 0: return False
        elif self.year % 4 == 0: return True
        
        return False
    
    
    def copy(self):
        """ Returns a new object with the same month, day, year
            as the calling object (self).
        """
        dnew = Date(self.month, self.day, self.year)
        return dnew

    

    def equals(self, d2):
        """ Decides if self and d2 represent the same calendar date,
            whether or not they are the in the same place in memory.
        """
        if self.year == d2.year and self.month == d2.month and self.day == d2.day:
            return True
        else:
            return False


    def tomorrow(self):


        fdays=28+self.isLeapYear()
        DIM = [0,31,fdays,31,30,31,30,31,31,30,31,30,31]
        self.day+=1
        if self.day>DIM[self.month]:
            self.month+=1
            self.day=1

            if self.month>12:
                self.year+=1
                self.month=1
      

    def yesterday(self):
        fdays=28+self.isLeapYear()
        DIM = [0,31,fdays,31,30,31,30,31,31,30,31,30,31]

        self.day-=1
        if self.day==0:
         self.month-=1
         self.day=DIM[self.month]
         if self.month==0:
              self.day=DIM[len(DIM)-1]
              self.month=12
              self.year-=1
          
    def addNDays(self,N):
        print self
        for i in range(N):
          tmp=self.tomorrow()
          print self

    def subNDays(self,N):
        print self
        for i in range(N):
         tmp=self.yesterday()
         print self

    def isBefore(self,d2):

        if self.year<d2.year:
            return True
        elif self.year==d2.year:
            if self.month<d2.month:
             return True
            elif self.month==d2.month:
              if self.day<d2.day:
                return True
              else:
                return False
        else:
           return False
 
    def isAfter(self,d2):

        if self.equals(d2):
            return False
        elif self.isBefore(d2):
            return False
        else:
            return True


    def diff(self,d2):
      count=0
      tmpday=self.copy()
      while tmpday.isBefore(d2):
       tmpday.tomorrow()
       count-=1
      
      while tmpday.isAfter(d2):
       tmpday.yesterday()
       count+=1
       
      return count

    def dow(self):
        knowndate=Date(11,10,2013) #Based on Sunday
        diff=self.diff(knowndate)
        tmp=diff%7
        if tmp==1:
         return "Monday"
        if tmp==2:
         return "Tuesday"
        if tmp==3:
         return "Wednesday"
        if tmp==4:
         return "Thursday"
        if tmp==5:
         return "Friday"
        if tmp==6:
         return "Saturday"
        if tmp==0:
         return "Sunday"

        
    def dow2(self, refDate):
        knowndate=refDate # Based on Friday
 
        diff=self.diff(knowndate)
        tmp=diff%7
        if tmp==1: 
         return "Wednesday"
        if tmp==2:
         return "Thursday"
        if tmp==3:
         return "Friday"
        if tmp==4:
         return "Saturday"
        if tmp==5:
         return "Sunday"
        if tmp==6:
         return "Monday"
        if tmp==0:
         return "Tuesday"


        
def nycounter():
    """Looking ahead to 100 years of NY celebrations..."""

    dowd = {}              # dowd == 'day of week dictionary'
    dowd["Sunday"] = 0     # a 0 entry for Sunday
    dowd["Monday"] = 0     # and so on...
    dowd["Tuesday"] = 0
    dowd["Wednesday"] = 0
    dowd["Thursday"] = 0
    dowd["Friday"] = 0
    dowd["Saturday"] = 0

    # live for another 100 years...
    for year in range(2013, 2114):
        d = Date(1, 1, year)   # get ny
        print 'Current date is', d
        s = d.dow()        # get day of week
        dowd[s] += 1       # count it

    print 'totals are', dowd

    # we could return dowd here
    # but we don't need to right now
    # return dowd

#Question1
# This function calulates each day from the years between the range.
# It uses function dow() to indicate the day, and uses the day as an index in
# dictionary dowd.


def birthday():
    dowd = {}              # dowd == 'day of week dictionary'
    dowd["Sunday"] = 0     # a 0 entry for Sunday
    dowd["Monday"] = 0     # and so on...
    dowd["Tuesday"] = 0
    dowd["Wednesday"] = 0
    dowd["Thursday"] = 0
    dowd["Friday"] = 0
    dowd["Saturday"] = 0
    for year in range(2014,2014+100+1):
        d=Date(04,29,year)
        print 'My birthday is',d
        s=d.dow()
        dowd[s]+=1

    print 'totals are', dowd
        
    
def thirteenthcounter():
    refDate=Date(04,04,2014) #it is a Friday
    dowd = {}              # dowd == 'day of week dictionary'
    dowd["Sunday"] = 0     # a 0 entry for Sunday
    dowd["Monday"] = 0     # and so on...
    dowd["Tuesday"] = 0
    dowd["Wednesday"] = 0
    dowd["Thursday"] = 0
    dowd["Friday"] = 0
    dowd["Saturday"] = 0
    for year in range(2014,2014+400+1): #From now to next 400 year
        for month in range(1,13):       # From Jan to Dec
            d=Date(month,13,year)       #set every 13th in each month in that year
            s=d.dow2(refDate)           
            dowd[s]+=1
            #print month, '/13/',year,' is ',s
            if s=='Friday':             # dow2 caculate days based on Friday
             refDate=Date(month,13,year)# In order to reduce the range to caculate, it renews refDate if it is a Friday. 
    print 'totals are', dowd
        
