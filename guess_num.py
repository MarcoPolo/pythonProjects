
isnum=True


def main():
 print 'Think of a number between 0-999'
 findNum(0,1000)


def findMid(pt1,pt2):
 midpt=(pt2-pt1)/2
 midpt+=pt1
 return midpt

def findNum(firstNum,endNum):
  numGuess=findMid(firstNum, endNum)
  print 'Is ' + str(numGuess) + ' too high (h) or too low (l) or correct (c)'
  usr = raw_input()
  if(usr=='h'):
   endNum=numGuess
   findNum(firstNum, endNum)
   return
  elif usr=='l':
   firstNum=numGuess
   findNum(firstNum, endNum)
  elif usr=='c':
   print "Sw33t"
  else:
   print "Sorry I didn't catch that"
   findNum(firstNum, endNum)

if __name__=='__main__':
	main()
