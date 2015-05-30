# Name: Yung-Jui,Chen(Ryan)




class Board:
    """ a datatype representing a C4 board
        with an arbitrary number of rows and cols
    """
    
    def __init__( self, width, height ):
        """ the constructor for objects of type Board """
        self.width = width
        self.height = height
        W = self.width
        H = self.height
        self.data = [ [' ']*W for row in range(H) ]

        # we do not need to return inside a constructor!
        

    def __repr__(self):
        """ this method returns a string representation
            for an object of type Board
        """
        H = self.height
        W = self.width
        s = ''   # the string to return
        for row in range(0,H):
            s += '|'   
            for col in range(0,W):
                s += self.data[row][col] + '|'
            s += '\n'

        s += (2*W+1) * '-'    # bottom of the board
        s+='\n'
        for i in range(0,W):
         if i >=10:
          s+=' '+str(i%10)
         else:
          s+=' '+str(i)
        return s       # the board is complete, return it


    def addMove(self, col, ox):
       H = self.height
   
       if self.data[0][col]==' ':
        for i in range(0,H):
         if self.data[abs(i-(H-1))][col]==' ':
          self.data[abs(i-(H-1))][col]=ox
          return
        
    def clear(self):
        H = self.height
        W = self.width
        for row in range(0,H):
         for col in range(0,W):
             self.data[row][col]=" "


    def setBoard( self, moveString ):
        """ takes in a string of columns and places
            alternating checkers in those columns,
            starting with 'X'
            
            For example, call b.setBoard('012345')
            to see 'X's and 'O's alternate on the
            bottom row, or b.setBoard('000000') to
            see them alternate in the left column.

            moveString must be a string of integers
        """
        nextCh = 'X'   # start by playing 'X'
        for colString in moveString:
            col = int(colString)
            if 0 <= col <= self.width:
                self.addMove(col, nextCh)
            if nextCh == 'X': nextCh = 'O'
            else: nextCh = 'X'

    def allowsMove(self,c):
      if c>=self.width or c<0:
         return False
        
      elif self.data[0][c]==' ':
       return True
      else:
       return False

    

    def isFull(self):
      W=self.width
      for i in range(0,W-1):
        if self.allowsMove(i):
          return False
      return True
        



    def delMove(self,c):
       H = self.height
       for i in range(0,H):
         if self.data[i][c] in 'OX':
          self.data[i][c]=' '
          return



    def winsFor(self, ox):


        H = self.height
        W = self.width
        D = self.data
        # check for horizontal wins
        for row in range(0,H):
            for col in range(0,W-3):
                if D[row][col] == ox and \
                   D[row][col+1] == ox and \
                   D[row][col+2] == ox and \
                   D[row][col+3] == ox:
                    return True

        for row in range(0,H-3):
            for col in range(0,W):
                if D[row][col] == ox and \
                   D[row+1][col] == ox and \
                   D[row+2][col] == ox and \
                   D[row+3][col] == ox:
                    return True

        for row in range(0,H-3):
            for col in range(0,W-3):
              if D[row][col] == ox and \
                 D[row+1][col+1] == ox and \
                 D[row+2][col+2] == ox and \
                 D[row+3][col+3] == ox:
                   return True


        for row in range(0,H-3):
            for col in range(0,W+3):
              if D[row][abs(col-(W-1))] == ox and \
                 D[row+1][abs(col-(W-1))-1] == ox and \
                 D[row+2][abs(col-(W-1))-2] == ox and \
                 D[row+3][abs(col-(W-1))-3] == ox:
                   return True

        return False


    def hostGame(self):
        print "Welcome to Connect Four!\n"
        print 
        while True:
            
         print self
         print
         # For X's input
         user=input("X's choice:" )
         print user
         if self.isFull():
          print "The Game is Over!"
          break
         while self.allowsMove(user) == False:
             user = input("Choose a right column: ")

         self.addMove(user,'X')
         print self
         if self.winsFor("X"):
            print ("X wins -- Congratulations!")
            break
         # For O's input
         user=input("O's choice:" )
         if self.isFull():
          print "The Game is Over!"
          break
         while self.allowsMove(user) == False:
             user = input("Choose a right column: ")

         self.addMove(user,'O')
     
         if self.winsFor("O"):
            print ("O wins -- Congratulations!")
            break
         
          
        
