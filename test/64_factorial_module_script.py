#WAPP to find factorial of a given number using module script

def fact(n):
      return 1 if n==1 else n*fact(n-1)
if(__name__=="__main__"):
      import sys
      fact(int(sys.argr[1]))
#c:\user\python 32\python fact 5
