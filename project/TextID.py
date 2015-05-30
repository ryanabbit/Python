# Name: Yung-Jui,Chen(Ryan)
# Milestone
# This TextID project enables user start at "Main()" function.
# It provides users to compare the files and string
# And I added TextClound function to enable users choose the file and to
# see the frequency of that file on browser. Users can decide the MAXWIRDS.
# We provided threee different text files(1/2/3) in the zip file.


import pickle
import math
import random
import os
import webbrowser
import operator

class TextModel:
    
    def __init__( self, name ):
        """ the constructor for objects of textmodel """
        self.name = name
        self.words= {}
        self.wordlengths={}
        self.stems={}
        self.sentencelengths={}
        
   
    def __repr__(self):
        """ returns a string representation """
        s = "a text model with name: " + self.name + "\n"
        s += "  number of words is " + str(len(self.words)) + "\n"
        s += "  number of lengths " + str(len(self.wordlengths)) +"\n"
        s += "  number of stems " + str(self.stems) +"\n"
        s += "  number of sentence lengths " + str(len(self.sentencelengths)) +"\n"
        
        return s
        
    def addTextFromString(self, s):
        """ analyzes the string s and adds its pieces
            to all of the dictionaries in this text model
        """
       
        s=self.cleanText(s)
        LoW = s.split()
        for w in LoW:
            if w not in self.words:
                self.words[w] = 1
                
            else:
                self.words[w] += 1

            if len(w) not in self.wordlengths:
                self.wordlengths[len(w)]=1
            else:
                self.wordlengths[len(w)]+=1
            
    def addTextFromFile(self, filename):
          f=open(filename)
          text=f.read()
          f.close()
          self.addTextFromString(text)

    def cleanText(self, s):
        LoW=s.split()
        count=0
        for w in LoW:
            count+=1
            if w[-1] in [".","?","!"]:
                if w not in self.sentencelengths:
                 self.sentencelengths[str(count)]=1
                 count=0
                else:
                 self.sentencelengths[str(count)]+=1
                 count=0
        s=s.replace(".","")
        s=s.replace("?","")
        s=s.replace("!","")
        s=s.replace("'","")
        s=s.replace(":","")
        s=s.replace(";","")
        s=s.replace("(","")
        s=s.replace(")","")
        s=s.replace("[","")
        s=s.replace("]","")
        s=s.replace("&","")
        s=s.replace(",","")
        s=s.replace('"',"")
        s=s.replace("-","")
        s=s.replace("&","")
        s=s.replace("*","")
        s=s.replace("/","")
     
        
        
        return s.lower()

    # I used pickle to store and retrieve the values of the object in a file.
    def saveDataToFile(self):
        with open('newtext.txt','w') as output:
         
         pickle.dump(self,output,pickle.HIGHEST_PROTOCOL)
        
      
        
    def readDataFromFile(self):
        with open("newtext.txt","r") as input:
         new1=pickle.load(input)
         self.words= new1.words
         self.wordlengths= new1.wordlengths
         self.stems= new1.stems
         self.sentencelengths= new1.sentencelengths
         
    ## We haven not finished this function.....   
    def stem(self, w):
        if w[-3:]=="ies":
            return w[:-2]
        elif w[-3:]=='ing' and\
             e[-4:-3]==w[-5:-4]:
            return w[:-4]


    def matchScore(self, other):
        score=1
        total=0
        for i in range(len(self.words.values())):
            total+=self.words.values()[i]
        
        for i in other.words:
          if i in self.words:
             
             score*=math.log(self.words.get(i)/(total+0.0))*other.words.get(i)
          
             

          else:
             score*=math.log(1.0/total)*other.words.get(i)
            
        return score
    

    def ShowTextCloud(self,Maxwords):
      """This function enable user choose a file to see the frequency of that fil.
           User input the MaxWords to decide how many words are going to be shown in
           the browser. I used html_string to store the HTML format in a new file
           and imported webbroswer to open that file. I also imported "OS" to get
           the absolute path of that file.
      """
      fileroot="file://"
      filename="TextCloud.html"
      wordlist=self.sort()
      title=1200
      html_string=""
      colorlist=["darkred","red","blue","gray","green","black"]
      color="red"
      Nowords=["it","they","them","is","are","was","were","for","to","the","a","an" \
               ,"if","this","as","i","like","you","he","she","will","can","so","of" \
               ,"that","in","on","at","by","do","does","did","but","however","what"\
               , "where","how","why","who","and","be","been","my","your","his","her"\
               ,"has",'have','not','these','those','its','we','our',"or"]
      
      if Maxwords>len(wordlist):
          Maxwords=len(wordlist)
          
      for i in range(Maxwords):
        if wordlist[i][0] not in Nowords:  
         html_string+='<abbr title =1267 style="font-size:'+str(title)+'%; color:'+color+'">'+str(wordlist[i][0])+'</abbr> &nbsp; &nbsp;'
         if i<len(wordlist)-1:
          if wordlist[i][1]>wordlist[i+1][1]:
           title=title*0.5
           color=random.choice(colorlist)
           
      f = open( filename, "w" )  # open for writing
      print >> f      # prints a blank line
      print >> f, html_string   # prints the data
      print >> f
      f.close()       # close the file
      webbrowser.open(fileroot+os.path.abspath(filename))
      
    def sort(self):
     words=self.words
     newlist=sorted(words.iteritems(), key=operator.itemgetter(1),reverse=True)
     return newlist


## this is the main function. This program starts at this function 

def main():

  print ("Welcome to TextID final project!")
  print ("Please input two articles and one text to compare!")
  
  first=TextModel("1")
  second=TextModel("2")
  other=TextModel("3")
  print ("Would you like to add text from the file or from typing string?")
  user=input("    1=>file,2 =>String:  ")
  if user==1:
      
      firstfile=input("Please give me the name of the first file(EX:test.txt): ")
      secondfile=input("Please give me the name of the second file: ")
      otherfile=input("Please give me the name of the file to compare: ")
      print
      first.addTextFromFile(firstfile)
      second.addTextFromFile(secondfile)
      other.addTextFromFile(otherfile)
  elif user==2:
      
      firststr=input("Please give me the first string: ")
      secondstr=input("Please give the the second string: ")
      otherstr=input("Please give the string to compare: ")
      print
      first.addTextFromString(firststr)
      second.addTextFromString(secondstr)
      other.addTextFromString(otherstr)

  score1=first.matchScore(other)
  print ("First  vs Other gives a score of", score1)
  score2=second.matchScore(other)
  print ("Scond  vs Other gives a score of", score2)
  print   
      
  show=input("Which TextCould would you like to see? 1(First)/2(Second)/3(Other) ?")
  MaxWords=input("How many words would you like to see? ")
  if show==1:
      first.ShowTextCloud(int(MaxWords))
  
  elif show==2:

      second.ShowTextCloud(int(MaxWords))
  elif show==3:
      other.ShowTextCloud(int(MaxWords))
    
